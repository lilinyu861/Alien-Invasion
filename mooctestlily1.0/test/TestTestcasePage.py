# coding=utf-8
import unittest
import time
import HTMLTestRunner

from page.TestcasePage import *
from selenium import webdriver
from variable.User import *
from variable.base_url import Url
from selenium.webdriver.support.ui import Select


class TestTestcasePage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        user = User().user_tea
        self.driver=webdriver.Chrome()
        self.page=TestcasePage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(1)
        self.driver.maximize_window()

    # 点击题库-测试案例，进入测试案例界面
    def test_click_into_test_case_page(self):
        self.page.question_bank.click()
        self.page.test_case.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.test_case_url)

    # 填写案例信息，点击提交创建成功，进入案例详情页面，有得分点数据
    def test_create_test_case_success(self):
        self.page.question_bank.click()
        self.page.test_case.click()
        time.sleep(2)
        self.page.create_exam.click()
        self.page.paperName.click()
        self.page.paperName.clear()
        self.page.paperName='TEST'
        self.page.paperDescription.click()
        self.page.paperDescription.clear()
        self.page.paperDescription='this is a test'
        time.sleep(2)
        self.page.add_case_btn.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTestcasePage('test_click_into_test_case_page'))
    suite.addTest(TestTestcasePage('test_create_test_case_success'))
    firepath = '../report/test_test_case_page.html'
    fp = open(firepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试案例模块测试用例集')
    runner.run(suite)

