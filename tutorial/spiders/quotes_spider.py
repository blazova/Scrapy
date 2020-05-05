import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]


    def parse(self, response):

        # Extracting data in our spider

        for quote in response.css('div.quote'):
            # A Scrapy spider typically generates many 
            # dictionaries containing the data extracted
            # from the page. To do that, we use the yield 
            # Python keyword in the callback:

            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }


# Storing the scraped data:

# The simplest way to store the scraped data is by using Feed exports, with the following command:

# scrapy crawl quotes -o quotes.json

# That will generate an quotes.json file containing all scraped items, serialized in JSON.

# For historic reasons, Scrapy appends to a given file instead of overwriting its contents. 
# If you run this command twice without removing the file before the second time, 
# you’ll end up with a broken JSON file.

# You can also use other formats, like JSON Lines:

# scrapy crawl quotes -o quotes.jl

#The JSON Lines format is useful because it’s stream-like, you can easily append new records 
# to it. It doesn’t have the same problem of JSON when you run twice.