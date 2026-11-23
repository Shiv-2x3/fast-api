from fastapi import FastAPI
import json

app = FastAPI() #app --> Fast api object

def Load_data():
    with open('paitents.json' , 'r') as file:
        data = json.load(file)
    return data

@app.get('/')
def home():
    return {'message' : 'Paitent managment system API'}

@app.get('/about')
def about():
    return {'description' : 'A working API for sysem management'}

@app.get("/view")
def view():
    collection = Load_data()
    return collection