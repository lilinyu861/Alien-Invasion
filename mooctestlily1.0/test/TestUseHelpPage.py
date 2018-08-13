import HTMLTestRunner
import time
import unittest

from page.UseHelpPage import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from variable.User import *
from variable.base_url import Url


class TestUseHelpPage(unittest.TestCase):
    def setUp(self):
        user = User().user_stu
        base_url = Url().base_url
        self.driver = webdriver.Chrome()
        self.page = UseHelpPage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        self.driver.maximize_window()

    # 点击用户名，点击使用帮助，进入帮助页面  1
    def test_click_username_click_userhelp(self):
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.usehelp.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.user_help_url)

    # 点击首页左侧导航栏“使用帮助”，进入帮助页面
    def test_click__usehelp(self):
        self.page.usehelpleft.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.user_help_url)

    # 逐一点击左侧目录，进入对应的使用帮助
    def test_click_usehelp_list(self):
        self.page.usehelpleft.click()
        time.sleep(2)
        self.page.platformintroduce.click()
        self.page.platformintroduce1.click()
        time.sleep(2)
        self.assertIn('慕测平台是编程类考试和练习的服务平台',self.driver.page_source)
        self.page.points.click()
        time.sleep(2)
        self.assertIn('如何获取积分', self.driver.page_source)
        time.sleep(2)
        self.page.teacher_feature.click()
        self.page.create_class.click()
        time.sleep(2)
        self.assertIn('如何创建一个班级',self.driver.page_source)
        self.page.test_target.click()
        time.sleep(2)
        self.assertIn('如何上传一个测试目标', self.driver.page_source)
        self.page.create_test.click()
        time.sleep(2)
        self.assertIn('如何创建一个试题', self.driver.page_source)
        self.page.create_testpage.click()
        time.sleep(2)
        self.assertIn('如何创建一张试卷', self.driver.page_source)
        self.page.organizing_exam.click()
        time.sleep(2)
        self.assertIn('如何组织一场考试', self.driver.page_source)
        self.page.scoring_score.click()
        time.sleep(2)
        self.assertIn('如何进行一次评分', self.driver.page_source)
        time.sleep(2)
        self.page.student_feature.click()
        self.page.join_class.click()
        time.sleep(2)
        self.assertIn('如何加入一个班级', self.driver.page_source)
        self.page.take_test.click()
        time.sleep(2)
        self.assertIn('如何参加一次考试', self.driver.page_source)
        self.page.view_score.click()
        time.sleep(2)
        self.assertIn('如何查看自己分数', self.driver.page_source)
        self.page.become_teacher.click()
        time.sleep(2)
        self.assertIn('如何成为老师', self.driver.page_source)
        self.page.plugin.click()
        self.page.developer_plugin.click()
        time.sleep(2)
        self.assertIn('如何完成开发者测试', self.driver.page_source)
        self.page.mobile_plugin.click()
        time.sleep(2)
        self.assertIn('如何完成移动应用测试', self.driver.page_source)
        self.page.web_plugin.click()
        time.sleep(2)
        self.assertIn('如何完成Web应用测试', self.driver.page_source)
        self.page.performance_plugin.click()
        time.sleep(2)
        self.assertIn('如何完成性能测试', self.driver.page_source)
        time.sleep(2)
        self.page.contest_guide.click()
        self.page.contest_register.click()
        time.sleep(2)
        self.assertIn('如何报名参加大赛', self.driver.page_source)

    # 点击目录“插件相关”下的“开发者插件”点击“文档链接”
    def test_developer_link(self):
        self.page.usehelpleft.click()
        time.sleep(2)
        self.page.plugin.click()
        time.sleep(1)
        self.page.developer_plugin.click()
        time.sleep(2)
        self.page.developer_guide.click()
        time.sleep(6)

    # 点击目录“插件相关”下的“移动应用插件”点击“文档链接”
    def test_mobile_link1(self):
        self.page.usehelpleft.click()
        time.sleep(2)
        self.page.plugin.click()
        time.sleep(1)
        self.page.mobile_plugin.click()
        time.sleep(2)
        self.page.mobile_guide.click()
        time.sleep(6)

    def test_mobile_link2(self):
        self.page.usehelpleft.click()
        time.sleep(2)
        self.page.plugin.click()
        time.sleep(1)
        self.page.mobile_plugin.click()
        time.sleep(2)
        self.page.mobile_claim.click()
        time.sleep(6)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    filepath = '../report/test_user_help_page.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestUseHelpPage('test_click_username_click_userhelp'))
    suite.addTest(TestUseHelpPage('test_click__usehelp'))
    suite.addTest(TestUseHelpPage('test_click_usehelp_list'))
    suite.addTest(TestUseHelpPage('test_developer_link'))
    suite.addTest(TestUseHelpPage('test_mobile_link1'))
    suite.addTest(TestUseHelpPage('test_mobile_link2'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'使用帮助模块测试用例集')
    runner.run(suite)
