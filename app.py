from lib.apiget import APIAccess
from lib.sql import SqlServer
from flask import Flask, jsonify, abort, Response, request
from datetime import datetime
import json

import configparser

config = configparser.ConfigParser()
config.read('api.conf')


app = Flask(__name__)

remote_api = APIAccess(str(config['tables']['cache_table']), str(config['db']['database']), str(config['db']['user']), str(config['db']['password']), str(config['db']['host']))
db = SqlServer(str(config['db']['host']), str(config['db']['user']), str(config['db']['password']), str(config['db']['database']))

aol_url = config['external']['aol_api_query_url']

poi_table = config['tables']['poi_table']
animal_table = config['tables']['animal_table']

@app.route('/api/aol', methods=['GET'])
def aol_search():
    query = request.args.get('query')
    print("Query: ", query)
    if query:
        json = remote_api.get(query, aol_url)
        return jsonify(json)
    else:
        abort(Response(jsonify({"error":"Invalid Query String", "code":1})))

@app.route('/api/animals/profiledata', methods=['GET'])
def aol_get_profile():
    query = request.args.get('animal')
    print("Profile data for animal: ", query)
    if query:
        json = remote_api.get(query, aol_url)
        print(json[1])
        return jsonify(json)
        #return jsonify({"success":True})
    else:
        abort(Response(jsonify({"error":"Invalid Query String", "code":1})))

@app.route('/api/animals/save', methods=['GET'])
def save_animal_data():
    animal_type = request.args.get('type')
    lat = float(request.args.get('lat'))  
    lon = float(request.args.get('lon'))  
    time = datetime.now()
    if animal_type:
        print("Animal {} at {},{} {}".format(animal_type, lat, lon, time))
        db.insert(animal_table, ['time', 'lat', 'lon', 'animal_type'], [time, lat  , lon  , animal_type])
        return jsonify({"success":True})
    else:
        return jsonify({"success":False})

@app.route('/api/animals/get_all', methods=['GET'])
def get_all_animals():
    json_dict = []
    json_string = ""
    animal_sightings = db.get_all(animal_table)
    for row in animal_sightings:
        id, timedate, lat, lon, animal_type = row
        json_dict.append('{"id":%s,"animal_type":%s, "lat":%s, "lon":%s, "time":%s}'% (id, animal_type, lat, lon, timedate))
    record_number = len(json_dict)
    json_string = json_string + '['
    for entry in json_dict:
        json_string = json_string + entry
        json_string = json_string + ','
    json_string = json_string.strip(',')
    json_string = json_string + ']'

    return json_string

@app.route('/api/poi/save', methods=['GET'])
def save_poi():
    poi_type = request.args.get('type') 
    poi_name = request.args.get('name') 
    lat = float(request.args.get('lat'))  
    lon = float(request.args.get('lon'))  
    time = datetime.now()
    if poi_type:
        print("POI {} ({}) at {},{} {}".format(poi_name, poi_type, lat, lon, time))
        db.insert(poi_table, ['poi_type', 'poi_name', 'lat', 'lon', 'time'], [poi_type, poi_name, lat  , lon  , time])
        return jsonify({"success":True})
    else:
        return jsonify({"success":False})
    
@app.route('/api/poi/get_all', methods=['GET'])
def get_all_pois():
    json_dict = []
    json_string = ""
    pois = db.get_all(poi_table)
    for row in pois:
        id, code_type, name, lat, lon, timedate = row
        json_dict.append('{"id":%s, "type":"%s", "name":"%s", "lat":%s, "lon":%s, "time":"%s"}' % (id, code_type, name, lat, lon, timedate))
    record_number = len(json_dict)
    json_string = json_string + '['
    for entry in json_dict:
        json_string = json_string + entry
        json_string = json_string + ','
    json_string = json_string.strip(',')
    json_string = json_string + ']'
    return json_string


@app.route('/api/poi/search/by_lat', methods=['GET'])
def find_poi_by_lat():
    lat = request.args.get('lat')
    json_dict = []
    json_string = ""
    results = db.search_int(poi_table, 'lat', lat)
    print(results)
    for row in results:
        id, type_code, name, lat, lon, time = row
        json_dict.append('{"id":%s, "type":"%s", "name":"%s", "lat":%s, "lon":%s, "time":"%s"}'% (id, type_code, name, lat, lon, time))

    record_number = len(json_dict)
    json_string = json_string + '['
    for entry in json_dict:
        json_string = json_string + entry
        json_string = json_string + ','
    json_string = json_string.strip(',')
    json_string = json_string + ']'

    return json_string
    
@app.route('/api/poi/search/by_lon', methods=['GET'])
def find_poi_by_lon():
    lon = request.args.get('lon')
    json_dict = []
    json_string = ""
    results = db.search_int(poi_table, 'lon',  lon)
    print(results)
    for row in results:
        id, type_code, name, lon, lon, time = row
        json_dict.append('{"id":%s, "type":%s, "name":%s, "lat":%s, "lon":%s, "time":%s}'% (id, type_code, name, lat, lon, time))

    record_number = len(json_dict)
    json_string = json_string + '['
    for entry in json_dict:
        json_string = json_string + entry
        json_string = json_string + ','
    json_string = json_string.strip(',')
    json_string = json_string + ']'

    return json_string

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

