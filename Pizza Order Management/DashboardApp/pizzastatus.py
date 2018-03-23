import warnings
import mysql.connector

from database_connection import cnx

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from bottle import get, post, run, debug, default_app, request, template, static_file, redirect
	
@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@get("/")
@get("/pizza")
def pizza():
	result = ()
	return template("checkpizzastatus",rows=result)

@post("/getpizza")
def getpizza():
	result = ()
	orderid = request.POST.get('orderid','').strip()
	cursor = cnx.cursor()
	cursor.execute('SELECT * FROM orders WHERE orderid = %s',(int(orderid),))
	result = cursor.fetchone()
	cursor.close()
	return template("checkpizzastatus",rows=result)

debug(True)
run(host='0.0.0.0', port=8080)