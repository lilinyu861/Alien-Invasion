#coding=utf-8
import unittest
import time
import HTMLTestRunner

from page.TestTargetPage import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from variable.User import *
from variable.base_url import Url


class TestTestcasePage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        user = User().user_tea
        self.driver=webdriver.Chrome()
        self.page=TestTargetPage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(1)
        self.driver.maximize_window()

    # 点击题库-测试目标，进入测试目标界面
    def test_click_into_test_target_page(self):
        self.page.question_bank.click()
        self.page.test_target.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.test_target_url)

    # 点击新建 进入新建测试目标界面
    def test_create_test_target(self):
        self.page.question_bank.click()
        self.page.test_target.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.create_new_test_target_url)

    def test_create_test_target_success(self):
        self.page.question_bank.click()
        self.page.test_target.click()
        time.sleep(2)
        self.page.new_btn.click()
        time.sleep(2)
        self.page.subsiteId_app.click()
        self.page.appName=self.page.app_name
        s1 = Select(self.page.select_class)
        s1.select_by_index(1)
        self.page.upload_app.click()
        time.sleep(2)
        self.page.imageFile = 'D:\\mooctest\\file\\testtarget.txt'
        self.page.description.click()
        self.page.description = self.page.description_content
        time.sleep(6)
        # self.page.create_btn.click()

    def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTestcasePage('test_click_into_test_target_page'))
    suite.addTest(TestTestcasePage('test_create_test_target_success'))
    firepath = '../report/test_test_case_page.html'
    fp = open(firepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试案例模块测试用例集')
    runner.run(suite)

