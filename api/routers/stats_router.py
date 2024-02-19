import io
from datetime import datetime

from fastapi import APIRouter
from starlette.responses import Response

from api.service import product_service

import plotly.graph_objects as go

from api.utils import utils

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
    product_history = product_service.get_history(product_id)

    for product in product_history:
        product["dt"] = datetime.fromtimestamp(product["dt"])
        product["price"]["RUB"] /= 100
        # print(f"{product['dt']} - {product['price']['RUB']}")

    dates = [d['dt'] for d in product_history]
    prices = [int(d['price']['RUB']) for d in product_history]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name='Цена'))
    fig.update_layout(title='График изменения цены',
                      xaxis_title='Дата',
                      yaxis_title='Цена (RUB)')

    img_bytes = fig.to_image(format='png', engine="kaleido")
    print(img_bytes)
    return Response(content=img_bytes, media_type="image/png")
    # fig.show()


@stats_routes.get("/{product_id}/categories/graphics")
def get_products_categories_line_chart(product_id: int):
    print(product_id)
    products, categories, brands = product_service.get_products_by_category(product_id)

    fig = go.Figure()
    print(products)
    for p in products:
        product_history = product_service.get_history(p.nm_id)

        for product in product_history:
            product["dt"] = datetime.fromtimestamp(product["dt"])
            product["price"]["RUB"] /= 100
            # print(f"{product['dt']} - {product['price']['RUB']}")

        dates = [d['dt'] for d in product_history]
        prices = [int(d['price']['RUB']) for d in product_history]
        fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name=p.name))

    fig.update_layout(title=f'График изменения цены по категории {categories[0]["category"]}',
                      xaxis_title='Дата',
                      yaxis_title='Цена (RUB)')

    img_bytes = fig.to_image(format='png', engine="kaleido")
    return Response(content=img_bytes, media_type="image/png")
    # fig.show()


@stats_routes.get("/{product_id}/min-max")
def products_min_max(product_id: int):
    json_data = product_service.get_history(product_id)
    return product_service.get_product_min_max(json_data)
