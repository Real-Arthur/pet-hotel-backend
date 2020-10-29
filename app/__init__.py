import psycopg2
from flask import Flask, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import test