"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User,Plants
from api.utils import generate_sitemap, APIException

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route("/signup", methods=["POST"])
def signup():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
   
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return "The user already exists", 400

    new_user = User(email=email, password=password)
    
    db.session.add(new_user)    
    db.session.commit()

    response_body = "You have created an user"
    return jsonify(response_body), 200

@api.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
   
    existing_user = User.query.filter_by(email=email).first()

    if existing_user.password != password or existing_user.email != email:
        response_body = "Invalidad credentials"
        return jsonify(response_body), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200


@api.route("/add/plant", methods=["POST"])
def add_plants():
    name = request.json.get("name", None)
    size34 = request.json.get("size34", None)
    size35 = request.json.get("size35", None)
    size36 = request.json.get("size36", None)
    size37 = request.json.get("size37", None)
    size38 = request.json.get("size38", None)
    size39 = request.json.get("size39", None)
    size40 = request.json.get("size40", None)
    print(name,size34)
   
    existing_plant = Plants.query.filter_by(name=name).first()

    if existing_plant:
        return "The plant already registered", 400

    new_plant = Plants(name=name, size34=size34,size35=size35, size36=size36, size37=size37, size38=size38, size39=size39, size40=size40, size41=0)
    
    db.session.add(new_plant)    
    db.session.commit()

    response_body = "You have registered a plant"
    return jsonify(response_body), 200

@api.route("/get/plants", methods=["GET"])
def get_plants():
    plants = Plants.query.all()
    plants_list = [plant.serialize() for plant in plants]
    return jsonify(plants_list), 200