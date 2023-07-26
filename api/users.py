from flask import Flask,jsonify,Blueprint

apiUsers =Blueprint('apiUsers',__name__,url_prefix='/api/users')


@apiUsers.route('/')
def users_func():
    return jsonify({"success":True,"messages":"hello users"})
