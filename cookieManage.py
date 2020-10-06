# -*- coding:utf-8 -*-
import json
from selenium import webdriver
from configUtils import Config
import findAppliedBills
import time

login_url = "http://cloud.easipass.com/ols/home.do#"
config = Config()


class CookieManage:
    def __init__(self):
        self.cookie_str = ""
        self.driver = ""

    def open_window(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('log-level=3')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("--auto-open-devtools-for-tabs")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=config.get_value("chrome_driver"))
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(8)  # 设置超时
        self.driver.set_script_timeout(8)

    @staticmethod
    def test_cookie():
        bill_json = findAppliedBills.get_booking_no_list()
        if bill_json and bill_json["total"] >= 0:
            return True
        else:
            return False

    def login_url(self):
        self.driver.get(login_url)
        while 1:  # 循环，直到判定登录成功，或者主动退出
            input_current = input("是否登录成功？（y/n）")
            if input_current == "y":
                if self.driver.get_cookies().__len__() <= 3:
                    print("没有正确的登录，请重试！")
                    continue
                else:
                    break
            elif input_current == "n":
                print("放弃登录！")
                return
            else:
                continue
        # 模拟游览器游览页面
        self.wonder_page()

    def wonder_page(self):
        current_cookie = input("输入cookie:")
        self.cookie_str = current_cookie
        config.add_value("cookie", current_cookie)

    def close_window(self):
        while input("是否关闭游览器？（y/n）") != "y":
            print("")
        self.driver.quit()


def main():
    cookie_manage = CookieManage()
    # 测试配置里的cookie是否任然有效
    has_cookie = cookie_manage.test_cookie()
    if has_cookie:
        print("配置里的cookie有效！")
        return
    # 配置里的cookie已经失效，需要重新登录更新cookie
    cookie_manage.open_window()
    cookie_manage.login_url()
    cookie_manage.close_window()


if __name__ == '__main__':
    main()
