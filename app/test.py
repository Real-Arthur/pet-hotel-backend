from app import app
from flask_cors import CORS
from flask import jsonify
CORS(app)
import psycopg2
conn = psycopg2.connect(user='rthrcrsn', host='localhost',  port=5432, dbname='pet_hotel')
cur = conn.cursor()

@app.route('/hello')
def hello():
    return 'Hello World! Booooo!'
@app.route('/spooky')
def spooky():
    return 'Skeletons'

@app.route('/homepage')
def customers():
    cur.execute("SELECT * FROM pets")
    pets = cur.fetchall()
    print(pets)
    for pet in pets:
        return jsonify(pet)