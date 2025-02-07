from fastapi import FastAPI

from classes.UserRequest import UserRequest
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
    # Передаем данные в функцию генерации
    result = generatedRLCShem(request)

     # Можно добавить дополнительную обработку
     # /result["status"] = "success"

    return result


# def getParameterForSimulate(JSON):
#     return UserRequest.model_dump(JSON)