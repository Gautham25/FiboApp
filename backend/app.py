from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from sqlalchemy import create_engine, text, insert
import psycopg2 
import psycopg2.extras as extras
import os
import pandas as pd

app = Flask(__name__)
CORS(app, support_credentials=True, resources={r"/*": {"origins": "*"}})
app.config["DEBUG"] = True

dbconn = {  
    'host':os.getenv('db_host'),
    'database': os.getenv("db"),
    'user': os.getenv("db_user"),
    'port': os.getenv("db_port"),
    'password': os.getenv("db_pass")
}

engine = create_engine(f'postgresql+psycopg2://{dbconn["user"]}:{dbconn["password"]}@{dbconn["host"]}:{dbconn["port"]}/{dbconn["database"]}')
@app.route('/')
def home():
    """
    Test API to check if backend is functional
    """
    return "Hello World"