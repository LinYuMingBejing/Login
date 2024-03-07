from flask import request, jsonify
from marshmallow import ValidationError

from app.api import api
from models import User
from schema import UserSchema
from utils.token import generate_jwt_token
from utils.response import success, error
from utils.status import CONFLICT, CREATE_SUCCESS, PARAMETER_ERROR, \
    USER_NOT_FOUND, PASSWORD_ERROR, LOGIN_SUCEESS


@api.route('/user', methods=['POST'])
def createAccount():
    data = request.json
    
    try:
        UserSchema().load(data)
    except ValidationError as err:
        return jsonify(error(err.messages)), PARAMETER_ERROR.code
    
    if User.is_exist(data['username']):
        return jsonify(error(CONFLICT.message)), CONFLICT.code
    
    User(
        username = data['username'],
        password = data['password']
    ).save()

    return jsonify(success(CREATE_SUCCESS.message)), CREATE_SUCCESS.code


@api.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(username=data['username']).first()

    if not user:
        return jsonify(error(USER_NOT_FOUND.message)), USER_NOT_FOUND.code
    
    if not user.verify_password(data['password']):
        return jsonify(error(PASSWORD_ERROR.message)), PASSWORD_ERROR.code

    response = success(LOGIN_SUCEESS.message, payload={'token': generate_jwt_token(user)})
    return jsonify(response), LOGIN_SUCEESS.code
