import json
from datetime import datetime, timedelta

import requests
from starlette.responses import JSONResponse

from api.models.Product import CreateProductModel
from api.utils.utils import get_basket_id
from db.database import SessionLocal, Product


def get_product(product_id: int):
    db = SessionLocal()
    try:
        return db.query(Product).filter(Product.nm_id == product_id).first()
    finally:
        db.close()


def get_products():
    db = SessionLocal()
    try:
        products = db.query(Product).all()
        return products
    finally:
        db.close()


def create_product(new_product: CreateProductModel):
    db = SessionLocal()
    try:
        product = Product(
            nm_id=new_product.nm_id,
            name=new_product.name,
            brand=new_product.brand,
            brand_id=new_product.brand_id,
            site_brand_id=new_product.site_brand_id,
            supplier_id=new_product.supplier_id,
            sale=new_product.sale,
            price=new_product.price,
            sale_price=new_product.sale_price,
            rating=new_product.rating,
            feedbacks=new_product.feedbacks,
            colors=new_product.colors
        )
        db.add(product)
        db.commit()
        return product
    finally:
        db.close()


def update_product(new_product: CreateProductModel):
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.nm_id == new_product.nm_id).first()

        product.name = new_product.name,
        product.brand = new_product.brand,
        product.brand_id = new_product.brand_id,
        product.site_brand_id = new_product.site_brand_id,
        product.supplier_id = new_product.supplier_id,
        product.sale = new_product.sale,
        product.price = new_product.price,
        product.sale_price = new_product.sale_price,
        product.rating = new_product.rating,
        product.feedbacks = new_product.feedbacks,
        product.colors = new_product.colors

        db.commit()
        return product
    finally:
        db.close()


def delete_product(product_id: int):
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.nm_id == product_id).first()
        db.delete(product)
        db.commit()
    finally:
        db.close()


def get_history(product_id: int):

    url = f"https://basket-{get_basket_id(product_id)}.wbbasket.ru/vol{product_id // 100000}/part{product_id // 1000}/{product_id}/info/price-history.json"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        for product in json_data:
            date = datetime.fromtimestamp(product["dt"])
            price = product["price"]["RUB"] / 100
            print(f"{date} - {price}")

        return json_data
    else:
        print("Ошибка при загрузке страницы:", response.status_code)


def get_products_count():
    db = SessionLocal()
    try:
        return db.query(Product).count()
    finally:
        db.close()


def get_product_min_max(json_data):
    current_date = datetime.now()
    six_months_ago = current_date - timedelta(days=30 * 6)

    six_months_ago_timestamp = six_months_ago.timestamp()
    print(current_date)
    print(datetime.fromtimestamp(six_months_ago_timestamp))

    filtered_data = [item for item in json_data if item["dt"] >= six_months_ago_timestamp]

    max_price = int(max(filtered_data, key=lambda x: x["price"]["RUB"])["price"]["RUB"] / 100)
    min_price = int(min(filtered_data, key=lambda x: x["price"]["RUB"])["price"]["RUB"] / 100)

    data = {
        "min_price": min_price,
        "max_price": max_price
    }

    return JSONResponse(data)
