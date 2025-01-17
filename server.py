from fastapi import FastAPI
import pymysql
from database import config

app=FastAPI()

def search_product(value):
    connection = pymysql.connect(**config)
    cursor = connection.cursor()

    # Update the product's information in the database
    query = f'SELECT * FROM business_owner WHERE cnic= %s'
    cursor.execute(query,value)
    data = cursor.fetchall()
    return data

@app.get("/")
async def route():
    return{
        "Hello World": "Python Program"
    }

@app.get("/search/{value}")
async def route(value:str):
    result = search_product(value)
    return{
        "Result": result
    }
