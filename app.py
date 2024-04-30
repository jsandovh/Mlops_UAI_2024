from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd
from ChatBOT_MLOps import generate_a

apli = FastAPI()

@apli.get("/")
async def root():
    return {"message": "Hola Chatbox"}

@apli.get("/consulta")
async def consulta(texto:str):
    return generate_a(texto)

if __name__ == "__main__":
    uvicorn.run(apli, port=8080, host="0.0.0.0")


