import HTMLTestRunner
import time
import unittest

from selenium import webdriver
from page.RegisterPage import *
from variable.base_url import Url


class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        self.driver = webdriver.Chrome()
        self.page = RegisterPage(self.driver, root_uri=base_url)

    # 进入登录页面，点击“现在注册”，进入注册页面
    def test_click_registernow(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.register_url)

    # 依次输入用户名、邮箱、密码和确认密码，点击注册
    def test_register_success(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName=self.page.new_username
        self.page.email=self.page.new_email
        self.page.password=self.page.new_password
        self.page.passwordAgain=self.page.new_password
        self.page.register_btn.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.user_info_url)

    # 注册时没有输入邮箱或输入邮箱格式有错误
    def test_wrong_email(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName = self.page.new_username
        self.page.email = self.page.wrong_email
        self.page.password = self.page.new_password
        self.page.passwordAgain = self.page.new_password
        self.page.register_btn.click()
        time.sleep(1)
        self.assertEqual(self.page.error.text,self.page.email_error_content)

    # 注册时输入的邮箱已经被注册
    def test_had_email(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName = self.page.new_username
        self.page.email = self.page.had_email
        self.page.password = self.page.new_password
        self.page.passwordAgain = self.page.new_password
        self.page.register_btn.click()
        time.sleep(1)
        self.assertEqual(self.page.error.text,self.page.hademail_error_content)

    # 注册时确认密码和密码不一致
    def test_differ_password(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName = self.page.new_username
        self.page.email = self.page.new_email
        self.page.password = self.page.new_password
        self.page.passwordAgain = self.page.differ_password
        self.page.register_btn.click()
        time.sleep(1)
        self.assertEqual(self.page.error.text,self.page.differ_password_error_content)

    # 注册时用户名没有填写或过长或过短 2-16位
    def test_null_username(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName = self.page.null_username
        self.page.email = self.page.new_email
        self.page.password = self.page.new_password
        self.page.passwordAgain = self.page.new_password
        self.page.register_btn.click()
        time.sleep(2)
        # self.assertEqual(self.page.error.text,self.page.username_error_content)
        self.assertEqual(self.driver.current_url,self.page.register_url)

    def test_long_username(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName = self.page.long_username
        self.page.email = self.page.new_email
        self.page.password = self.page.new_password
        self.page.passwordAgain = self.page.new_password
        self.page.register_btn.click()
        time.sleep(1)
        self.assertEqual(self.page.error.text,self.page.username_error_content)

    def test_short_username(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName = self.page.short_username
        self.page.email = self.page.new_email
        self.page.password = self.page.new_password
        self.page.passwordAgain = self.page.new_password
        self.page.register_btn.click()
        time.sleep(1)
        self.assertEqual(self.page.error.text,self.page.username_error_content)

    # 注册时密码长度过短或过长 6-16位
    def test_long_password(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName = self.page.new_username
        self.page.email = self.page.new_email
        self.page.password = self.page.long_password
        self.page.passwordAgain = self.page.long_password
        self.page.register_btn.click()
        time.sleep(1)
        self.assertEqual(self.page.error.text,self.page.password_length_error_content)

    def test_short_password(self):
        self.driver.maximize_window()
        self.page.get('/login2')
        self.page.register_now.click()
        self.page.userName = self.page.new_username
        self.page.email = self.page.new_email
        self.page.password = self.page.short_password
        self.page.passwordAgain = self.page.short_password
        self.page.register_btn.click()
        time.sleep(1)
        self.assertEqual(self.page.error.text,self.page.password_length_error_content)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    filepath = '../report/test_register_page.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestRegisterPage('test_click_registernow'))
    suite.addTest(TestRegisterPage('test_register_success'))
    suite.addTest(TestRegisterPage('test_wrong_email'))
    suite.addTest(TestRegisterPage('test_had_email'))
    suite.addTest(TestRegisterPage('test_differ_password'))
    suite.addTest(TestRegisterPage('test_null_username'))
    suite.addTest(TestRegisterPage('test_long_username'))
    suite.addTest(TestRegisterPage('test_short_username'))
    suite.addTest(TestRegisterPage('test_long_password'))
    suite.addTest(TestRegisterPage('test_short_password'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title='注册模块测试用例集')
    runner.run(suite)