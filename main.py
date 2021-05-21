from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from routes.connexion import connexion1,connexion2

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(connexion1,"/connexion1") 
api.add_resource(connexion2,"/connexion2") 


if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')
