from fastapi import FastAPI ,Path , HTTPException , Query
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

@app.get('/paitent/{id}')
def view_paitent(id : str = Path(... , description="Paitent ID in Database" , example="P001")):
    #loads all the data
    data = Load_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code=404 , detail="User not found")


@app.get('/sort')
def sort_paitents(sort_by :str = Query(... , description="Sort on the basis of height , weight , BMI" ), order : str = Query('asc' , description="sort in asecending or desending order")):
    valid_feils = ['height' , 'weight' , 'bmi']

    if sort_by not in valid_feils:
        raise HTTPException(status_code=400 , detail=f"invalid feild , select from {valid_feils}")
    if order not in ['asc' , 'dsc']:
        raise HTTPException(status_code=400 ,detail="invalid order select between asc or desc")
    
    data = Load_data()

    sort_order = True if order == 'desc' else  False

    sorted_data = sorted(data.values() , key = lambda x: x.get('height' , 0) , reverse = sort_order)


    return sorted_data
