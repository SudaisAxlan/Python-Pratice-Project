from flask import Flask
from data.Control import home,about,users,Products,singUp

from flask import Blueprint


# Routes=Blueprint("routes",__name__)
routes = Blueprint('routes', __name__)

routes.add_url_rule("/",view_func=home)
routes.add_url_rule("/about",view_func=about)
routes.add_url_rule("/users",view_func=users)
routes.add_url_rule("/products",view_func=Products)
routes.add_url_rule("/singUp",view_func=singUp,methods=[ 'POST'])
# @app.route("")
