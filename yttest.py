import time
from bs4 import BeautifulSoup
import requests
import json

url = "http://cloud.easipass.com/ols/app/getAppInfos.json?t="

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': 'EPCAS_TID=PGT-409700-40601020075D-JCExYqVVHI1o4cvSFjsy6SKyayfVimzs2KQqefLcxUeRbWK0xr; UM_distinctid=174cebf102919e-047b46a7ec0a05-58143518-1fa400-174cebf102a117; showQrcode=Y; showTranscarrierQrcode=Y; JSESSIONID=41LT1oEEyoqywC-ienLap4qrZMZVOJ89-ZAG7QzmuzcqssB-66jF!-1202925223; unReadCount=0; gateInFlag=; CNZZDATA3496066=cnzz_eid%3D1777890598-1601196461-%26ntime%3D1601283344',
    'Host': 'cloud.easipass.com',
    'Referer': 'http://cloud.easipass.com/ols/home.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def main():
    print(11111)
    t = int(round(time.time() * 1000))
    new_url = url + str(t)
    wb_data = requests.get(new_url, headers=headers)
    print(wb_data.status_code)
    if wb_data.status_code == 200:
        print(wb_data.text)


if __name__ == '__main__':
    main()
