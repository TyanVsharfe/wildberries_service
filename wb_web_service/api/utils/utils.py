import requests

from wb_web_service.api.models.Product import ProductModel


def get_product_card(product_id):
    url = f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={product_id}"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        product = json_data["data"]["products"]

        return product
    else:
        print("Ошибка при получении товара:", response.status_code)
        return None


def get_product_model(product_id):
    product = get_product_card(product_id)
    categories = get_product_category(product_id)

    if product or categories is None:
        ValueError("Неверный ID товара")
        return {"Error": "Неверный ID товара"}

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

    return product_model


def get_product_category(product_id):
    b_id = get_basket_id(product_id)
    if b_id is None:
        ValueError("Неверный ID товара")
        return None
    url = f"https://basket-{b_id}.wbbasket.ru/vol{product_id // 100000}/part{product_id // 1000}/{product_id}/info/ru/card.json"
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        category = json_data["subj_name"]
        root_category = json_data["subj_root_name"]

        return category, root_category
    else:
        print("Ошибка при получении товара:", response.status_code)


def get_basket_id(product_id: int) -> str:
    short_id = product_id // 100000

    if 0 <= short_id <= 143:
        basket = "01"
    elif 144 <= short_id <= 287:
        basket = "02"
    elif 288 <= short_id <= 431:
        basket = "03"
    elif 432 <= short_id <= 719:
        basket = "04"
    elif 720 <= short_id <= 1007:
        basket = "05"
    elif 1008 <= short_id <= 1061:
        basket = "06"
    elif 1062 <= short_id <= 1115:
        basket = "07"
    elif 1116 <= short_id <= 1169:
        basket = "08"
    elif 1170 <= short_id <= 1313:
        basket = "09"
    elif 1314 <= short_id <= 1601:
        basket = "10"
    elif 1602 <= short_id <= 1655:
        basket = "11"
    elif 1656 <= short_id <= 1919:
        basket = "12"
    elif 1920 <= short_id <= 2163:
        basket = "13"
    elif 2164 <= short_id <= 2407:
        basket = "14"
    elif 2408 <= short_id <= 2651:
        basket = "15"
    elif 2652 <= short_id <= 2895:
        basket = "16"
    elif 2896 <= short_id <= 3139:
        basket = "17"
    else:
        basket = None

    return basket


