import requests

# 目标网页的URL
url = 'https://matchday.ai/match/8919/analytics/advanced/analyse-by-shot-type'

try:
    # 发起GET请求获取网页内容
    response = requests.get(url)

    # 检查响应状态码，200表示成功
    if response.status_code == 200:
        # 打印网页内容
        print(response.text)
    else:
        print('请求失败，状态码:', response.status_code)

except requests.exceptions.RequestException as e:
    print('请求发生错误:', e)
