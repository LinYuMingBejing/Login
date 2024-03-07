from flask import jsonify
from app.api import api
from app.utils.token import verify_authorization
from utils.status import SUCCESS


@api.route('/about/me')
@verify_authorization()
def aboutMe():
    return jsonify(message=SUCCESS.message, code=200)
