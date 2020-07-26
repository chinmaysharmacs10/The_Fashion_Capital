import scrapy
from ..items import AmazonshirtsItem

class AmazonTshirtSpider(scrapy.Spider):
    name = 'amazon_tshirt'
    #allowed_domains = ['amazon.in']
    page_no = 2
    website = ['https://www.amazon.in']

    start_urls = ['https://www.amazon.in/gp/browse.html?node=1968120031&ref_=nav_em_sbc_mfashion_tshirts_0_2_9_3']

    def parse(self, response):

        all_tshirts = response.css(".s-latency-cf-section")
        c = 0
        for tshirts in all_tshirts:
            #name = tshirts.css(".a-size-base-plus.a-text-normal::text").extract_first()
            #no_of_rating = tshirts.css(".a-size-small .a-size-base::text").extract_first()
            #image_url = tshirts.css(".s-image::attr(src)").extract_first()
            #rating = tshirts.css("span.a-icon-alt::text").extract_first()

            tshirt_url = self.website[0] + tshirts.css("a.a-link-normal.a-text-normal::attr(href)").extract_first()
            c+=1
            #print(name,tshirt_url)
            yield scrapy.Request(tshirt_url, callback=self.parse_tshirt)




            #print(name,image_url,rating,no_of_rating)
            #print(tshirt_url)

            '''items = AmazonshirtsItem()
            items['name'] = name
            items['url'] = tshirt_url
            items['rating'] = rating
            items['image'] = image_url
            items['no_of_ratings'] = no_of_rating

            yield items'''


        '''next_page = 'https://www.amazon.in/s?k=Men%27s+T-Shirts+%26+Polos&page=' + str(AmazonTshirtSpider.page_no) + '&_encoding=UTF8&c=ts&qid=1593753780&ts_id=1968120031&ref=sr_pg_' + str(AmazonTshirtSpider.page_no)
        if AmazonTshirtSpider.page_no <= 5:
            AmazonTshirtSpider.page_no += 1
            yield response.follow(next_page, callback=self.parse)'''


    def parse_tshirt(self,response):
        '''all_ratings = response.css(".card-padding")
        for rating in all_ratings:
            rating_value = rating.css(".review-rating::text").extract()
            #review = rating.css(".a-text-bold span::text").extract()
            review_date = rating.css(".review-date::text").extract()
            print(rating_value,review_date)'''

        name = response.xpath('//h1[@id="title"]/span/text()').extract()
        no_of_ratings = response.xpath('//a[@id="acrCustomerReviewLink"]/span/text()').extract()
        #image = response.xpath('//div[@class="imgTagWrapper"]/img/@src').extract_first()

        '''all_ratings = response.css(".card-padding")
        #for rating in all_ratings:
            rat_val = response.xpath("//i[contains(@data-hook,"review-star-rating")]/span/text()").extract()
            rev_date = response.xpath("//span[contains(@class,"a-size-base a-color-secondary review-date")]/text()").extract()
            rev = response.xpath("//a[contains(@data-hook,"review-title")]/span/text()").extract()
            print(rat_val,rev_date,rev)'''


        #image_url = response.css(".a-dynamic-image.a-stretch-vertical::attr(src)").extract()
        print(name,no_of_ratings)

        #items = AmazonshirtsItem()
        #items['Name'] = name
        #items['Ratings'] = no_of_ratings

        #yield items





