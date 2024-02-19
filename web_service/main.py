import uvicorn
from fastapi import FastAPI

from web_service.api.routers import product_router, stats_router
from web_service.db.database import Base, engine

Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(product_router.product_routes, prefix="/api/products")
app.include_router(stats_router.stats_routes, prefix="/api/stats")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


