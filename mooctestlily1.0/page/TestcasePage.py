from .BasePage import PageElement,PageObject
from variable.base_url import Url


class TestcasePage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    question_bank=PageElement(link_text='题库')
    test_target=PageElement(link_text='测试目标')
    test_case=PageElement(link_text='测试案例')
    new_btn=PageElement(css='#harden-main > div > div > div > div > div.col-md-10 > mt-table > div > div:nth-child(2) > span > a > button')
    subsiteId_app = PageElement(id='subsiteId_app')
    subsiteId_web = PageElement(id='subsiteId_web')
    subsiteId_pc = PageElement(id='subsiteId_pc')
    subsiteId_dev = PageElement(id='subsiteId_dev')
    appName = PageElement(name='appName')
    selectedCategory = PageElement(name='selectedCategory')
    upload_app = PageElement(id='upload_app')
    upload = PageElement(css='#harden-main > div > div > div > div > div.col-md-10 > div > div:nth-child(2) > div:nth-child(2) > target-create-web > div > form > div > div:nth-child(2) > div.x_content > div > div:nth-child(2) > button')
    description = PageElement(name='description')
    create = PageElement(css='#harden-main > div > div > div > div > div.col-md-10 > div > div:nth-child(2) > div:nth-child(2) > target-create-web > div > form > div > div:nth-child(4) > button')

    create_exam = PageElement(css = '#case-lib > div > div > div > div > div:nth-child(3) > div > button')
    paperName = PageElement(id = 'paperName')
    paperDescription = PageElement(id='paperDescription')
    add_case_btn = PageElement(id='add-case-button')
    base_url = Url().base_url
    test_target_url=base_url+'/target/list'
    test_case_url=base_url+'/case/lib'