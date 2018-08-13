from .BasePage import PageObject,PageElement
from variable.base_url import Url


class LanguagePage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    EN_image=PageElement(css='#navbar > ul > li:nth-child(8) > img')
    Chinese_image=PageElement(css='#navbar > ul > li:nth-child(8) > img')

    base_url = Url().base_url
    click_en_src=base_url+'/assets/img/hover-chicon.png'
    click_chi_src=base_url+'/assets/img/hover-enicon.png'

