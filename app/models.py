from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
# data = {
#     "asin": "AMZNIDNUMBER",
#     "title": "Mark 1"
# }


class Product(Model): # -> table
    __keyspace__ = "scraper_app" #
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()



# def this -> Product.objects().filter(asin="AMZNIDNUMBER")

# not this -> Product.objects().filter(title="Mark 1")