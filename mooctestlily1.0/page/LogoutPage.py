from .BasePage import PageObject,PageElement
from  variable.base_url import Url


class LogoutPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    image=PageElement(css='#nav_image > img')
    logout = PageElement(link_text=u'退出登录')

    base_url = Url().base_url
    login_url=base_url+'/login2'

