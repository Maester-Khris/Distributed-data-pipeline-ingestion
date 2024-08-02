from flask import Blueprint, render_template, make_response

message_bp = Blueprint('message', __name__)

@message_bp.route('/')
def index():
    return make_response('Welcome to our alert message Api'), 200

@message_bp.route('/about')
def about():
    return make_response('We are well aware of all the challenges and trial you are facing'), 200