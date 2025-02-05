import requests
import redis

r = redis.Redis(host='hadoop01', port=6379, password='123456')

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
        r.srem('valid_proxies', proxy)
    return False

if __name__ == '__main__':
    while True:
        proxy = r.spop('temp_proxies')
        if not proxy:
            break
        check_proxy(proxy.decode())
