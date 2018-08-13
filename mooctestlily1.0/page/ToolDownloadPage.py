from .BasePage import PageObject,PageElement
from variable.base_url import Url


class ToolDownloadPage(PageObject):
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
    btn = PageElement(css='#login-panel2 > form > div > button')
    tools_download=PageElement(css='#quick-start > div > ul > li:nth-child(3)')

    juint_tool=PageElement(css='body > sd-app > common > div > download > div > div > div.x_content > div > div:nth-child(1) > div')
    mooctest_plugin=PageElement(link_text='慕测插件')
    win64_eclipse=PageElement(link_text='Win64 含插件Eclipse下载')
    mac_eclipse = PageElement(link_text='Mac 含插件eclipse下载')
    linux_eclipse = PageElement(link_text='Linux 含插件eclipse下载')

    selenium_tool=PageElement(css='body > sd-app > common > div > download > div > div > div.x_content > div > div:nth-child(2) > div')
    selenium = PageElement(link_text='Selenium Jar包下载')

    jmeter_tool=PageElement(css='body > sd-app > common > div > download > div > div > div.x_content > div > div:nth-child(3) > div')
    jmeter=PageElement(link_text='Jmeter插件下载')

    base_url = Url().base_url
    tools_download_url = base_url+'/download'



