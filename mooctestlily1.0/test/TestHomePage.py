import time
import unittest
import HTMLTestRunner

from page.HomePage import *
from selenium import webdriver
from variable.User import *
from variable.base_url import Url


class TestHomePage(unittest.TestCase):
    def setUp(self):
        user = User().user_stu
        base_url = Url().base_url
        self.driver = webdriver.Chrome()
        self.page = HomePage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        self.driver.maximize_window()

    # 点击首页，进入慕测平台首页
    def test_click_homepage(self):
        self.page.homepage.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.user_main_url)

    # 点击左上角mooctest图标，进入慕测平台首页
    def test_click_mooctest_image(self):
        self.page.mooctest_image.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.user_main_url)

    # 逐一点击首页“新闻列表”下的新闻，弹出对应新闻网页
    def test_news_list(self):
        self.page.news1.click()
        time.sleep(2)
        self.assertIn(self.page.news_content,self.driver.page_source)
        # 获取页面句柄
        homepage_handle=self.driver.current_window_handle
        self.driver.switch_to_window(homepage_handle)
        time.sleep(2)
        self.page.news2.click()
        time.sleep(2)
        self.assertIn(self.page.news_content,self.driver.page_source)
        homepage_handle = self.driver.current_window_handle
        self.driver.switch_to_window(homepage_handle)
        time.sleep(2)
        self.page.news3.click()
        time.sleep(2)
        self.assertIn(self.page.news_content,self.driver.page_source)
        homepage_handle = self.driver.current_window_handle
        self.driver.switch_to_window(homepage_handle)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    filepath = '../report/test_home_page.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestHomePage('test_click_homepage'))
    suite.addTest(TestHomePage('test_click_mooctest_image'))
    suite.addTest(TestHomePage('test_news_list'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'首页模块测试用例集')
    runner.run(suite)
