from datetime import datetime

from fastapi import APIRouter
from api.service import product_service

import plotly.graph_objects as go

stats_routes = APIRouter()


@stats_routes.get("/count")
def get_products_count():
    return product_service.get_products_count()


@stats_routes.get("/categories/count")
def get_products_count():
    return product_service.get_products_count_by_category()


@stats_routes.get("/{product_id}/graphics")
def get_products_line_chart(product_id: int):

    print(product_id)
    history = product_service.get_history(product_id)

    for product in history:
        product["dt"] = datetime.fromtimestamp(product["dt"])
        product["price"]["RUB"] /= 100
        # print(f"{product['dt']} - {product['price']['RUB']}")

    dates = [d['dt'] for d in history]
    prices = [int(d['price']['RUB']) for d in history]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name='Цена'))
    fig.update_layout(title='График изменения цены',
                      xaxis_title='Дата',
                      yaxis_title='Цена (RUB)')

    fig.show()


@stats_routes.get("/{product_id}/categories/graphics")
def get_products_line_chart(product_id: int):

    print(product_id)
    history = product_service.get_history(product_id)

    for product in history:
        product["dt"] = datetime.fromtimestamp(product["dt"])
        product["price"]["RUB"] /= 100
        # print(f"{product['dt']} - {product['price']['RUB']}")

    dates = [d['dt'] for d in history]
    prices = [int(d['price']['RUB']) for d in history]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name='Цена'))
    fig.update_layout(title='График изменения цены',
                      xaxis_title='Дата',
                      yaxis_title='Цена (RUB)')

    fig.show()


@stats_routes.get("/{product_id}/min-max")
def products_min_max(product_id: int):
    json_data = product_service.get_history(product_id)
    return product_service.get_product_min_max(json_data)