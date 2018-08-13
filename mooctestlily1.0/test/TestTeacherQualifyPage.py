import HTMLTestRunner
import time
import unittest

from page.TeacherQualifyPage import *
from selenium import webdriver
from variable.User import *
from variable.base_url import Url


class TestTeacherQualify(unittest.TestCase):

    def setUp(self):
        base_url = Url().base_url
        user = User().user_tea
        self.driver = webdriver.Chrome()
        self.page = TeacherQualifyPage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        time.sleep(2)

    # 点击首页左侧导航栏成为教师，进入教师资格帮助界面
    def test_become_teacher(self):
        self.page.becometeacher.click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, self.page.become_teacher_url)

    # 进入教师帮助界面，点击‘教师资格认证’，下载教师资格认证文件
    def test_teacherQulify(self):
        self.page.becometeacher.click()
        time.sleep(2)
        self.page.teacherQualify.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    filepath = '../report/test_teacher_qualify_page.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestTeacherQualify('test_become_teacher'))
    suite.addTest(TestTeacherQualify('test_teacherQulify'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'教师资格模块测试用例')
    runner.run(suite)
