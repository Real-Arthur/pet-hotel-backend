from app import app
import psycopg2
conn = psycopg2.connect(user='rthrcrsn', host='localhost', dbname='pet_hotel')
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
        return pet