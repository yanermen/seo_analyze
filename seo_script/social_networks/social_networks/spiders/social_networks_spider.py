import scrapy
import re


class SocialNetworkSpider(scrapy.Spider):
    name = 'social_networks'
    start_urls = ['https://www.mercedes-benz.com/']


    def parse(self, response):

        social_networks_link = response.css('a::attr(href)').getall()

        pattern_fb = r'^https://www.facebook.com/\w+'
        pattern_twitter = r'^https://twitter.com/\w+'

        for link in social_networks_link:
            if re.match(pattern_fb, link):
                print(link)
                continue
            elif re.match(pattern_twitter, link):
                print(link)
                break


