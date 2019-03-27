import populartimes
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from common import notify_error, log_api_call
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
api = Api(app)

HTTP_ERROR_CLIENT = 403
HTTP_ERROR_SERVER = 500

@app.route('/populartimes/place/<place_id>')
def getPopularTimes(place_id):
    if 'apiKey' not in request.args or request.args['apiKey'] in ("", None):
        return notify_error("ERR_NO_ARG:  'apiKey' argument required to /populartimes/ API", HTTP_ERROR_CLIENT)

    api_key = request.args.get('apiKey')
    try:
        return jsonify(populartimes.get_id(api_key, place_id))
    except Exception as ex:
        return notify_error(ex, HTTP_ERROR_SERVER)


@app.route('/populartimes/search')
def getPopularPlaces():
    n_threads = 10
    radius =  3000
    all_places = False

    if 'apiKey' not in request.args or request.args['apiKey'] in ("", None):
        return notify_error("ERR_NO_ARG:  'apiKey' argument required to /populartimes/ API", HTTP_ERROR_CLIENT)
    api_key = request.args.get('apiKey')

    if 'types' not in request.args or request.args['types'] in ("", None):
        return notify_error("ERR_NO_ARG:  'types' argument required to /populartimes/ API", HTTP_ERROR_CLIENT)
    types = request.args.get('types').split(',')

    if 'p1' not in request.args or request.args['p1'] in ("", None):
        return notify_error("ERR_NO_ARG:  'p1' argument required to /populartimes/ API", HTTP_ERROR_CLIENT)
    print(request.args.get('p1'))
    p1_list = request.args.get('p1').split(',')
    p1 = (float(p1_list[0]), float(p1_list[1]))

    if 'p2' not in request.args or request.args['p2'] in ("", None):
        return notify_error("ERR_NO_ARG:  'p2' argument required to /populartimes/ API", HTTP_ERROR_CLIENT)
    p2_list = request.args.get('p2').split(',')
    p2 = (float(p2_list[0]), float(p2_list[1]))

    try:
        return jsonify(populartimes.get(api_key, types, p1, p2, n_threads, radius, all_places))
    except Exception as ex:
        return notify_error(ex, HTTP_ERROR_SERVER)


if __name__ == '__main__':
     app.run(port='5001')
