import requests
from pyquery import PyQuery as pq

def get_proxies():
    url = 'https://www.free-proxy-list.net/'
    try:
        resp = requests.get(url, timeout=10)
        doc = pq(resp.text)
        proxies = []
        for row in doc('table#proxylisttable tr'):
            ip = pq(row).find('td:nth-child(1)').text()
            port = pq(row).find('td:nth-child(2)').text()
            if ip and port:
                proxies.append(f"{ip}:{port}")
        return proxies
    except Exception as e:
        print(f"采集失败：{str(e)}")
        return []

if __name__ == '__main__':
    proxies = get_proxies()
    print("采集到代理：", proxies[:3], "...")
