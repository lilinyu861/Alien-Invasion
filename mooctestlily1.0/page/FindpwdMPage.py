from .BasePage import PageObject,PageElement
from variable.base_url import Url


class FindpssMPage(PageObject):
    btn1=PageElement(css='#login-panel2 > form > div > div.switch-style > a')
    btn2=PageElement(css='#forget-password > div > div > div.register-style.right-bottom > a')
    mobile=PageElement(id='verifyMobile')
    captcha=PageElement(id='verifyCaptcha')
    btnf=PageElement(css='#forget-password > div > div > div:nth-child(3) > div:nth-child(1) > button')
    send_captcha=PageElement(css='body > div > div > div.ui-pnotify-text')
    btnc=PageElement(css='#forget-password > div > div > div:nth-child(3) > div:nth-child(2) > button')
    newpassword=PageElement(id='password')
    repeatpassword=PageElement(name='repeatpassword')
    btnc1 = PageElement(css='#reset-password > form > div > button')
    reset_success=PageElement(css='body > div > div > div.ui-pnotify-text')
    differ_passwd=PageElement(css='#parsley-id-25 > li')
    wronglen_passwd=PageElement(css='#parsley-id-23 > li')
    phonenum_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    captcha_error=PageElement(css='body > div > div > h4')
    captcha_error1=PageElement(css='body > div > div > div.ui-pnotify-text')
    captcha_error2=PageElement(xpath='/html/body/div/div/div[4]')

    wrong_mobile_number='153122'
    new_password='123123123'
    differ_new_password='12312222'
    reset_new_password='abc123'
    short_password='12'
    long_password='1234567899876543211'
    right_captcha='summer'
    wrong_captcha='1'

    send_success_content='发送成功'
    reset_success_content='重置成功，即将跳转'
    differ_passwd_content='输入值不同'
    wronglen_passwd_content='字符长度应该在6到16之间'
    phonenum_error_content='请输入一个有效的手机号'
    captcha_error_content='错误'
    captcha_error1_content= 'Invalid mobile captcha'
    reset_password_content='重置密码'

    base_url = Url().base_url
    forget_password_url=base_url+'/forgetPassword'
    reset_password_url=base_url+'/password/reset/WFUxckt3N1JrdHVheHIrblRLK2JUKzQrUEdiSmZDSEc2QzhYY1hnS3BZdz0%3D'



