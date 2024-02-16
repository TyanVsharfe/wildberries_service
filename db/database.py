from sqlalchemy import create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', connect_args={"check_same_thread": False})
Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    nm_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    brand = Column(String)
    brand_id = Column(Integer)
    site_brand_id = Column(Integer)
    supplier_id = Column(Integer)
    sale = Column(Integer)
    price = Column(Integer)
    sale_price = Column(Integer)
    rating = Column(Float)
    feedbacks = Column(Integer)
    colors = Column(String)

    def to_json(self):
        return {
            "nm_id": self.nm_id,
            "name": self.name,
            "brand": self.brand,
            "brand_id": self.brand_id,
            "site_brand_id": self.site_brand_id,
            "supplier_id": self.supplier_id,
            "sale": self.sale,
            "price": self.price,
            "sale_price": self.sale_price,
            "rating": self.rating,
            "feedbacks": self.feedbacks,
            "colors": self.colors,
        }


SessionLocal = sessionmaker(autoflush=False, bind=engine)