import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Denis'  # Not gonna be showing to others
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()



# JWT creates new end point /auth when auth called we send username and password after than the user found /auth endpoint sends back JWT token
jwt = JWT(app, authenticate, identity)
                                       # and then we send the token with every API call and the server calls the identity func



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

db.init_app(app)
if __name__ == "__main__":
    app.run(port=5000)

