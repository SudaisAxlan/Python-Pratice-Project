from flask import Flask
from flask import jsonify
# from data.products import product
from data.Routes.AllRoutes import routes

app=Flask(__name__)
# 
# app.register_blueprint(routes)
app.register_blueprint(routes,url_prefix="/api/v1")


if __name__=="__main__":
    app.run()    
