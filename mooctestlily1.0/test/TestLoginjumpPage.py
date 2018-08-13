# coding=utf-8
import unittest
import HTMLTestRunner
import time

from selenium import webdriver
from page.LoginjumpPage import *
from variable.User import *
from variable.base_url import Url


class TestLoginjumpPage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        self.driver = webdriver.Chrome()
        self.page = LoginjumpPage(self.driver, root_uri=base_url)

    # edu-public-7-[1]
    # 未登录状态跳转
    def test_not_login_jump(self):
        self.page.get('')
        time.sleep(6)
        self.assertEqual(self.driver.current_url,self.page.login_url)

    # 输入正确用户账号密码，用户信息不全，则进入/user/info界面
    def test_not_full_info(self):
        user=User().user_uncomlete_info
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.main_url)

    # 输入正确用户密码，用户信息全，则进入大赛报名页面
    def test_full_info(self):
        user=User().user_stu
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url,self.page.contest_url)

    # 普通用户输入http://www.mooctest.net/user/info，跳转到登录界面
    def test_user_input_user_info(self):
        user=User().user_stu
        self.page.get('/user/info')
        time.sleep(6)
        self.assertEqual(self.driver.current_url,self.page.login_url)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.user_info_url)

    # 普通教师用户/conpetition/list
    def test_teacher_contest(self):
        user = User().user_tea
        self.page.get('/competition/list')
        time.sleep(6)
        self.assertEqual(self.driver.current_url, self.page.login_url)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, self.page.main_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    filepath = '../report/test_login_jump.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestLoginjumpPage('test_not_login_jump'))
    suite.addTest(TestLoginjumpPage('test_not_full_info'))
    suite.addTest(TestLoginjumpPage('test_full_info'))
    suite.addTest(TestLoginjumpPage('test_user_input_user_info'))
    suite.addTest(TestLoginjumpPage('test_teacher_contest'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'用户登录跳转测试')
    runner.run(suite)

