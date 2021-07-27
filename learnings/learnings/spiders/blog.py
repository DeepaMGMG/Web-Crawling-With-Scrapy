import scrapy
import re


class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['www.zyte.com']
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for post in response.css('div.oxy-post'): 
#            print(post)
            
            title = re.sub('\s+',' ', post.css('a.oxy-post-title::text').get()).strip()
            author = re.sub('\s+',' ', post.css('div.oxy-post-meta-author.oxy-post-meta-item::text').get()).strip()
            refer = re.sub('\s+',' ',post.css('a.oxy-read-more::attr(href)').get()).strip()
        
            yield {'title': title,
               'author':author,
               'refer':response.urljoin(refer)
                }
            
        next_url = re.sub('\s+',' ', response.css('a.next.page-numbers::attr(href)').get()).strip()
        if next_url:
            next_page = response.urljoin(next_url)
            yield scrapy.Request(next_page, callback=self.parse)
            
        
