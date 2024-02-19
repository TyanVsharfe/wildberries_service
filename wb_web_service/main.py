import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from wb_web_service.api.routers import product_router, stats_router
from wb_web_service.config import settings
from wb_web_service.db.database import Base, engine

Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(product_router.product_routes, prefix="/api/products")
app.include_router(stats_router.stats_routes, prefix="/api/stats")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


