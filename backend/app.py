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

@app.route('/fiboValue', methods=['GET'])
def generate_fibo_value():
    """
    API to get the first N numbers in the Fibonacci series
    """
    args = request.args
    num = int(args.get('num')) if 'num' in args else None
    if num == None:
        return {'data':'No Value Provided'}

    fibo = get_values(num)
    return fibo

def get_values(num):
    """
    Function to check if the Nth Fibonacci number is present in the DB and return the series
    If the Nth Fibonacci number is not present then we find the number closest to N and start calculating
    the next numbers in the series and store it in the DB
    """
    with engine.connect() as conn:
        query = text(f'SELECT * FROM fibonacci.fibo_values WHERE number_id <= {num} ORDER BY number_id ASC')
        sql_query = conn.execute(query)
        df = pd.DataFrame(sql_query, columns=['numberId', 'value'])
        result = [i for i in df['value']]
        if (len(df)-1) != num:
            df2 = df.tail(2)
            last_nums, last_vals = list(df2.loc[:,'numberId']), list(df2.loc[:,'value'])
            fibo_pairs = [[last_nums[0], last_vals[0]], [last_nums[1], last_vals[1]]]
            for i in range(last_nums[-1]+1, num+1):
                next_val = fibo_pairs[-1][1]+fibo_pairs[-2][1]
                fibo_pairs.append([i, next_val])
                result.append(next_val)
            fibo_pairs = fibo_pairs[2:]
            df3 = pd.DataFrame(fibo_pairs, columns=df.columns)
            insert_values(df3, "fibonacci.fibo_values")    
            df = pd.concat([df,df3], ignore_index=True)
        result = result[1:]
        return {'data': result}

def insert_values(df, table):
    """
    Function that converts the N Fibonacci numbers to be stored in the database 
    """
    tuples = [tuple(x) for x in df.to_numpy()]
    with engine.connect() as conn:
        for t in tuples:
            statement = text(f'INSERT INTO fibonacci.fibo_values(number_id, fibon_value) VALUES({t[0]}, {t[1]})')
            conn.execute(statement)
        conn.commit()

if __name__ == '__main__':
    app.run()