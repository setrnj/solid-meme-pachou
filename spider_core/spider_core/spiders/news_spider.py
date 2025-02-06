from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request

class NewsSpider(RedisSpider):
    name = 'news_spider'
    allowed_domains = ['news.baidu.com', 'www.qq.com']  # 添加qq.com到允许域名
    redis_key = 'spider:start_urls'  # 从Redis读取URL的键

def parse(self, response):  
    # 提取新URL并设置优先级  
    new_links = response.css("a::attr(href)").getall()  
    for link in new_links:  
        yield scrapy.Request(  
            url=link,  
            callback=self.parse,  
            priority=5  # 默认优先级  
        )          
            # 如果需要继续爬取，可以生成新的请求
            # yield Request(absolute_link, callback=self.parse)
