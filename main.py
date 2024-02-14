from fastapi import FastAPI

from api.routers.product_router import product_routes
from db.database import Base, engine

Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(product_routes)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
