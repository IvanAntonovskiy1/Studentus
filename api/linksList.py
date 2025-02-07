from fastapi import FastAPI

from classes.UserRequest import UserRequest

#
# from classes.UserRequest import UserRequest
# from moduleMakeCircuit.generateFullAnswer import generatedRLCShem
app = FastAPI()





@app.post("/getTask")
async def get_task(request: UserRequest):
    # Передаем данные в функцию генерации
    #result = generatedRLCShem(request)

     # Можно добавить дополнительную обработку
     # /result["status"] = "success"

    return request

@app.post("/get")
async def get(request: UserRequest):
    # Передаем данные в функцию генерации
    #result = generatedRLCShem(request)

     # Можно добавить дополнительную обработку
     # /result["status"] = "success"

    return request

