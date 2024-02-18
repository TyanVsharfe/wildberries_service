from typing import Optional

from pydantic import BaseModel


class ProductModel(BaseModel):
    nm_id: int
    name: str
    brand: str
    brand_id: int
    site_brand_id: int
    supplier_id: int
    sale: int
    price: int
    sale_price: int
    rating: float
    feedbacks: int
    colors: Optional[str]
    category: str
    root_category: str


class ProductCategoryModel(BaseModel):
    nm_id: int
    name: str
    brand: str
    sale_price: int
    category: str
    root_category: str


