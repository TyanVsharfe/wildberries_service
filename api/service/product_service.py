from api.models.Product import CreateProductModel
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
        for p in products:
            print(f"{p}\n")
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


def delete_product(product_id: int):
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.nm_id == product_id).first()
        db.delete(product)
        db.commit()
    finally:
        db.close()
