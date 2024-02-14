from fastapi import APIRouter
import requests

from api.models.Product import CreateProductModel
from api.service import product_service
from api.utils.utils import get_basket_id

product_routes = APIRouter()


@product_routes.get("/products")
def get_products():
    return product_service.get_products()


@product_routes.get("/product/{product_id}")
def get_product(product_id: int):
    return product_service.get_product(product_id)


@product_routes.get("/product/{product_id}/history")
def get_product_history(product_id: int):

    url = f"https://basket-{get_basket_id(product_id)}.wbbasket.ru/vol{product_id // 100000}/part{product_id // 1000}/{product_id}/info/price-history.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Ошибка при загрузке страницы:", response.status_code)


@product_routes.post("/product/{product_id}")
def add_product(product_id: int):
    url = f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={product_id}"
    response = requests.get(url)

    if response.status_code == 200:

        json_data = response.json()
        product = json_data["data"]["products"]

        product_model = CreateProductModel(
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
            colors=product[0]["colors"][0]["name"]
            )

        product_service.create_product(product_model)
        return product_model.name
    else:
        print("Ошибка при получении товара:", response.status_code)


@product_routes.delete("/product/{product_id}")
def delete_product(product_id: int):
    product_service.delete_product(product_id)
