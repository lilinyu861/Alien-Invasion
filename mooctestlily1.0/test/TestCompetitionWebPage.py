import time
import unittest
import HTMLTestRunner

from selenium import webdriver
from variable.User import *
from page.CompetitionWebPage import *
from variable.base_url import Url


class TestCompetitionWebPage(unittest.TestCase):
    def setUp(self):
        user = User().user_stu
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        base_url = Url().base_url
        self.page = CompetitionWebPage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(2)

    # 点击大赛官网，进入大赛官网
    def test_click_competition_official_website(self):
        self.page.Official_web.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.competition_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    filepath = '../report/test_competition_website.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestCompetitionWebPage('test_click_competition_official_website'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'大赛官网模块测试集')
    runner.run(suite)
