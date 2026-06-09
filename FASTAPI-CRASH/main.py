from fastapi import FastAPI #core framework
from pydantic import BaseModel #data validation and settings management
from typing import List #type hinting for lists


app = FastAPI() #create FastAPI instance

class Tea(BaseModel): #define a Pydantic model for Tea
    id:int
    name: str
    origin: str #chai kaha se ayi hai assam se ya darjeeling se
   
teas: List[Tea] = []#in-memory list to store tea data
## above we have initalized the data structure to store tea information, it is an empty list that will hold instances of the Tea model. 
#fastapi as a whole simply works on one concepts named decorators, which provide super powers to the functions, in this case we are using @app.post and @app.get decorators to define our API endpoints.
@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API!"} #root endpoint that returns a welcome message


@app.get("/teas") #decorator to define a GET endpoint at /teas
def get_teas():
    return teas #endpoint to get the list of all teas

@app.post("/teas") #decorator to define a POST endpoint at /teas
def add_tea(tea: Tea):
    teas.append(tea)
    return tea 

@app.put("/teas/{tea_id}") #decorator to define a PUT endpoint for updating tea information
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"} #endpoint to update tea information based on tea_id


app.delete("/teas/{tea_id}") #decorator to define a DELETE endpoint for deleting tea information
def delete_tea(tea_id: int):    
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea
    return {"error": "Tea not found"} #endpoint to delete tea information based on tea_id