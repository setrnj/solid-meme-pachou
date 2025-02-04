import redis

# 创建 Redis 连接时不要传递 password 参数，如果不需要认证的话
r = redis.StrictRedis(host='localhost', port=6379, db=0)

try:
    url = r.rpop('pending_urls')  # 取出一个网址
    if url:
        print(f"取出的网址是: {url.decode('utf-8')}")
    else:
        print("没有待处理的网址")
except redis.ConnectionError as e:
    print(f"连接 Redis 服务器失败: {e}")
