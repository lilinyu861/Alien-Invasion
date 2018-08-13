from .BasePage import PageObject,PageElement
from variable.base_url import Url


class TeacherQualifyPage(PageObject):
    email=PageElement(id='inputEmail')
    passwd=PageElement(id='inputPassword')
    btn=PageElement(css='#login-panel2 > form > div > button')
    teacher = '123@123.com'
    teacherpwd = '111111'
    becometeacher=PageElement(css='#quick-start > div > ul > li:nth-child(6)')
    teacherQualify=PageElement(link_text='教师资格认证')

    base_url = Url().base_url
    become_teacher_url=base_url+'/summer-faq?key=faqBeTeacher'