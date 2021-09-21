from cassandra.cqlengine.management import sync_table
from .db import get_session
from .models import Product

session = get_session()
sync_table(Product)

def create_entry(data:dict):
    return Product.create(**data)
