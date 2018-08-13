from .BasePage import PageObject,PageElement
from variable.base_url import Url

class HomePage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    image=PageElement(css='#nav_image > img')
    homepage = PageElement(link_text=u'首页')
    mooctest_image=PageElement(id='logo-left')
    news1=PageElement(css='#harden-main > div > div > div > div:nth-child(1) > div:nth-child(2) > ul > li:nth-child(2) > td.col-md-8 > a')
    news2=PageElement(css='#harden-main > div > div > div > div:nth-child(1) > div:nth-child(2) > ul > li:nth-child(3) > td.col-md-8 > a')
    news3=PageElement(css='#harden-main > div > div > div > div:nth-child(1) > div:nth-child(2) > ul > li:nth-child(4) > td.col-md-8 > a')

    news_content='慕测新闻站'

    base_url = Url().base_url
    user_main_url=base_url+'/user/main'


