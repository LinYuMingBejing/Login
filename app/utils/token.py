from datetime import datetime, timedelta
from flask import request, jsonify
from functools import wraps
import jwt

from models import User
from settings.defaults import SECRET_KEY
from utils.response import error
from utils.status import FORBIDDEN, UNAUTHORIZED


def generate_jwt_token(user: User) -> str:
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }

    pyload = {
        'id': user.id,
        'username': user.username,
        'exp': datetime.now() + timedelta(minutes=30)
    }

    token = jwt.encode(headers=headers, payload=pyload, key=SECRET_KEY, algorithm='HS256')

    return token


def verify_authorization():
    def decorator(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            token = request.headers.get('Authorization', None)

            if not token or not token.startswith('Bearer '):
                return jsonify(error(FORBIDDEN.message)), FORBIDDEN.code
            
            try:
                payload = jwt.decode(token[7:], SECRET_KEY, algorithms=['HS256'])
                if 'username' not in payload:
                    return jsonify(error(UNAUTHORIZED.message)), UNAUTHORIZED.code
                return func(*args, **kwargs)
            except Exception:
                return jsonify(error(UNAUTHORIZED.message)), UNAUTHORIZED.code
            
        return wrapped_func
    return decorator