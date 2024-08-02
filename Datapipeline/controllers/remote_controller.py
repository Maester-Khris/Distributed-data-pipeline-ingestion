from json import dumps 
import requests
from flask import Blueprint, jsonify, request, make_response

remote_bp = Blueprint('remote', __name__)

@remote_bp.route('/', methods=['GET'])
def send_request():
    headers = {'Client-Identifier': 'dan-citymonitor'}
    response = requests.get('https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json', headers=headers)
    r = response.json()
    print("response acquired")
    return make_response("request to remote api successfuly made and response available")