from flask import Flask
from flask import jsonify



app=Flask(__name__)


@app.route("/")
def home():
    return "This is home screen !!"
@app.route("/about")
def about():
    return "This is About screen !!"
@app.route("/users")
def user():
    userList = [
        {   
            "status":True,
            "name": "Khan",
            "age": 21
        },
        {
            "name": "Asad",
            "age": 22
        },
        {
            "name": "Zan",
            "age": 22
        },
        {
            "name": "Saim",
            "age": 21
        },
    ]

    # return jsonify(userList)
    return jsonify(userList)
    # return "This is user screen !!"




if __name__=="__main__":
    app.run(port=200)    
    