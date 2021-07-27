import scrapy
import re

class BlogPostSpider(scrapy.Spider):
    name = 'blog_post'
    allowed_domains = ['www.zyte.com']
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for post in response.css('div.oxy-post'):        
            title = re.sub('\s+',' ', post.css('a.oxy-post-title::text').get()).strip()
            author = re.sub('\s+',' ', post.css('div.oxy-post-meta-author.oxy-post-meta-item::text').get()).strip()
            refer = re.sub('\s+',' ',post.css('a.oxy-read-more::attr(href)').get()).strip()
        
            initial_data =  {'title': title,
               'author':author,
               'refer':response.urljoin(refer)
                }
            #CALL A parse_post METHOD WHICH LEADS TO OTHER URL. PASS META DATA ALONG WITH CALLBACK.
            yield scrapy.Request(response.urljoin(refer), callback=self.parse_post, meta={'item': initial_data})       
         
        #FETCH THE URL FOR NEXT PAGE AND CALLBACK parse
        next_url = response.css('a.next.page-numbers::attr(href)').get()
        if next_url:
            next_page = response.urljoin( re.sub('\s+',' ', next_url).strip() )
            yield scrapy.Request(next_page, callback=self.parse)
##            
            
            
    def parse_post(self, response):
        # STEP1: Collect meta data sent in the response.  
        item = response.meta['item']
        
        # STEP2: Crawl data from this function and add it to item.
        post_title = re.sub('\s+',' ', response.css('h1.ct-headline span.ct-span::text').get()).strip()
        read_time = re.sub('\s+',' ', response.css('span.rt-time::text').get()).strip()
        published_date = re.sub('\s+',' ', response.css('div.ct-text-block.blog-date span.ct-span::text').get()).strip()
        item['Post Title'] = post_title
        item['published_date'] = published_date
        item['read_time'] = read_time
        
        # STEP3: At the end yield item      yield item
        yield item
    
        
      
