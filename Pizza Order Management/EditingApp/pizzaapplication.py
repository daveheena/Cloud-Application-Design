from database_connection import r
import sys
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from bottle import get, post, run, debug, default_app, request, template, static_file 	

if __name__ == '__main__':
    channel = sys.argv[1]

    pubsub = r.pubsub()
    pubsub.subscribe(channel)

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@get("/")
@get("/pizza")
def pizza():
	orders = {}
	for item in r.keys():
			orders[int(item)] = int(r.get(item))
	return template("addpizza",rows=orders)

@post("/addpizza")
def addpizzatodb():
	orderid = request.POST.get('orderid','').strip()
	orderstatus = request.POST.get('orderstatus','').strip()
	r.set(orderid,orderstatus)
	orders = {}
	for item in r.keys():
			orders[int(item)] = int(r.get(item))
	return template("addpizza",rows=orders)

@get("/updatepizza/<params>")
def updatepizzatodb(params):
	orderid = params[int(params.index(':'))+1:int(params.index('&'))]
	orderstatus = params[-1:]
	r.set(orderid,orderstatus)
	orders = {}
	for item in r.keys():
			orders[int(item)] = int(r.get(item))
	return template("addpizza",rows=orders)
	
@get("/deletepizza/<orderid>")
def deletepizzafromdb(orderid):
	r.delete(str(orderid))
	orders = {}
	for item in r.keys():
			orders[int(item)] = int(r.get(item))
	return template("addpizza",rows=orders)
	
debug(True)
run(host='0.0.0.0', port=8080)