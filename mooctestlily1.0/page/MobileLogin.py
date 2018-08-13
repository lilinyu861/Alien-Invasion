from .BasePage import PageObject,PageElement


class MobileLogin(PageObject):
    btnm=PageElement(css='#login-panel2 > form > div > div.register-style.right-bottom > a')
    mobile=PageElement(id='mobile')
    captcha=PageElement(id='captcha')
    btnf=PageElement(css='#login-panel2 > form > div > div:nth-child(5) > div:nth-child(1) > button')
    btn=PageElement(css='#login-panel2 > form > div > div:nth-child(5) > div:nth-child(2) > button')
    mobile_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    captcha_error=PageElement(css='body > div > div > div.ui-pnotify-text')
    send_success=PageElement(css='body > div > div > div.ui-pnotify-text')

    mobile_number='18626421831'
    wrong_number='1221'
    captcha_send_success_content= '发送成功'
    mobile_error_content='请输入一个有效的手机号'
    captcha_error_content='验证码错误。'
    wrong_captcha='1'
