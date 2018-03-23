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
	orders = []
	return template("checkpizzastatus",rows=orders)

@post("/getpizza")
def getpizza():
	orderid = request.POST.get('orderid','').strip()
	orderstatus = r.get(orderid)
	print(orderstatus)
	orders = []
	orders.append(orderstatus)
	return template("checkpizzastatus",rows=orders)

debug(True)
run(host='0.0.0.0', port=8080)