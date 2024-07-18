from fastapi import APIRouter, HTTPException
from sqlalchemy import select 

from models.chatBot import chat
from dataBase.dataBase import conetion 

routes = APIRouter()

@routes.get("/markbot")
def consultarChat():
    try:
        consulta = select(chat)
        res = conetion.execute(consulta).fetchall()
        resJSON = [{'id': row.id,'pregunta':row.pregunta,'respuesta':row.respuesta} for row in res]
        return resJSON

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))