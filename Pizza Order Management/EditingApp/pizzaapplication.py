from database_connection import r
import sys
import warnings
import redis
import time

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from bottle import get, post, run, debug, default_app, request, template, static_file, redirect 	

orders = {}
if __name__ == "__main__":
	channel = "database_connection.py"
	pubsub = r.pubsub()
	pubsub.subscribe(channel)
	
@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@get("/")
@get("/pizza")
@post("/")
def pizza():
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

@post("/updatepizza")
def updatepizzatodb():
	orderid = request.POST.get('orderid','').strip()
	orderstatus = request.POST.get('status','').strip()
	r.set(orderid,orderstatus)
	
@post("/deletepizza")
def deletepizzafromdb():
	orderid = request.POST.get('orderid','').strip()
	r.delete(str(orderid))
	pubsub = r.pubsub()
	pubsub.subscribe(channel)
	orders = {}
	for item in r.keys():
			orders[int(item)] = int(r.get(item))
	return template("addpizza",rows=orders)
	
debug(True)
run(host='0.0.0.0', port=8080,reloader=True)