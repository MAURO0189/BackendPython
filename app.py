from fastapi import FastAPI

from routes.routesAPI import routes

app = FastAPI()

app.include_router(routes)