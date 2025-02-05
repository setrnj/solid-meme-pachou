from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request

class NewsSpider(RedisSpider):
    name = 'news_spider'
    allowed_domains = ['news.baidu.com', 'www.qq.com']  # 添加qq.com到允许域名
    redis_key = 'spider:start_urls'  # 从Redis读取URL的键

    def parse(self, response):
        # 解析标题和链接（保留原解析逻辑）
        titles = response.css("a::text").getall()
        links = response.css("a::attr(href)").getall()
        
        for title, link in zip(titles, links):
            # 处理相对链接
            absolute_link = response.urljoin(link)
            
            yield {
                "title": title.strip(),
                "link": absolute_link  # 使用绝对路径
            }
            
            # 如果需要继续爬取，可以生成新的请求
            # yield Request(absolute_link, callback=self.parse)
