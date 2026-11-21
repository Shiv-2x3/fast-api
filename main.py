from fastapi import FastAPI

app = FastAPI() #app --> Fast api object

@app.get("/") # This is a route --> With  a get request to process user request
def hello():
    return {'message': "Hello World"}

@app.get("/bio")
def bio():
    return {'message' : "This is me.. yes me!!"}

@app.get("/topic")
def topic():
    return {'topic-1' : 'ML',
            'topic-2' : 'DS',
            'topic3' : 'linux'}