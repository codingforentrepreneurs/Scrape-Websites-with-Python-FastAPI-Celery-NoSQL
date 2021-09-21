from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
data = {
    "asin": "TESTING123D",
    "title": "Mark 1adsf"
}


class Product(Model): # -> table
    __keyspace__ = "scraper_app" #
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")


# def this -> Product.objects().filter(asin="AMZNIDNUMBER")

# not this -> Product.objects().filter(title="Mark 1")