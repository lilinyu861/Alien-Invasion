import time
import unittest
import HTMLTestRunner

from page.IntegralPage import *
from selenium import webdriver
from variable.User import *
from selenium.webdriver.common.action_chains import ActionChains
from variable.base_url import Url


class TestIntegralPage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        self.driver = webdriver.Chrome()
        self.page = IntegralPage(self.driver, root_uri=base_url)

    # 进入登录界面，输入正确的用户名密码 成功登录，进入主页面
    def test_login_view_integral(self):
        user = User().user_stu
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(2)
        # 进入个人信息界面，查看我的积分
        self.driver.maximize_window()
        ele =self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.page.user_info.click()
        time.sleep(1)
        a0=self.page.integral.text
        b0=int(a0)
        print(b0)

        # 退出，重新登录，进入个人信息页面，再次查看积分，积分比上次多一分
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.page.logout.click()
        time.sleep(2)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(2)
        # 进入个人信息界面，查看我的积分
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.page.user_info.click()
        time.sleep(1)
        a1 = self.page.integral.text
        b1 = int(a1)
        print(b1)

        # 再次退出，重新登录，进入个人信息页面，积分数与上次积分相同
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.page.logout.click()
        time.sleep(2)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(2)
        # 进入个人信息界面，查看我的积分
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.page.user_info.click()
        time.sleep(1)
        a2 = self.page.integral.text
        b2 = int(a2)
        print(b2)
        self.assertEqual(b1, b0 + 1)
        self.assertEqual(b2, b1)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    filepath = '../report/test_view_integral.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestIntegralPage('test_login_view_integral'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'积分系统—登录积分测试用例集合')
    runner.run(suite)
