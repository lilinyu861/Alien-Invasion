import HTMLTestRunner
import time
import unittest

from page.ModifyPasswdPage import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from variable.User import *
from variable.base_url import Url

class TestModifyPwdPage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        user = User().user_modify_new
        self.driver = webdriver.Chrome()
        self.page = ModifyPasswdPage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        self.driver.maximize_window()

    # 点击用户名，点击修改密码，进入个人信息界面
    def test_click_username(self):
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.user_info_url)

    # 4 旧密码输入错误
    def test_modify_wrong_oldpassword(self):
        user = User().user_modify_new
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.page.modifyPassword.click()
        self.page.oldPassword=user['wrong_passwd']
        self.page.confirmPassword.click()
        time.sleep(1)
        self.assertEqual(self.page.oldpassword_error.text,self.page.wrong_old_password_content)

    # 5 输入密码长度小于6位
    def test_modify_short_password(self):
        user = User().user_modify_new
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.page.modifyPassword.click()
        self.page.oldPassword = user['passwd']
        self.page.newPassword = user['short_newpasswd']
        self.page.repeatPassword = user['short_newpasswd']
        self.page.confirmPassword.click()
        time.sleep(1)
        self.assertEqual(self.page.pwdlen_error.text,self.page.password_length_error_content)

    # 5 输入密码长度大于16位
    def test_modify_long_password(self):
        user = User().user_modify_new
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.page.modifyPassword.click()
        self.page.oldPassword = user['passwd']
        self.page.newPassword = user['long_newpasswd']
        self.page.repeatPassword = user['long_newpasswd']
        self.page.confirmPassword.click()
        time.sleep(1)
        self.assertEqual(self.page.pwdlen_error.text,self.page.password_length_error_content )

    # 6 不输入旧密码提示‘请输入旧密码’
    def test_modify_null_oldpassword(self):
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.page.modifyPassword.click()
        self.page.oldPassword = ''
        self.page.confirmPassword.click()
        time.sleep(1)
        self.assertEqual(self.page.pwdlen_error.text,self.page.null_old_password_content)

    # 7 输入新密码与重复密码不一致提示'两次密码不一致'
    def test_modify_differ_password(self):
        user = User().user_modify_new
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.page.modifyPassword.click()
        self.page.oldPassword = user['passwd']
        self.page.newPassword = user['new_passwd']
        self.page.repeatPassword = user['differ_new_passwd']
        self.page.confirmPassword.click()
        time.sleep(1)
        self.assertEqual(self.page.differpwd_error.text, self.page.differ_password_content)

    # 8 输入验证码错误提示‘验证码错误’
    def test_modify_wrong_captcha(self):
        user = User().user_modify_new
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.page.modifyPassword.click()
        self.page.oldPassword = user['passwd']
        self.page.newPassword = user['new_passwd']
        self.page.repeatPassword = user['new_passwd']
        self.page.passwordCaptcha=self.page.wrong_captcha
        self.page.confirmPassword.click()
        time.sleep(1)
        self.assertEqual(self.page.differpwd_error.text, self.page.captcha_error_content)

    # 修改成功，修改为新密码’12345678‘
    def test_modify_success(self):
        user = User().user_modify_new
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.page.modifyPassword.click()
        self.page.oldPassword = user['passwd']
        self.page.newPassword = user['new_passwd']
        self.page.repeatPassword = user['new_passwd']
        self.page.passwordCaptcha = self.page.right_captcha
        self.page.confirmPassword.click()
        time.sleep(1)
        self.assertEqual(self.page.modifypasswd_success.text, '修改成功')
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.login_url)

        # 修改成功,修改为原来密码’111111‘
        self.page.email = user['email']
        self.page.passwd = user['new_passwd']
        self.page.btn.click()
        self.driver.maximize_window()
        time.sleep(2)
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.modifyPasswd.click()
        time.sleep(2)
        self.page.modifyPassword.click()
        self.page.oldPassword = user['new_passwd']
        self.page.newPassword = user['passwd']
        self.page.repeatPassword = user['passwd']
        self.page.passwordCaptcha = self.page.right_captcha
        self.page.confirmPassword.click()
        time.sleep(1)
        self.assertEqual(self.page.modifypasswd_success.text, '修改成功')
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.login_url)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    filepath = '../report/test_modify_user_password_page.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestModifyPwdPage('test_click_username'))
    suite.addTest(TestModifyPwdPage('test_modify_wrong_oldpassword'))
    suite.addTest(TestModifyPwdPage('test_modify_short_password'))
    suite.addTest(TestModifyPwdPage('test_modify_long_password'))
    suite.addTest(TestModifyPwdPage('test_modify_null_oldpassword'))
    suite.addTest(TestModifyPwdPage('test_modify_differ_password'))
    suite.addTest(TestModifyPwdPage('test_modify_wrong_captcha'))
    suite.addTest(TestModifyPwdPage('test_modify_success'))
    # suite.addTest(TestModifyPwdPage('test_click_username'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'修改密码模块测试用例集')
    runner.run(suite)
