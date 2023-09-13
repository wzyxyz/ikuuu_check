import requests, json, re, os
from lxml import etree

session = requests.session()
# ikuuu用户名
EMAIL = os.environ.get('EMAIL')
# ikuuu密码
PASSWD = os.environ.get('PASSWD')
# server酱
SCKEY = os.environ.get('SCKEY')


def get_url():
    publish = "https://ikuuu.club/"
    response = session.get(url=publish)
    tree = etree.HTML(response.text)
    ip = tree.xpath("/html/body/center[1]/p[1]/a/text()")[0]
    return ip


def checkin():
    url = get_url()
    login_url = '{}/auth/login'.format(url)
    check_url = '{}/user/checkin'.format(url)
    header = {
        'origin': url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    data = {
        'email': EMAIL,
        'passwd': PASSWD
    }
    try:
        response = json.loads(session.post(url=login_url, headers=header, data=data).text)
        # 进行签到
        result = json.loads(session.post(url=check_url, headers=header).text)
        content = result['msg']
        # 进行推送
        if SCKEY != '':
            push_url = 'https://sctapi.ftqq.com/{}.send?title=ikuuu签到成功&desp={}'.format(SCKEY, content)
            requests.post(url=push_url)
    except Exception as e:
        content = str(e)
        if SCKEY != '':
            push_url = 'https://sctapi.ftqq.com/{}.send?title=ikuuu签到失败&desp={}'.format(SCKEY, content)
            requests.post(url=push_url)


if __name__ == "__main__":
    checkin()
