from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

from sqlalchemy import select 

from sqlalchemy.sql import func

from models.chatBot import chat
from dataBase.dataBase import conetion 

class ChatRequest(BaseModel):
    pregunta: str

routes = APIRouter()

@routes.post("/markbot")
def consultarChat(request: ChatRequest):
    try:
        normalizada_pregunta = request.pregunta.strip().lower()
        consulta = select(chat).where(func.lower(func.trim(chat.c.pregunta)) == normalizada_pregunta)
        res = conetion.execute(consulta).fetchone()
        if res:
            return {"respuesta": res.respuesta}
        else:
            respuesta_default = (
                "Lo siento, no tengo una respuesta para esa pregunta, pero tienes estos enlaces que te pueden ayudar a resolver tus inquietudes:<br>"
                "- <a href='https://www.segurossura.com.co/paginas/movilidad/autos/centros-de-servicio/inicio.aspx' target='_blank' rel='noopener noreferrer'>Centro de Servicios Autos SURA</a><br>"
                "- <a href='https://www.epssura.com/' target='_blank' rel='noopener noreferrer'>EPS SURA</a><br>"
                "- <a href='https://www.segurossura.com.co/paginas/inicio.aspx' target='_blank' rel='noopener noreferrer'>Seguros SURA</a>"
            )
            return {"respuesta": respuesta_default}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@routes.get("/markbot")
def consultarChat():
    try:
        consulta = select(chat)
        res = conetion.execute(consulta).fetchall()
        resJSON = [{'id': row.id,'pregunta':row.pregunta,'respuesta':row.respuesta} for row in res]
        return resJSON

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
    

    

    