# -*- coding: utf-8 -*-
import cx_Oracle
from bottle import route, run, template, static_file, request, redirect, response, get, post, default_app

#ruta index
@route('/')
def index():

    return template("index.tpl")

#ruta busqueda
@route('/acceso',method='POST')

def acceso():

	username = request.forms.get('username')
	password = request.forms.get('password')
	host = request.forms.get('host')
	basedatos = request.forms.get('basedatos')

	nombre = []

	connection = cx_Oracle.connect(str(username)+"/"+str(password)+"@"+str(host)+"/"+str(basedatos))
	cursor = connection.cursor()
	cursor.execute("select * from sergio.pilotos")
	info = cursor.fetchall()
	for datos in info:
		nombre.append(datos[0])
	return template('acceso.tpl', nombre=nombre)
	cursor.close()

@route('/views/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='views')

run (host='localhost', port='8080', debug='True')