from .BasePage import PageObject,PageElement
from variable.base_url import Url


class IntegralPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    image=PageElement(css='#nav_image > img')
    user_info = PageElement(link_text=u'个人信息')
    logout=PageElement(link_text='退出登录')
    integral=PageElement(id='integral')

    base_url = Url().base_url
    user_main_url=base_url+'/user/main'


