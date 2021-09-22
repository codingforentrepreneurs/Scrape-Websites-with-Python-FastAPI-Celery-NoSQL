from celery import Celery
from celery.signals import (
    beat_init,
    worker_process_init,
)

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from . import (
    config,
    db,
    models
)

celery_app = Celery(__name__)
settings = config.get_settings()

REDIS_URL = settings.redis_url
celery_app.conf.broker_url = REDIS_URL
celery_app.conf.result_backend = REDIS_URL

Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent

def celery_on_startup(*args, **kwargs):
    if connection.cluster is not None:
        connection.cluster.shutdown()
    if connection.session is not None:
        connection.session.shutdown()
    cluster = db.get_cluster()
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    sync_table(Product)
    sync_table(ProductScrapeEvent)


beat_init.connect(celery_on_startup)
worker_process_init.connect(celery_on_startup)


@celery_app.task
def random_task(name):
    print(f"Who throws a shoe. Honestly {name}.")



@celery_app.task
def list_products():
    q = Product.objects().all().values_list("asin", flat=True)
    print(list(q))