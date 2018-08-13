import HTMLTestRunner
import time
import unittest

from page.LanguagePage import *
from selenium import webdriver
from variable.User import *
from variable.base_url import Url


class TestCompetitionWebPage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        user = User().user_stu
        self.driver = webdriver.Chrome()
        self.page = LanguagePage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        self.driver.maximize_window()

    # 点击右上角“EN"标识，网站文字变为英文，“EN”标识变为“中”
    def test_click_EN_click_Chinese(self):
        self.page.EN_image.click()
        time.sleep(2)
        self.assertIn('Home',self.driver.page_source)
        en_image=self.page.EN_image.get_attribute("src")
        self.assertEqual(en_image,self.page.click_en_src)
        self.page.Chinese_image.click()
        time.sleep(2)
        self.assertIn('首页',self.driver.page_source)
        en_image = self.page.Chinese_image.get_attribute("src")
        self.assertEqual(en_image, self.page.click_chi_src)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    filepath = '../report/test_language.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestCompetitionWebPage('test_click_EN_click_Chinese'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'语言切换模块测试用例集')
    runner.run(suite)
