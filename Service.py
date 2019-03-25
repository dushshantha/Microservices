from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Employee(Resource):
    def get(self):
        employees = [{'Name': 'Marcus S',
                      'Age' : 38},
                     {'Name': 'Marcus S1',
                      'Age' : 38}]
        return jsonify(employees)

@app.route('/test', methods=['GET'])
def testMethod():
    return jsonify({'test': 'Its working'})


api.add_resource(Employee, '/employees')

if __name__ == '__main__':
     app.run(port='5002')
