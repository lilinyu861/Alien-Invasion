import HTMLTestRunner
import time
import unittest

from page.ModifyInfoPage import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from variable.User import *
from variable.base_url import Url


class TestModifyInfoPage(unittest.TestCase):
    def setUp(self):
        base_url = Url().base_url
        user = User().user_stu
        self.driver = webdriver.Chrome()
        self.page = ModifyInfoPage(self.driver, root_uri=base_url)
        self.page.get('/login2')
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()

    # 点击用户名，点击个人信息，进入个人信息修改界面
    def test_modify_user_info(self):
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, self.page.user_info_url)

    # 更改姓名成功
    def test_modify_username_success(self):
        user = User().user_stu
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        self.page.modifyName.click()
        self.page.newName.clear()
        self.page.newName=user['username']+'1'
        self.page.confirmName.click()
        time.sleep(2)
        self.assertEqual(self.page.userName.text, user['username']+'1')
        # 改回原名
        time.sleep(2)
        self.page.modifyName.click()
        self.page.newName.clear()
        self.page.newName = user['username']
        self.page.confirmName.click()
        time.sleep(2)
        self.assertEqual(self.page.userName.text, user['username'])

    # 更改姓名取消
    def test_modify_username_cancel(self):
        user = User().user_modify_new
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        oldname = self.page.userName.text
        self.page.modifyName.click()
        self.page.newName = user['username']+'1'
        self.page.cancelName.click()
        time.sleep(2)
        self.assertEqual(self.page.userName.text, oldname)

    # 更改学校成功
    def test_modify_school_success(self):
        user = User().user_stu
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        self.page.modifySchool.click()
        s1 = Select(self.page.province)
        s1.select_by_index(1)
        s2 = Select(self.page.city)
        s2.select_by_index(1)
        s3 = Select(self.page.newSchool)
        s3.select_by_index(1)
        self.page.confirmSchool.click()
        time.sleep(2)
        self.assertEqual(self.page.userSchool.text, '北京大学')

        # 改回原来学校成功
        time.sleep(2)
        self.page.modifySchool.click()
        s1 = Select(self.page.province)
        s1.select_by_index(10)
        s2 = Select(self.page.city)
        s2.select_by_index(1)
        s3 = Select(self.page.newSchool)
        s3.select_by_index(1)
        self.page.confirmSchool.click()
        time.sleep(2)
        self.assertEqual(self.page.userSchool.text, user['school'])

    # 修改学校取消
    def test_modify_school_cancel(self):
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        oldSchool=self.page.userSchool.text
        self.page.modifySchool.click()
        s1 = Select(self.page.province)
        s1.select_by_index(1)
        s2 = Select(self.page.city)
        s2.select_by_index(1)
        s3 = Select(self.page.newSchool)
        s3.select_by_index(1)
        self.page.cancelSchool.click()
        time.sleep(2)
        self.assertEqual(self.page.userSchool.text, oldSchool)

    # 成功修改手机号
    def test_modify_mobile_success(self):
        user = User().user_stu
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        self.page.modifyMobile.click()
        self.page.newMobile = user['new_phone']
        self.page.sendMobileCapatcha.click()
        time.sleep(2)
        self.page.mobileCaptcha=self.page.right_captcha
        self.page.confirmMobile.click()
        time.sleep(2)
        self.assertEqual(self.page.userMobile.text, user['new_phone'])
        # 成功修改为原来手机号
        time.sleep(2)
        self.page.modifyMobile.click()
        self.page.newMobile = user['phone']
        # self.page.sendMobileCapatcha.click()
        time.sleep(2)
        self.page.mobileCaptcha = self.page.right_captcha
        self.page.confirmMobile.click()
        time.sleep(2)
        self.assertEqual(self.page.userMobile.text, user['phone'])
        
    # 取消修改手机号
    def test_modify_mobile_cancel(self):
        user = User().user_stu
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        usermobile = self.page.userMobile.text
        self.page.modifyMobile.click()
        self.page.newMobile = user['new_phone']
        self.page.sendMobileCapatcha.click()
        time.sleep(2)
        self.page.mobileCaptcha =self.page.right_captcha
        self.page.cancelMobile.click()
        self.assertEqual(self.page.userMobile.text,usermobile)

    # 输入错误格式手机号
    def test_wrong_mobile_format(self):
        user = User().user_stu
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        self.page.modifyMobile.click()
        self.page.newMobile = user['phone']+'1'
        self.page.sendMobileCapatcha.click()
        time.sleep(1)
        self.assertEqual(self.page.mobile_error.text, self.page.mobile_error_content)

    # 输入错误的验证码
    def test_wrong_captcha(self):
        user = User().user_stu
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(1)
        self.page.modifyMobile.click()
        self.page.newMobile = user['new_phone']
        self.page.mobileCaptcha=self.page.wrong_captcha
        self.page.confirmMobile.click()
        time.sleep(1)
        self.assertEqual(self.page.mobile_error.text, self.page.captcha_error_content)

        '''
        #上传附件这里测试用例写的很不清楚
        #第一次上传附件
        self.page.photo1.click()
        self.page.photo1='D:\mooctest\\file\\4.jpg'
        '''

    # 修改头像成功2.jpg,3.jpg,4.jpg均符合要求,修改头像为4.jpg
    def test_modify_avatar_success(self):
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.page.info.click()
        time.sleep(2)
        self.page.updateImage.click()
        time.sleep(2)
        self.page.imageFile = '../file/4.jpg'
        time.sleep(1)
        self.assertEqual(self.page.updateimage_success.text, self.page.modify_image_success_content)

    # 修改头像成功2.jpg,3.jpg,4.jpg均符合要求，修改头像为3.jpg
        time.sleep(2)
        self.page.updateImage.click()
        self.page.imageFile = '../file/3.jpg'
        time.sleep(1)
        self.assertEqual(self.page.updateimage_success.text, self.page.modify_image_success_content)
        time.sleep(2)

    # 修改头像图片超过200K
    def test_large_avatar(self):
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(2)
        self.page.updateImage.click()
        self.page.imageFile='../file/3.jpg'
        time.sleep(1)
        self.assertEqual(self.page.image_big.text,self.page.image_big_error_content)
        self.assertEqual(self.page.image_error.text,self.page.image_error_content)

    # 修改头像上传文件错误
    def test_wrong_avatar_file(self):
        self.driver.maximize_window()
        ele = self.page.image
        ActionChains(self.driver).move_to_element(ele).perform()
        self.page.info.click()
        time.sleep(2)
        self.page.updateImage.click()
        self.page.imageFile = '../file/1.txt'
        time.sleep(1)
        self.assertEqual(self.page.image_big.text, self.page.image_format_error_content)
        self.assertEqual(self.page.image_error.text, self.page.image_error_content)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    filepath = '../report/test_modify_user_info_page.html'
    ftp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestModifyInfoPage('test_modify_user_info'))
    suite.addTest(TestModifyInfoPage('test_modify_username_cancel'))
    suite.addTest(TestModifyInfoPage('test_modify_username_success'))
    suite.addTest(TestModifyInfoPage('test_modify_school_cancel'))
    suite.addTest(TestModifyInfoPage('test_modify_school_success'))
    suite.addTest(TestModifyInfoPage('test_wrong_mobile_format'))
    suite.addTest(TestModifyInfoPage('test_wrong_captcha'))
    suite.addTest(TestModifyInfoPage('test_modify_mobile_success'))
    suite.addTest(TestModifyInfoPage('test_large_avatar'))
    suite.addTest(TestModifyInfoPage('test_wrong_avatar_file'))
    suite.addTest(TestModifyInfoPage('test_modify_avatar_success'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=ftp, title=u'修改个人信息模块测试用例集')
    runner.run(suite)
