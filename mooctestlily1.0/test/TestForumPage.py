import time
import unittest
import HTMLTestRunner

from variable.User import *
from page.ForumPage import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from variable.base_url import Url


class TestLogoutPage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        user = User().user_stu
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.page = ForumPage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(1)
    # 点击用户名，点击慕测论坛1
    def test_click_username_click_forum(self):
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.mooctest_forum.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_url)

    # 点击首页左侧慕测论坛2
    def test_click_left_forum(self):
        self.page.left_forum.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_url)

    # 点击慕测论坛界面中的登录，进入登录界面3
    def test_forum_login(self):
        self.page.left_forum.click()
        time.sleep(2)
        self.page.forum_login.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_login_url)

    # 输入用户名密码登录成功4
    def test_forum_login_success(self):
        user = User().user_stu
        self.page.left_forum.click()
        time.sleep(2)
        self.page.forum_login.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_login_url)
        self.page.username = user['email']
        self.page.password = user['passwd']
        self.page.forum_login_btn.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_url)

    # 输入错误的信息，停留在登录界面5
    def test_forum_login_wrong_password(self):
        user=User().user_wrong_pwd
        self.page.left_forum.click()
        time.sleep(2)
        self.page.forum_login.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_login_url)
        self.page.username = user['email']
        self.page.password = user['passwd']
        self.page.forum_login_btn.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_login_error_url)

    def test_forum_login_wrong_username(self):
        user = User().user_wrong_email
        self.page.left_forum.click()
        time.sleep(2)
        self.page.forum_login.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_login_url)
        self.page.username = user['email']
        self.page.password = user['passwd']
        self.page.forum_login_btn.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_login_error_url)

    def test_forum_null_username_password(self):
        user = User().user_null_passwd
        self.page.left_forum.click()
        time.sleep(2)
        self.page.forum_login.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_login_url)
        self.page.username = user['email']
        self.page.password = user['passwd']
        self.page.forum_login_btn.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.forum_login_url)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    filepath = "../report/test_forum_page.html"
    ftp=open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestLogoutPage('test_click_username_click_forum'))
    suite.addTest(TestLogoutPage('test_click_left_forum'))
    suite.addTest(TestLogoutPage('test_forum_login'))
    suite.addTest(TestLogoutPage('test_forum_login_success'))
    suite.addTest(TestLogoutPage('test_forum_login_wrong_username'))
    suite.addTest(TestLogoutPage('test_forum_login_wrong_password'))
    suite.addTest(TestLogoutPage('test_forum_null_username_password'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'论坛模块测试用例集')
    runner.run(suite)
