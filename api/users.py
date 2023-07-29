from flask import Flask,jsonify,Blueprint

apiUsers =Blueprint('apiUsers',__name__,url_prefix='/api/users')





@apiUsers.route('/')
def users_func():
    allUsers = [{"id":1,"username":"ahmetemrecakir","followers":98 },{"id":2,"username":"kenanfarukcakir","followers":242},{"id":3,"username":"omercakir","followers":41}]


    return jsonify({"success":True,"data":allUsers})


@apiUsers.route("/<int:id>")
def user(id):
    user= {"id":4,"username":"id4user","followers":421}

    return jsonify({"succes":True,"userdata":user})


