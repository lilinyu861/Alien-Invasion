import HTMLTestRunner
import time
import unittest

from page.LogoutPage import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from variable.User import *
from variable.base_url import Url


class TestLogoutPage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        self.driver = webdriver.Chrome()
        self.page = LogoutPage(self.driver, root_uri=base_url)

    # 学生账号登录后退出
    def test_student_logout(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.logout.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.login_url)

    # 教师账号登录后退出
    def test_teacher_logout(self):
        user = User().user_tea
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.logout.click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, self.page.login_url)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    filepath = '../report/test_logout_page.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestLogoutPage('test_student_logout'))
    suite.addTest(TestLogoutPage('test_teacher_logout'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'退出登录模块测试用例集')
    runner.run(suite)
