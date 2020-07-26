# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonshirtsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()
    image = scrapy.Field()
    no_of_ratings = scrapy.Field()
