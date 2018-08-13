# coding=utf-8
import unittest
import time
import HTMLTestRunner

from page.MobileLogin import *
from selenium import webdriver
from variable.User import *
from variable.base_url import Url


# edu-public-15:短信登录模块测试用例集
class TestMobileLogin(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        self.driver=webdriver.Chrome()
        self.page=MobileLogin(self.driver, root_uri=base_url)

    # 输入手机号码，点击发送验证码，手机收到慕测平台发送的验证码短信
    def test_send_captcha_success(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btnm.click()
        self.page.mobile = user['phone']
        self.page.btnf.click()
        time.sleep(1)
        self.assertEqual(self.page.send_success.text,self.page.captcha_send_success_content)

    # 输入错误格式的手机号，提示手机格式错误
    def test_wrong_mobile_number(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btnm.click()
        self.page.mobile = user['phone']+'1'
        self.page.btnf.click()
        time.sleep(1)
        self.assertEqual(self.page.mobile_error.text,self.page.mobile_error_content)

    # 输入验证码错误，提示验证码错误
    def test_wrong_captcha(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btnm.click()
        self.page.mobile = user['phone']
        # self.page.btnf.click()
        # time.sleep(6)
        self.page.captcha=self.page.wrong_captcha
        self.page.btn.click()
        time.sleep(1)
        self.assertEqual(self.page.captcha_error.text,self.page.captcha_error_content)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    filepath = '../report/test_mobile_login.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMobileLogin('test_send_captcha_success'))
    suite.addTest(TestMobileLogin('test_wrong_mobile_number'))
    suite.addTest(TestMobileLogin('test_wrong_captcha'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='短信登录模块测试用例集')
    runner.run(suite)



