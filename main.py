from fastapi import FastAPI
from model import model, vuelta
app =FastAPI()

@app.post('/prueba')
def prueba(texto:model):
    contenido=vuelta(texto.tipo)
    return[
           'frase':contenido         
    ]