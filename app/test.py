from app import app
from flask_cors import CORS
from flask import jsonify, json, g, request
CORS(app)
import psycopg2
conn = psycopg2.connect(user='cooper', host='localhost', dbname='pet_hotel')
cur = conn.cursor()

@app.route('/hello')
def hello():
    return 'Hello World! Booooo!'
@app.route('/spooky')
def spooky():
    return 'Skeletons'

@app.route('/pets')
def pets():
    cur.execute("SELECT * FROM pets")
    pets = cur.fetchall()
    print(pets)
    return jsonify(pets)

@app.route('/pets/<id>', methods=['DELETE'])
def petsdelete(id):
    cur.execute(f"DELETE FROM pets WHERE id=?")
    conn.commit()
    cur.execute("SELECT * FROM pets")
    pets = cur.fetchall()
    print(pets)
    return jsonify(pets)

@app.route('/owners')
def owners():
    cur.execute("SELECT * FROM owners")
    pets = cur.fetchall()
    print(pets)
    return jsonify(pets)

@app.route('/addOwners', methods=['POST'])
def addOwners():
    cur.execute("INSERT INTO owners (first_name, last_name) VALUES (%s, %s)", ('Jane', 'Doe'))
    conn.commit()
    cur.execute("SELECT * FROM owners")
    owners = cur.fetchall()
    return jsonify(owners)

@app.route('/add', methods=['POST'])
def addPets(owner_id, name, breed, color, is_checked_in):
    # content = request.json
    # cur.execute(f"INSERT INTO pets (owner_id, name, breed, color, is_checked_in) VALUES ({owner_id}, {name}, {breed}, {color}, {is_checked_in}');")
    # cur.execute(sql, (content["owner_id"], content["name"], content["breed"], content["color"], content["is_checked_in"]))
    conn.commit()
    cur.execute("SELECT * FROM pets")
    pets = cur.fetchall()
    return jsonify(pets)
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000/')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response