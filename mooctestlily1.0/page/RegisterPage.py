from .BasePage import PageObject,PageElement
import random
from variable.base_url import Url

class RegisterPage(PageObject):
    register_now=PageElement(link_text='现在注册')
    userName=PageElement(name='userName')
    email=PageElement(name='email')
    password=PageElement(name='password')
    passwordAgain=PageElement(name='passwordAgain')
    register_btn=PageElement(css='#register2Panel > div > form > button')
    error=PageElement(css='body > div > div > div.ui-pnotify-text')


#register_success
    new_username='testRegister'
    new_email=str(random.randint(1111,999999999))+'@qq.com'
    new_password='12345678'
#email_error
    wrong_email='abcd123'
    email_error_content='请输入有效邮箱'
#had_email
    had_email='985404955@qq.com'
    hademail_error_content='用户已存在'
#differ_password
    differ_password='12121212'
    differ_password_error_content='请保证两次密码一致'
#wrong_username
    username_error_content='请保证姓名在2与16位之间'
    #null_username
    null_username=''
    #too_long_username
    long_username='1234567890qwertyuioplkhgfdsa'
    #too_short_username
    short_username='1'
#wrong_password_length
    password_length_error_content='密码长度请在6位与16位之间'
    #long_password
    long_password='1234567890987654321234'
    #short_password
    short_password='1234'

#url
    base_url = Url().base_url
    register_url=base_url+'/register2'
    user_info_url=base_url+'/user/info'


