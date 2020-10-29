from app import app
from flask_cors import CORS
from flask import jsonify, json, g, request
CORS(app)
import psycopg2
conn = psycopg2.connect(user='rthrcrsn', host='localhost', dbname='pet_hotel')
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
    cur.execute(f"DELETE FROM pets WHERE id={id}")
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

@app.route('/add', methods=['POST'])
def addPets():
    cur.execute("INSERT INTO pets (owner_id, name, breed, color, is_checked_in) VALUES (%s, %s, %s, %s, %s)", (1, 'Charlie', 'Shih-tzu', 'Black', True))
    conn.commit()
    cur.execute("SELECT * FROM pets")
    pets = cur.fetchall()
    return jsonify(pets)
