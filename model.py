from api import API
from pydantic import BaseModel
class model(BaseModel):
        tipo : str

def vuelta(frase1):
        contenido=API.reversa(
                frase=frase1
        )
        return contenido