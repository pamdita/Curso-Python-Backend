from fastapi import FastAPI
from super_db import usuarios, items

app = FastAPI()

@app.get("/")
def get_base():
    return("Mensaje": "Hola Mundo")

@app.get("/usuario/{id}")
def get_usuario(id: int)
    
