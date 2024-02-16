from fastapi import FastAPI

from api.routers import stats_router, product_router
from db.database import Base, engine

Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(product_router.product_routes, prefix="/products")
app.include_router(stats_router.stats_routes, prefix="/stats")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
