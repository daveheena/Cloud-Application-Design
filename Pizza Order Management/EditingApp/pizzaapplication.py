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
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM orders')
    result = cursor.fetchall()
    cursor.close()
    return template("addpizza",rows=result)

@post("/addpizza")
def addpizzatodb():
    orderid = request.POST.get('orderid','').strip()
    orderstatus = request.POST.get('orderstatus','').strip()
    cursor = cnx.cursor()
    cursor.execute("""INSERT INTO orders(orderid,orderstatus) VALUES (%s, %s)""",(int(orderid),int(orderstatus)))
    cursor.close()
    cnx.commit()
    return redirect("/")

@post("/updatepizza")
def updatepizzatodb():
	orderid = request.POST.get('id','').strip()
	orderstatus = request.POST.get('status','').strip()
	cursor = cnx.cursor()
	cursor.execute("""UPDATE orders SET orderstatus= %s WHERE orderid = %s""",(int(orderstatus),int(orderid)))
	cursor.close()
	cnx.commit()
	return redirect("/")

@post("/deletepizza")
def deletepizzafromdb():
    orderid = request.POST.get('id','').strip()
    cursor = cnx.cursor()
    cursor.execute("""DELETE FROM orders WHERE orderid = %s""",(int(orderid),))
    cursor.close()
    cnx.commit()
    return redirect("/")

debug(True)
#run(host='0.0.0.0', port=8080)
application = default_app()