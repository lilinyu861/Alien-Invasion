from .BasePage import PageElement,PageObject
from variable.base_url import Url


class LoginjumpPage(PageObject):
    email=PageElement(id='inputEmail')
    passwd=PageElement(id='inputPassword')
    btn=PageElement(css='#login-panel2 > form > div > button')

    base_url = Url().base_url
    login_url=base_url+"/login2"
    main_url=base_url+'/user/main'

    contest_url=base_url+'/contest/list'
    competition_url=base_url+'/competition/list'
    user_info_url=base_url+'/user/info'
