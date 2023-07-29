from flask import Flask,jsonify
from api.users import apiUsers
from api.admins import apiAdmins
from api.products import apiProducts


omer = "Omer"

app = Flask(__name__)

app.register_blueprint(apiAdmins)
app.register_blueprint(apiUsers)
app.register_blueprint(apiProducts)



@app.route('/')
def hello_page():
    return jsonify("this is our welcome page")



@app.route('/profile')

def profile_page():
    return jsonify({"profile id": "your id"})


if __name__ == '__main__':
    app.run(debug=True)
