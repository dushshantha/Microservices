import populartimes
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

def getPopularTimes(api_key, place_id):
    return jsonify(populartimes.get_id(api_key, place_id))

def getPopularPlaces(api_key, types, p1, p2, n_threads, n_threads = 10, radius =  3000, all_places = False):
    return jsonify(populartimes.get(api_key, types, p1, p2, n_threads, n_threads, radius, all_places))
