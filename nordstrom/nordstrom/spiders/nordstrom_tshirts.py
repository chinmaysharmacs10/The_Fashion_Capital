import scrapy
from ..items import NordstromItem


class NordstromTshirtsSpider(scrapy.Spider):
    name = 'nordstrom_tshirts'
    #allowed_domains = ['https://shop.nordstrom.com/c/mens-tshirts?origin=topnav']
    start_urls = ['https://shop.nordstrom.com/c/mens-tshirts?origin=topnav&breadcrumb=Home%2FMen%2FClothing%2FT-Shirts%20%26%20Tank%20Tops']

    def parse(self, response):
        items = NordstromItem()

        product_name = response.css("a._1av3_::attr(title)").extract()
        product_price = response.css("._3bi0z ._3wu-9").css('::text').extract()
        product_image = response.css("img.TDd9e::attr(src)").extract()
        product_rating = response.css("._1Td8y::text").extract()
        no_of_ratings = response.css("span._1uDOY::text").extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_image'] = product_image
        items['product_rating'] = product_rating
        items['no_of_ratings'] = no_of_ratings

        yield items

