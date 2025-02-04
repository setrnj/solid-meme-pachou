import requests
import redis

# 创建 Redis 连接时不使用 password 参数
r = redis.Redis(host='hadoop01', port=6379, decode_responses=True)

def check_proxy(proxy):
    try:
        resp = requests.get('http://httpbin.org/ip',
                            proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'},
                            timeout=5
                            )
        if resp.status_code == 200:
            print(f"[有效代理] {proxy}")
            r.sadd('valid_proxies', proxy)
            return True
    except Exception as e:
        print(f"[无效代理] {proxy} 错误：{str(e)}")
        # 注意：这里需要确保在尝试移除前，该代理确实存在于 valid_proxies 中
        r.srem('valid_proxies', proxy)
    return False

if __name__ == '__main__':
    while True:
        # 从 Redis 中取出一个代理
        proxy = r.spop('temp_proxies')
        if not proxy:
            break
        # 确保解码正确
        check_proxy(proxy.decode())       
