# login页面需要输入的变狼
class User():
# mooctest
    # 有完整信息的学生用户
    user_stu = {
        'email': '2386712083@qq.com',
        'passwd': 'abc123',
        'username': 'wyf',
        'phone': '15651620791',
        'role': '学生',
    }
    # 有完整信息的老师用户
    user_tea = {
        'email': '123@123.com',
        'passwd': '111111',
        'username': 'test',
        'phone': '18626421831',
        'role': '老师',
    }
    # 列表为方便登录以老师和学生身份各登陆一次
    users = [user_stu, user_tea]

    # 密码错误的用户
    user_wrong_pwd={
        'email': '2386712083@qq.com',
        'passwd': 'abc1234',
    }
    # 尚未注册的用户
    user_no_register={
        'email': '1234556@123.com',
        'passwd': 'abc123',
    }
    # 信息不完整的用户
    user_uncomlete_info={
        'email': 'abc@123.com',
        'passwd': 'abc123',
        'username': 'test',
        'phone': '',
        'role': '学生',
    }


# QQMail
    qq_user={
        'email':'2386712083@qq.com',
        'passwd': 'abcd1234',
    }

    general={
        'vcode':"summer",
    }