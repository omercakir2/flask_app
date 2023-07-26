from flask import Flask , jsonify,Blueprint

apiProducts =Blueprint('apiProducts',__name__,url_prefix='/api/products')


@apiProducts.route('/')
def products_func():
    return jsonify({"success":True,"messages":"products"})