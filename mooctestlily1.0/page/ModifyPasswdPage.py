from .BasePage import PageObject,PageElement
from variable.base_url import Url


class ModifyPasswdPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    image=PageElement(css='#nav_image > img')
    modifyPasswd=PageElement(link_text=u'修改密码')
    # 修改密码
    modifyPassword=PageElement(id='modifyPassword')
    oldPassword=PageElement(id='oldPassword')
    newPassword=PageElement(id='newPassword')
    repeatPassword=PageElement(id='repeatPassword')
    passwordCaptcha=PageElement(id='passwordCaptcha')
    confirmPassword=PageElement(id='confirmPassword')
    cancelPassword=PageElement(id='cancelPassword')
    oldpassword_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    pwdlen_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    differpwd_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    modifypasswd_success=PageElement(css='body > div > div > div.ui-pnotify-text')


    user_emial='modifypwd@qq.com'
    user_password='12345678'
    wrong_old_password='12332112'
    wrong_old_password_content='两次密码不一致'

    new_short_password='1'
    new_long_password='123456789123456789'
    password_length_error_content='密码长度请在6位与16位之间'

    null_old_password=''
    null_old_password_content= '请输入旧密码'

    new_password='111111'
    differ_new_password='11112112'
    differ_password_content='两次密码不一致'

    wrong_captcha='1'
    captcha_error_content='验证码错误'

    right_captcha='summer'

    base_url = Url().base_url
    user_info_url=base_url+'/user/info'
    login_url=base_url+'/login2'

