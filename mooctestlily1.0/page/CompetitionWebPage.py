from .BasePage import PageObject,PageElement
from variable.base_url import Url


class CompetitionWebPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    Official_web = PageElement(css='#quick-start > div > ul > li:nth-child(1)')

    base_url=Url().base_url
    # competition_url=base_url+'/#/'
    competition_url = 'http://www.mooctest.org/#/'




