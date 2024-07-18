from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from dataBase.dataBase import metaData, engineBD


chat = Table("chatBot", metaData,
             Column("id", Integer, primary_key=True),
             Column("pregunta", String(255)),
             Column("respuesta", String(255)),
             ) 

metaData.create_all(engineBD)