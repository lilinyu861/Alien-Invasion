from .BasePage import PageElement,PageObject
from variable.base_url import Url

class TestTargetPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    question_bank=PageElement(link_text='题库')
    test_target=PageElement(link_text='测试目标')
    test_case=PageElement(link_text='测试案例')
    new_btn=PageElement(css='#harden-main > div > div > div > div > div.col-md-10 > mt-table > div > div:nth-child(2) > span > a > button')
    subsiteId_app=PageElement(id='subsiteId_app')
    subsiteId_web=PageElement(id='subsiteId_web')
    subsiteId_pc=PageElement(id='subsiteId_pc')
    subsiteId_dev=PageElement(id='subsiteId_dev')
    visible=PageElement(name='visible')
    appName=PageElement(name='appName')
    select_class=PageElement(name='selectedCategory')
    upload_app=PageElement(id='upload_app')
    description=PageElement(name='description')
    create_btn=PageElement(css='#harden-main > div > div > div > div > div.col-md-10 > div > div:nth-child(2) > div:nth-child(2) > target-create-kibug > div > form > div > div:nth-child(4) > button')

    description_content=u'这是一个测试'
    app_name='test测试'

    base_url = Url().base_url
    test_target_url=base_url+'/target/list'
    test_case_url=base_url+'/case/lib'
    create_new_test_target_url=base_url+'/target/create'