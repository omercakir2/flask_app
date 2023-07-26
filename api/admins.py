from flask import Flask,jsonify, Blueprint

apiAdmins =Blueprint('apiAdmins',__name__,url_prefix='/api/admins')


@apiAdmins.route('/')
def admins_func():
    return jsonify({"success":True,"messages":"hello admins"})

@apiAdmins.route('/admin1')
def index2():
    return jsonify("Welcome admin1")