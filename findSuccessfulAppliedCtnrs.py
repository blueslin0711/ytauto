import time
import requests
from cookieManage import CookieManage
from configUtils import Config

url = "http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do/findSuccessfulAppliedCtnrs.do?shipCode=NPO"
bookingno = "204659855"
billId = 401164700
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '16',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': "",
        'Host': 'cloud.easipass.com',
        'Origin': 'http://cloud.easipass.com',
        'Referer': 'http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do/operate.do?shipCode=NPO&bookingno=' + bookingno,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

form_data = {
    'billId': billId
}


def execute_url(current_cookie):
    print("输出cookie:" + current_cookie)
    global headers
    headers["Cookie"] = current_cookie
    print(headers)
    wb_data = requests.post(url, headers=headers, data=form_data)
    print(wb_data.status_code)
    if wb_data.status_code == 200:
        print(wb_data.text)
    time.sleep(5)


def test_cookie(t_cookie):
    global headers
    headers["Cookie"] = t_cookie
    wb_data = requests.post(url, headers=headers, data=form_data)
    if wb_data.status_code == 200:
        if wb_data.text.find("看不清楚，请点击图片换一张") > 0:
            return False
        else:
            return True
    else:
        return False


def main():
    config = Config()
    t_cookie = config.get_value("cookie")
    if test_cookie(t_cookie):
        print("有用！")
    else:
        print("重新获取cookie")
        manage = CookieManage()
        manage.open_window()
        manage.login_url()
        print(manage.cookie_str)
        execute_url(manage.cookie_str)
        manage.close_window()


if __name__ == '__main__':
    main()



# Request URL: http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do/findSuccessfulAppliedCtnrs.do?shipCode=NPO
# Request Method: POST
# Status Code: 200 OK
# Remote Address: 180.167.29.54:80
# Referrer Policy: strict-origin-when-cross-origin
# Cache-Control: no-cache, must-revalidate
# Connection: Keep-alive
# Content-Length: 343
# Content-Type: text/plain; charset=UTF-8
# Date: Sat, 03 Oct 2020 07:34:13 GMT
# P3P: CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"
# Pragma: no-cache
# Server: Apache/2.2.34 (Unix)
# Via: 1.1 ID-5301755341116374 uproxy-2
# X-Powered-By: Servlet/2.5 JSP/2.1
# Accept: application/json, text/javascript, */*; q=0.01
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7
# Connection: keep-alive
# Content-Length: 16
# Content-Type: application/x-www-form-urlencoded
# Cookie: JSESSIONID=tGDBf4pGY2tzbh60RyL9qQLNXX1C5vYJM82lJgvZKKk1bRDw5m2B!-2052631637; EPCAS_TID=PGT-527742-40601020075D-WdfxhKyx4gYGjr8k3f7pYhG1rdRgVblF9gH2vLdabDcttUcE8u; UM_distinctid=174cebf102919e-047b46a7ec0a05-58143518-1fa400-174cebf102a117; showQrcode=Y; showTranscarrierQrcode=Y; JSESSIONID=XlLs8ZJIcTKPCV2cflyuGJVG62UUfZoq9Qe5EiTTDeD4_hyu5MFb!-1202925223; CNZZDATA3496066=cnzz_eid%3D1777890598-1601196461-%26ntime%3D1601710194; unReadCount=0; gateInFlag=
# Host: cloud.easipass.com
# Origin: http://cloud.easipass.com
# Referer: http://cloud.easipass.com/mskeir2/mskCarrierApplyCtnr.do/operate.do?shipCode=NPO&bookingno=204659855
# User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
# shipCode: NPO
# billId: 401164700