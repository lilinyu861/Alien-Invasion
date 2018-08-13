from .BasePage import PageObject,PageElement
from variable.base_url import Url


class LoginPage(PageObject):
    base_url = Url().base_url
    url = base_url+'/login2'

    # login页面元素
    email=PageElement(id='inputEmail')
    passwd=PageElement(id='inputPassword')
    btn=PageElement(css='#login-panel2 > form > div > button')
    form=PageElement(tag_name='form')
    username=PageElement(css='#navbar > ul > li:nth-child(7) > ul > div > div > div')
    passwd_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    email_error=PageElement(css='body > div > div > div.ui-pnotify-text')

    # 提示登录浏览器版本信息
    version_tip=PageElement(css='form > div > p')
    tip_info='为了更好的使用体验，请使用 Chrome 64.0 或 Firefox 56.0及以上版本。'






