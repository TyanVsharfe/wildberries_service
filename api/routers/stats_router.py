from fastapi import APIRouter
from api.service import product_service

import plotly.graph_objects as go
import numpy as np

stats_routes = APIRouter()


@stats_routes.get("/count")
def get_products_count():
    return product_service.get_products_count()


@stats_routes.get("/graphics")
def get_products_count():
    np.random.seed(1)

    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N) * 30

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        marker=go.scatter.Marker(
            size=sz,
            color=colors,
            opacity=0.6,
            colorscale="Viridis"
        )
    ))

    fig.show()
    return product_service.get_products_count()


@stats_routes.get("/{product_id}/min-max")
def products_min_max(product_id: int):
    json_data = product_service.get_history(product_id)
    return product_service.get_product_min_max(json_data)