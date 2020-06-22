import scrapy
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

class SocialNetworkSpider(scrapy.Spider):
    name = 'social_networks'
    # allowed_domains = ['tripadvisor.com/']
    allowed_domains = ['awca.com/']
    # start_urls = ['https://www.tripadvisor.com/']
    start_urls = ['https://www.awca.com/']

    #
    # def parse(self, response):
    #     social_networks_link = LxmlLinkExtractor(allow=r'https://[a-z.]+/[a-z.]+$',
    #                                              deny_domains=['shop.github.com','youtube.com','twitter.com'], unique = True).extract_links(response)
    #     for link in social_networks_link:
    #         print(f'link.url', 'link.text')

        # facebook_link = response.css('a::attr(href)').getall()
        # facebook_link = response.xpath('//a/@href').getall()
        # print(facebook_link)

    def parse(self, response):
        """ Main function that parses downloaded pages """
        # Print what the spider is doing
        print(response.url)
        # Get all the <a> tags
        a_selectors = response.xpath("//a")
        # Loop on each tag
        for selector in a_selectors:
            # Extract the link text
            text = selector.xpath("text()").extract_first()
            # Extract the link href
            link = selector.xpath("@href").extract_first()
            # Create a new Request object
            request = response.follow(link, callback=self.parse)
            # Return it thanks to a generator
            yield request