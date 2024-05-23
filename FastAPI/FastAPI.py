from fastapi import FastAPI
from enum import Enum
# to run it go to cmd , change directory and write { uvicorn {filename}:{APIname} --reload
# --reload is like live server

app = FastAPI()

@app.get('/hello/{name}')
async def hello(name):
    return f"welcome to fastapi tutorial {name}"

# @app.get()   # get is to read data ex:[ Show me iPhone Covers ]
# @app.post()  # create data  ex : [ create new order ]
# @app.put()   # update data ex : [ update an order ]
# @app.delete()  # delete an order

# 127.0.0.1:8000/docs # displays all methods and turns and schemas ( databases )
# 127.0.0.1:8000/Redoc # also generate a document like above

class AvailableCuisines(str,Enum): # inbuilt Validation
    indian = 'indian'
    american = 'american'
    italian = 'italian'

food_items = {
    'indian' : ['Samosa','Dosa'],
    'american' : ['Hot Dog','Apple pie'],
    'italian' : ['Spagetti','Pizza' ]
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines): # cuisine must be one of the AvailableCuisines , otherwise error
    return food_items.get(cuisine)


coupon_codes = {
    1 : '10%',
    2 : '20%',
    3 : '30%'
}

@app.get('/get_coupon/{code}')
async def get_items(code: int):
    return { 'discount_amount ': coupon_codes.get(code,'Invalid Code') }