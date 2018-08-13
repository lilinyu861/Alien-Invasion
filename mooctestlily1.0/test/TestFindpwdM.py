# coding=utf-8
import unittest
import time
import HTMLTestRunner

from selenium import webdriver
from page.FindpwdMPage import *
from variable.User import *
from variable.base_url import Url


class TestFindpwdM(unittest.TestCase):

    def setUp(self):
        base_url = Url().base_url
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.page=FindpssMPage(self.driver, root_uri=base_url)

    # 在忘记密码页面，输入错误格式的手机号,提示'请输入一个有效的手机号'
    def test_wrong_phone(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btn1.click()
        time.sleep(2)
        self.page.btn2.click()
        time.sleep(2)
        self.page.mobile = user['phone']+'1'
        self.page.btnf.click()
        time.sleep(1)
        self.assertEqual(self.page.phonenum_error.text, self.page.phonenum_error_content)

    # 在忘记密码页面，输入验证码错误，提示'错误' 'Invalid mobile captcha'
    def test_wrong_captcha(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btn1.click()
        time.sleep(2)
        self.page.btn2.click()
        time.sleep(2)
        self.page.mobile = user['phone']
        self.page.captcha = self.page.wrong_captcha
        self.page.btnc.click()
        time.sleep(1)
        self.assertEqual(self.page.captcha_error.text, self.page.captcha_error_content)
        self.assertEqual(self.page.captcha_error1.text,self.page.captcha_error1_content)

    # 在重置密码页面新密码和确认密码不一致，提示'输入值不同'
    def test_differ_reset_password(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btn1.click()
        time.sleep(2)
        self.page.btn2.click()
        time.sleep(2)
        self.page.mobile = user['phone']
        # self.page.btnf.click()
        self.page.captcha = self.page.right_captcha
        self.page.btnc.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.reset_password_url)
        self.page.newpassword = user['passwd']+'1'
        self.page.repeatpassword = user['passwd']+'11'
        self.page.btnc1.click()
        self.assertEqual(self.page.differ_passwd.text, self.page.differ_passwd_content)

    # 在重置密码页面输入密码过长或过短（6~16），提示'字符长度应该在6到16之间'
    def test_short_length_reset_password(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btn1.click()
        time.sleep(2)
        self.page.btn2.click()
        time.sleep(2)
        self.page.mobile = user['phone']
        # self.page.btnf.click()
        self.page.captcha = self.page.right_captcha
        self.page.btnc.click()
        time.sleep(2)
        js = "window.open('http://139.224.0.118/password/reset/')"
        self.driver.execute_script(js)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.assertEqual(self.page.reset_password_content,self.driver.page_source)
        self.page.newpassword = '12'
        self.page.repeatpassword = '12'
        self.page.btnc1.click()
        self.assertEqual(self.page.wronglen_passwd.text, self.page.wronglen_passwd_content)

    # 在重置密码页面输入密码过长或过短（6~16），提示'字符长度应该在6到16之间'
    def test_long_length_reset_password(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btn1.click()
        time.sleep(2)
        self.page.btn2.click()
        time.sleep(2)
        self.page.mobile = user['phone']
        # self.page.btnf.click()
        self.page.captcha = self.page.right_captcha
        self.page.btnc.click()
        time.sleep(2)
        js = "window.open('http://139.224.0.118/password/reset/')"
        self.driver.execute_script(js)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.assertEqual(self.page.reset_password_content,self.driver.page_source)
        self.page.newpassword = self.page.long_password
        self.page.repeatpassword = self.page.long_password
        self.page.btnc1.click()
        self.assertEqual(self.page.wronglen_passwd.text, self.page.wronglen_passwd_content)

    # TestCase1-03
    # 点击忘记密码，进入忘记密码界面,输入验证码，新密码，成功重置密码
    def test_reset_password_success(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btn1.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forget_password_url)
        self.page.btn2.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forget_password_url)
        self.page.mobile = user['phone']
        # 发送验证码
        # self.page.btnf.click()
        time.sleep(1)
        # self.assertEqual(self.page.send_captcha.text, self.page.send_success_content)
        # 手机验证码
        self.page.captcha = self.page.right_captcha
        self.page.btnc.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.reset_password_url)
        self.page.newpassword = user['passwd']+'1'
        self.page.repeatpassword = user['passwd']+'1'
        self.page.btnc1.click()
        self.assertEqual(self.page.reset_success.text, self.page.reset_success_content)

    # 设置密码为abc123
    def test_reset_password_success_abc123(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.btn1.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forget_password_url)
        self.page.btn2.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forget_password_url)
        self.page.mobile = user['phone']
        # self.page.btnf.click()
        time.sleep(1)
        # self.assertEqual(self.page.send_captcha.text, self.page.send_success_content)
        # 手机验证码
        self.page.captcha = self.page.right_captcha
        self.page.btnc.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.reset_password_url)
        self.page.newpassword = user['passwd']
        self.page.repeatpassword = user['passwd']
        self.page.btnc1.click()
        time.sleep(1)
        self.assertEqual(self.page.reset_success.text, self.page.reset_success_content)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    filepath = '../report/test_find_password_by_mobile.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestFindpwdM('test_wrong_phone'))
    suite.addTest(TestFindpwdM('test_wrong_captcha'))
    suite.addTest(TestFindpwdM('test_differ_reset_password'))
    suite.addTest(TestFindpwdM('test_short_length_reset_password'))
    suite.addTest(TestFindpwdM('test_long_length_reset_password'))
    suite.addTest(TestFindpwdM('test_reset_password_success'))
    suite.addTest(TestFindpwdM('test_reset_password_success_abc123'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'忘记密码手机找回模块测试用例')
    runner.run(suite)
    unittest.main()





