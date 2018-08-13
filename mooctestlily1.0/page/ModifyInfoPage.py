from .BasePage import PageObject,PageElement
from  variable.base_url import Url


class ModifyInfoPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    image=PageElement(css='#nav_image > img')
    info=PageElement(link_text=u'个人信息')
    # 修改姓名
    modifyName=PageElement(id='modifyName')
    newName=PageElement(id='newName')
    confirmName=PageElement(id='confirmName')
    userName=PageElement(id='userName')
    cancelName=PageElement(id='cancelName')
    # 修改学校
    modifySchool=PageElement(id='modifySchool')
    province=PageElement(id='province')
    city=PageElement(id='city')
    newSchool=PageElement(id='newSchool')
    confirmSchool=PageElement(id='confirmSchool')
    cancelSchool=PageElement(id='cancelSchool')
    userSchool=PageElement(id='userSchool')
    # 修改手机号
    userMobile=PageElement(id='userMobile')
    modifyMobile=PageElement(id='modifyMobile')
    newMobile=PageElement(id='newMobile')
    sendMobileCapatcha=PageElement(id='sendMobileCapatcha')
    mobileCaptcha=PageElement(id='mobileCaptcha')
    confirmMobile=PageElement(id='confirmMobile')
    cancelMobile=PageElement(id='cancelMobile')
    mobile_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    captcha_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    # 第一次上传附件
    photo1=PageElement(id='photo1')
    # 已上传附件
    hadfile=PageElement(css='#base-info > div > div:nth-child(2) > div > div.col-md-8 > form > div:nth-child(7) > div > div:nth-child(1) > a')
    # 重新上传附件
    reupdate=PageElement(css='#base-info > div > div:nth-child(2) > div > div.col-md-8 > form > div:nth-child(7) > div > div:nth-child(1) > button')
    reupdatefile=PageElement(css='')

    # 修改头像
    updateImage=PageElement(id='updateImage')
    imageFile=PageElement(id='imageFile')
    updateimage_success=PageElement(css='body > div:nth-child(5) > div > div.ui-pnotify-text')
    image_error=PageElement(css='body > div:nth-child(6) > div > div.ui-pnotify-text')
    image_big=PageElement(css='body > div:nth-child(5) > div > div.ui-pnotify-text')
    image_wrong=PageElement(css='body > div:nth-child(5) > div > div.ui-pnotify-text')

    wrong_mobile='12'
    mobile_error_content='请输入一个有效的手机号'
    wrong_captcha='1'
    right_captcha='summer'

    captcha_error_content='验证码错误'
    modify_image_success_content='上传成功'
    image_big_error_content='照片大小不能超过200K'
    image_error_content='请重新上传'
    image_format_error_content='请上传jpg,dmp,png,jpeg格式的照片'

    base_url = Url().base_url
    user_info_url= base_url+'/user/info'



