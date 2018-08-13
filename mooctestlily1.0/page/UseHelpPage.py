# coding=utf-8
from .BasePage import PageObject,PageElement
from variable.base_url import Url


class UseHelpPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    image=PageElement(css='#nav_image > img')
    usehelp = PageElement(link_text=u'使用帮助')
    usehelpleft=PageElement(css='#quick-start > div > ul > li:nth-child(4)')
    student='985404955@qq.com'
    studentpwd='111111'

    platformintroduce=PageElement(xpath=' // *[ @ id = "main-nav"] / li[1] / a')
    platformintroduce1=PageElement(link_text='平台简介')
    points=PageElement(link_text='积分相关')
    teacher_feature=PageElement(link_text='老师功能')
    create_class=PageElement(link_text='创建班级')
    test_target=PageElement(link_text='测试目标')
    create_test=PageElement(link_text='创建试题')
    create_testpage=PageElement(link_text='创建试卷')
    organizing_exam=PageElement(link_text='组织考试')
    scoring_score=PageElement(link_text='阅卷评分')

    student_feature=PageElement(link_text='学生功能')
    join_class=PageElement(link_text='加入班级')
    take_test=PageElement(link_text='参加考试')
    view_score=PageElement(link_text='查看分数')
    become_teacher=PageElement(link_text='成为教师')

    plugin=PageElement(link_text='插件相关')
    developer_plugin=PageElement(link_text='开发者插件')
    mobile_plugin=PageElement(link_text='移动应用插件')
    web_plugin=PageElement(link_text='Web应用插件')
    performance_plugin=PageElement(link_text='性能测试插件')

    contest_guide=PageElement(link_text='大赛指南')
    contest_register=PageElement(link_text='大赛报名')

    mobile_guide=PageElement(link_text='移动应用测试指南')
    mobile_guide_doc_url = u'http://mooctest-site.oss-cn-shanghai.aliyuncs.com/guide/移动应用测试指南.pdf'
    mobile_claim=PageElement(link_text='脚本编写要求')

    developer_guide=PageElement(link_text='开发者测试指南')

    base_url = Url().base_url
    user_help_url=base_url+'/summer-faq'






