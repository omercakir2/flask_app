from flask import Flask,jsonify
#api klasörunun içindekileri appde çalıştırmak için önce import etmemiz lazım.

from api.users import apiUsers
from api.admins import apiAdmins
from api.products import apiProducts

 #databasei ecommerceden import etmek lazım
from ecommerce import createApp
from ecommerce.initialize_db import createDB


app = createApp()
createDB()


#ardından blueprint ile appimize kayıt ettik
app.register_blueprint(apiAdmins)
app.register_blueprint(apiUsers)
app.register_blueprint(apiProducts)

@app.route('/')
#app.route'un içindeki '/' slash localhosta (127.0.0.1)in sonuna eklenecek şeyi belirler.örn: 127.0.0.1/
#slash / yerine /x koysaydık , appe gitmek için 127.0.0.1/x yapmalıydık!!


def hello_page():
    return jsonify("Welcome to our website")



@app.route('/profile')

def profile_page():
    return jsonify({"profile id": "your id"})


if __name__ == '__main__':
    app.run(debug=True)


