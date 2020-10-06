import time
from bs4 import BeautifulSoup
import requests
import json

url = "http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do/findBillInfo.do?shipCode=NPO"

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '16',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=pb52fyFCCRGTFL1PhnZ9FPh2VfFkktcBQBD616BjVwVPDjWpj7q1!-1556035624; EPCAS_TID=PGT-432773-40601020075D-u85Nj794elhkg0Rdki5uBnUutMU7FO3QHx4eXitRbB5rbKta6T; UM_distinctid=174cebf102919e-047b46a7ec0a05-58143518-1fa400-174cebf102a117; showQrcode=Y; showTranscarrierQrcode=Y; unReadCount=0; gateInFlag=; JSESSIONID=zMLXWyXDzeB6q92PT8mQ1HSTvC-s9fdCNyIIc1uCHbmFW4NicXrF!-1202925223; CNZZDATA3496066=cnzz_eid%3D1777890598-1601196461-%26ntime%3D1601340909',
    'Host': 'cloud.easipass.com',
    'Origin': 'http://cloud.easipass.com',
    'Referer': 'http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do/operate.do?shipCode=NPO&bookingno=204460301',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

form_data = {
    'billId': 401307000
}


def main():
    print(11111)
    wb_data = requests.post(url, headers=headers, data=form_data)
    print(wb_data.status_code)
    if wb_data.status_code == 200:
        print(wb_data.text)


if __name__ == '__main__':
    main()
