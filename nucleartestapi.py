# coding: utf8
#!/usr/bin/python3

# Author: Nicolas Flandrois
# Date: Fri 22 May 2020 17:17:40 CEST

# Description: Training Exercise, creating a simple RESTful API using Flask,
# backedup with MongoDB, using GET & POST methods.

# This API uses the official list of nuclear tests given by wikipedia
# https://en.wikipedia.org/wiki/List_of_nuclear_weapons_tests#Known_tests
# Are not taken into account the Allged tests.
# Import the json file in this repository in MongoDB, nucleartest.json

# MongoDB Sample from database 'mongo_rest':
# > db.nucleartest.find().pretty()
# {
#     "_id" : ObjectId("xxxxxxxxxxxxxxxxxxxxxxx1"),
#     "country" : "USA",
#     "year" : "1945",
#     "where" : "New Mexico",
#     "location" : "Socorro",
#     "name" : "Trinity",
#     "max_yield" : "20 kt"
# }
# {
#     "_id" : ObjectId("xxxxxxxxxxxxxxxxxxxxxxx2"),
#     "country" : "USA",
#     "year" : "1946",
#     "where" : "Marshall Island",
#     "location" : "Bikini Atoll",
#     "name" : "Operation Crossroads",
#     "max_yield" : "NaN"
# }
# {
#     "_id" : ObjectId("xxxxxxxxxxxxxxxxxxxxxxx3"),
#     "country" : "USA",
#     "year" : "1951",
#     "where" : "Marshall Island",
#     "location" : "Enewetak Atoll",
#     "name" : "Operation Greenhouse",
#     "max_yield" : "NaN"
# }


from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongo_rest'
# app.config['MONGO_URI'] = 'mongodb://username:password@hostname:port/databasename'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mongo_rest'

mongo = PyMongo(app)


@app.route('/nucleartest', methods=['GET'])
def get_all_nucleartests():
    nucleartest = mongo.db.nucleartest

    output = []

    for q in nucleartest.find():
        output.append({'name': q['name'], 'country': q['country'],
                       'year': q['year'], 'where': q['where'],
                       'location': q['location'], 'max_yield': q['max_yield']})

    return jsonify({'result': output})


@app.route('/nucleartest/<name>', methods=['GET'])
def get_one_nucleartest(name):
    nucleartest = mongo.db.nucleartest

    q = nucleartest.find_one({'name': name.title()})

    if q:
        output = {'name': q['name'], 'country': q['country'],
                  'year': q['year'], 'where': q['where'],
                  'location': q['location'], 'max_yield': q['max_yield']}
    else:
        output = 'No Results Found'

    return jsonify({'result': output})


@app.route('/nucleartest/country/<country>', methods=['GET'])
def get_all_nucleartests_for_one_country(country):
    nucleartest = mongo.db.nucleartest

    query = nucleartest.find({'country': country})

    if query:
        output = [{'name': q['name'], 'country': q['country'],
                   'year': q['year'], 'where': q['where'],
                   'location': q['location'], 'max_yield': q['max_yield']}
                  for q in query]
    else:
        output = 'No Results Found'

    return jsonify({'result': output})


@app.route('/nucleartest/year/<year>', methods=['GET'])
def get_all_nucleartests_by_year(year):
    nucleartest = mongo.db.nucleartest

    query = nucleartest.find({'year': year})

    if query:
        output = [{'name': q['name'], 'country': q['country'],
                   'year': q['year'], 'where': q['where'],
                   'location': q['location'], 'max_yield': q['max_yield']}
                  for q in query]
    else:
        output = 'No Results Found'

    return jsonify({'result': output})

@app.route('/nucleartest', methods=['POST'])
def add_nucleartest():
    nucleartest = mongo.db.nucleartest

    name = request.json['name']
    country = resquest.json['country']
    year = resquest.json['year']
    where = resquest.json['where']
    location = resquest.json['location']
    max_yield = resquest.json['max_yield']

    nucleartest_id = nucleartest.insert(
        [{'name': name, 'country': country,
          'year': year, 'where': where,
          'location': location, 'max_yield': max_yield}])

    new_nucleartest = nucleartest.find_one({'_id': nucleartest_id})

    output = {'name': new_nucleartest['name'], 'country': new_nucleartest['country'],
              'year': new_nucleartest['year'], 'where': new_nucleartest['where'],
              'location': new_nucleartest['location'],
              'max_yield': new_nucleartest['max_yield']}

    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
