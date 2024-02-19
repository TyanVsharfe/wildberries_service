from fastapi import APIRouter
import requests

from api.models.Product import ProductModel
from api.service import product_service
from api.utils import utils
from api.utils.utils import get_basket_id, get_product_category

product_routes = APIRouter()


@product_routes.get("/all")
def get_products():
    return product_service.get_products()


@product_routes.get("/{product_id}")
def get_product(product_id: int):
    return product_service.get_product(product_id)


@product_routes.get("/{product_id}/history")
def get_product_history(product_id: int):
    return product_service.get_history(product_id)


@product_routes.post("/{product_id}")
def add_product(product_id: int):
    product = utils.get_product_card(product_id)
    categories = get_product_category(product_id)
    print(categories)
    print(categories[0])
    print(categories[1])

    product_model = ProductModel(
        nm_id=product[0]["id"],
        name=product[0]["name"],
        brand=product[0]["brand"],
        brand_id=product[0]["brandId"],
        site_brand_id=product[0]["siteBrandId"],
        supplier_id=product[0]["supplierId"],
        sale=product[0]["sale"],
        price=product[0]["priceU"] / 100,
        sale_price=product[0]["salePriceU"] / 100,
        rating=product[0]["rating"],
        feedbacks=product[0]["feedbacks"],
        colors=product[0]["colors"][0]["name"] if len(product[0]["colors"]) > 0 else None,
        category=categories[0],
        root_category=categories[1]
    )

    product_service.create_product(product_model)
    return product_model.name


@product_routes.put("/{product_id}")
def update_product(product_id: int):
    product = utils.get_product_card(product_id)
    categories = get_product_category(product_id)

    product_model = ProductModel(
        nm_id=product[0]["id"],
        name=product[0]["name"],
        brand=product[0]["brand"],
        brand_id=product[0]["brandId"],
        site_brand_id=product[0]["siteBrandId"],
        supplier_id=product[0]["supplierId"],
        sale=product[0]["sale"],
        price=product[0]["priceU"] / 100,
        sale_price=product[0]["salePriceU"] / 100,
        rating=product[0]["rating"],
        feedbacks=product[0]["feedbacks"],
        colors=product[0]["colors"][0]["name"] if len(product[0]["colors"]) > 0 else None,
        category=categories[0],
        root_category=categories[1]
    )

    product_service.update_product(product_model)
    return product_model.name


@product_routes.delete("/{product_id}")
def delete_product(product_id: int):
    product_service.delete_product(product_id)




