# 启用Redis调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 启用Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 保持Redis连接
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# 保持爬虫状态（可选）
SCHEDULER_PERSIST = True

# 设置管道（用于存储结果到Redis）
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
