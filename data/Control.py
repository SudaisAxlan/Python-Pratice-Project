from flask import Flask
# from data.user import users
# from data.products import product
from flask import jsonify
from data.alldata import AllUser,product

def home():
    return "This is home screen !!"
def about():
    return "This is About screen !!"
def singUp():
    return "This is SingUp screen !!"
def users():
    userResponce={
        "status" :True,
        "message" :"All Users Here",
        "user" : AllUser
        
    }
    return jsonify(userResponce)
        
    # return jsonify(users)
def Products():
 response = {
        "status": True,
        "message": "All products are here",
        "products": product
    }
 return jsonify(response)    
    # return jsonify(product)


