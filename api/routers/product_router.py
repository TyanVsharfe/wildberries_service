from fastapi import APIRouter

product_routes = APIRouter()


@product_routes.get("/products")
def get_products():
    pass


@product_routes.get("/product/{product_id}")
def get_product(product_id: int):
    pass


@product_routes.get("/product/{product_id}")
def add_product(product_id: int):
    pass


@product_routes.delete("/product/{product_id}")
def delete_product(product_id: int):
    pass
