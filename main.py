from fastapi import FastAPI

from classes.JsonAnswer import JsonAnswer
from classes.UserRequest import UserRequest
from moduleMakeCircuit.checkAnswer import checkAnswer
from moduleMakeCircuit.generateFullAnswer import generatedRLCShem
from moduleMakeCircuit.getFullParameterForGenerateCircuit import getParameterForSimulate


#from moduleMakeCircuit.generateFullAnswer import generatedRLCShem

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
#
# @app.post("/getTask")
# async def get_task():
#
#     return "result"

@app.post("/getTask")
async def get_task(request: UserRequest):
    result = generatedRLCShem(request)
    return result


@app.post("/checkAnswer")
async def get_task(request: JsonAnswer):
    checkAnswer(request)
    return checkAnswer(request)