from .BasePage import PageObject,PageElement
from variable.base_url import Url

class ForumPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    image = PageElement(css='#nav_image > img')
    mooctest_forum = PageElement(link_text=u'慕测论坛')
    left_forum = PageElement(css='#quick-start > div > ul > li:nth-child(2)')
    forum_login = PageElement(link_text='登录')
    username = PageElement(id='username')
    password = PageElement(id='password')
    forum_login_btn = PageElement(id='login')

    base_url = Url().base_url
    forum_url = 'http://forum.mooctest.net/'
    forum_login_url = 'http://api.mooctest.net/login'
    forum_login_error_url = 'http://api.mooctest.net/login?error'




