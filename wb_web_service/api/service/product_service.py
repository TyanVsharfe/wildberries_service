from datetime import datetime, timedelta
import requests
from sqlalchemy import func
from starlette.responses import JSONResponse

from wb_web_service.api.models.Product import ProductModel, ProductCategoryModel
from wb_web_service.api.routers import product_router
from wb_web_service.api.utils import utils
from wb_web_service.api.utils.utils import get_basket_id
from wb_web_service.db.database import SessionLocal, Product


def get_product(product_id: int):
    db = SessionLocal()
    try:
        return db.query(Product).filter(Product.nm_id == product_id).first()
    finally:
        db.close()


def get_products():
    db = SessionLocal()
    try:
        return db.query(Product).all()
    finally:
        db.close()


def create_product(new_product: ProductModel):
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
            category=new_product.category,
            root_category=new_product.root_category,
            colors=new_product.colors
        )
        db.add(product)
        db.commit()
        return product
    finally:
        db.close()


def update_product(new_product: ProductModel):
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.nm_id == new_product.nm_id).first()

        product.name = new_product.name
        product.brand = new_product.brand
        product.brand_id = new_product.brand_id
        product.site_brand_id = new_product.site_brand_id
        product.supplier_id = new_product.supplier_id
        product.sale = new_product.sale
        product.price = new_product.price
        product.sale_price = new_product.sale_price
        product.rating = new_product.rating
        product.feedbacks = new_product.feedbacks
        product.colors = new_product.colors
        product.category = new_product.category
        product.root_category = new_product.root_category

        db.commit()
        return product
    finally:
        db.close()


def update_all_products():
    db = SessionLocal()
    try:
        ids = db.query(Product.nm_id).all()
        for i in ids:
            product_router.update_product(i)
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


def get_products_count():
    db = SessionLocal()
    try:
        return db.query(Product).count()
    finally:
        db.close()


def get_products_count_by_category():
    db = SessionLocal()
    try:
        products_by_category = db.query(
            Product.category, func.count(Product.nm_id)
        ).group_by(Product.category).all()
        print(products_by_category)

        data = [
            {
                "category": row[0],
                "count": row[1],
            }
            for row in products_by_category
        ]
        # print(data)

        return JSONResponse(data)
    finally:
        db.close()


def get_products_categories():
    db = SessionLocal()
    try:
        products_by_category = db.query(
            Product.category, func.count(Product.nm_id)
        ).group_by(Product.category).all()
        print(products_by_category)

        data = [
            {
                "category": row[0],
                "count": row[1],
            }
            for row in products_by_category
        ]
        # print(data)

        return JSONResponse(data)
    finally:
        db.close()


def get_products_by_category(product_id: int):
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.nm_id == product_id).first()
        print(product)
        products = db.query(Product).filter(Product.category == product.category).all()

        categories = db.query(Product).filter(Product.nm_id == product_id).distinct("category").all()
        brands = db.query(Product).filter(Product.nm_id == product_id).distinct("brand").all()

        data_c = [{"category": category.category} for category in categories]
        data_b = [{"brand": brand.brand} for brand in brands]

        print(data_c, data_b)
    finally:
        db.close()

    product_data = []
    for product in products:
        product_dict = ProductCategoryModel(
            nm_id=product.nm_id,
            name=product.name,
            brand=product.brand,
            sale_price=product.sale_price,
            category=product.category,
            root_category=product.root_category
        )
        product_data.append(product_dict)
    print(product_data)
    return product_data, data_c, data_b


def get_history(product_id: int):

    url = f"https://basket-{get_basket_id(product_id)}.wbbasket.ru/vol{product_id // 100000}/part{product_id // 1000}/{product_id}/info/price-history.json"
    response = requests.get(url)

    product = utils.get_product_card(product_id)
    actual_price = {
        "dt": datetime.now().timestamp(),
        "price": {
            "RUB": product[0]["salePriceU"]
        }
    }

    if response.status_code == 200:
        json_data = response.json()
        json_data.append(actual_price)

        return json_data
    else:
        print("Ошибка при загрузке страницы:", response.status_code)


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


