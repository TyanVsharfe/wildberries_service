from fastapi import APIRouter

from wb_web_service.api.service import product_service
from wb_web_service.api.utils.utils import get_product_model

product_routes = APIRouter()


@product_routes.get("/all",
                    description="Get all products from the database")
def get_products():
    return product_service.get_products()


@product_routes.get("/{product_id}",
                    description="Get product from the database by product id.")
def get_product(product_id: int):
    return product_service.get_product(product_id)


@product_routes.get("/{product_id}/history",
                    description="Get product history from from wildberries.com.")
def get_product_history(product_id: int):
    return product_service.get_history(product_id)


@product_routes.post("/{product_id}",
                     description="Add a product from wildberries.com")
def add_product(product_id: int):
    product_model = get_product_model(product_id)
    product_service.create_product(product_model)
    return product_model.name


@product_routes.put("/{product_id}", description="Update product from the database by product id.")
def update_product(product_id: int):
    product_model = get_product_model(product_id)
    product_service.update_product(product_model)
    return product_model.name


@product_routes.delete("/{product_id}",
                       description="Delete product from the database by product id.")
def delete_product(product_id: int):
    product_service.delete_product(product_id)
