import HTMLTestRunner
import time
import unittest

from page.ToolDownloadPage import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from variable.User import *
from variable.base_url import Url


class TestToolDownloadPage(unittest.TestCase):

    def setUp(self):
        user = User().user_stu
        base_url = Url().base_url
        self.driver = webdriver.Chrome()
        self.page = ToolDownloadPage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        self.driver.maximize_window()

    # 点击工具下载，进入工具下载模块
    def test_download_tools_page(self):
        self.page.tools_download.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url,self.page.tools_download_url)

    # 逐一点击下载链接，进入对应的工具下载界面
    def test_download_tools(self):
        self.page.tools_download.click()
        ele = self.page.juint_tool
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.mooctest_plugin.click()
        time.sleep(10)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.win64_eclipse.click()
        time.sleep(10)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.mac_eclipse.click()
        time.sleep(10)
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.linux_eclipse.click()
        time.sleep(10)

        ele = self.page.selenium_tool
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.selenium.click()
        time.sleep(10)

        ele = self.page.jmeter_tool
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.jmeter.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    filepath = '../report/test_tool_download.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestToolDownloadPage('test_download_tools_page'))
    suite.addTest(TestToolDownloadPage('test_download_tools'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'工具下载模块测试用例集')
    runner.run(suite)