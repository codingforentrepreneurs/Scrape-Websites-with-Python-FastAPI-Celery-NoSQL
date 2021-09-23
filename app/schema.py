from uuid import UUID
from typing import Optional, Any
from pydantic import BaseModel, root_validator

from . import utils

class ProductSchema(BaseModel):
    asin: str
    title: Optional[str]


class ProductListSchema(BaseModel):
    asin: str
    title: Optional[str]
    price_str: Optional[str]
    brand: Optional[str]
    country_of_origin: Optional[str]


class ProductScrapeEventSchema(BaseModel):
    uuid: UUID
    asin: str
    title: Optional[str]
    price_str: Optional[str]


class ProductScrapeEventDetailSchema(BaseModel):
    asin: str
    title: Optional[str]
    price_str: Optional[str]
    created: Optional[Any] = None
    brand: Optional[str]
    country_of_origin: Optional[str]

    @root_validator(pre=True)
    def extra_create_time_from_uuid(cls, values):
        values['created'] = utils.uuid1_time_to_datetime(values['uuid'].time).timestamp()
        return values       
