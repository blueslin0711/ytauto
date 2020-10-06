import time
import requests
from configUtils import Config
import json

"""
    获取 马士基出口（宁波） 订单的列表（这个对象可以用来测试cookie是否可用）
"""

url = "http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do/findAppliedBills.do?shipCode=NPO"
cookie = Config().get_value("cookie")
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '197',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie,
        'Host': 'cloud.easipass.com',
        'Origin': 'http://cloud.easipass.com',
        'Referer': 'http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do?forward=msk/carrier/mskCarrierApplyCtnr'
                   '/mskCarrierApplyCtnr&shipCode=NPO&servfrom=ols&service=eir.html&ticket=PGT-554380-40601020075D'
                   '-wyzEPfCKpepRbgBTvxeEDxv59Lh7xNdBmt0fhVHnEA8AVCqFeh',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.121 Safari/537.36 '
}

form_data = {
    'param.greateEqual.mskeirBizApply.applyTime': '20201003000000',
    'param.lessEqual.mskeirBizApply.applyTime': '20201006235959',
    'className': 'com.easipass.business.model.MskeirBizApply  mskeirBizApply',
    'page': 1,
    'rows': 10
}


def get_booking_no_list():
    print(headers["Cookie"])
    wb_data = requests.post(url, headers=headers, data=form_data)
    print(wb_data.status_code)
    if wb_data.status_code == 200:
        return wb_data.json()


def main():
    booking_no_list = get_booking_no_list()
    print(booking_no_list)


if __name__ == '__main__':
    main()


# Request URL: http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do/findAppliedBills.do?shipCode=NPO
# Request Method: POST
# Status Code: 200 OK
# Remote Address: 180.167.29.54:80
# Referrer Policy: strict-origin-when-cross-origin
# Cache-Control: no-cache, must-revalidate
# Connection: Keep-alive
# Content-Length: 5415
# Content-Type: text/plain; charset=UTF-8
# Date: Tue, 06 Oct 2020 04:19:21 GMT
# P3P: CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"
# Pragma: no-cache
# Server: Apache/2.2.34 (Unix)
# Via: 1.1 ID-5301755341116374 uproxy-2
# X-Powered-By: Servlet/2.5 JSP/2.1
# Accept: application/json, text/javascript, */*; q=0.01
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7
# Connection: keep-alive
# Content-Length: 197
# Content-Type: application/x-www-form-urlencoded
# Cookie: JSESSIONID=zjPLf7rfGpWyH23GC4GLYMpPfpMby42gfnzJrfGJp9ddZL89KY6y!-2052631637; EPCAS_TID=PGT-554380-40601020075D-wyzEPfCKpepRbgBTvxeEDxv59Lh7xNdBmt0fhVHnEA8AVCqFeh; UM_distinctid=174cebf102919e-047b46a7ec0a05-58143518-1fa400-174cebf102a117; showQrcode=Y; showTranscarrierQrcode=Y; JSESSIONID=Osb8Dyu4MFOONkuH3qPZvHrlnayZWPZH3kh4CN0oOB6Bv7kGOjRD!-1202925223; CNZZDATA3496066=cnzz_eid%3D1777890598-1601196461-%26ntime%3D1601956687; unReadCount=0; gateInFlag=
# Host: cloud.easipass.com
# Origin: http://cloud.easipass.com
# Referer: http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do?forward=msk/carrier/mskCarrierApplyCtnr/mskCarrierApplyCtnr&shipCode=NPO&servfrom=ols&service=eir.html&ticket=PGT-554380-40601020075D-wyzEPfCKpepRbgBTvxeEDxv59Lh7xNdBmt0fhVHnEA8AVCqFeh
# User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
# shipCode: NPO
# param.greateEqual.mskeirBizApply.applyTime: 20201003000000
# param.lessEqual.mskeirBizApply.applyTime: 20201006235959
# className: com.easipass.business.model.MskeirBizApply  mskeirBizApply
# page: 1
# rows: 10