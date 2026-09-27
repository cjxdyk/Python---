import os


def welcome():
    print("欢迎使用账户管理程序")
    print("1.用户注册")
    print("2.用户登录")
    print("3.用户注销")
    print("4.修改密码")
    print("5.退出")
    while True:
        option = input("请选择功能\n")
        # 用户注册
        if option == '1':
            register()
        # 用户登录
        elif option == '2':
            login()
        # 注销
        elif option == '3':
            cancel()
        # 修改密码
        elif option == '4':
            modify()
        elif option == '5':
            break


# 将文件中的数据转换为字典
def convert_data():
    info_li = []
    with open('./info.txt', mode='r+', encoding='utf8') as f:
        info_data = f.readlines()
    for i in info_data:
        info_dict = dict()
        # 替换{ 和 } 并去掉空格
        step_one = i.replace('{', '').replace('}', '')
        # 以冒号进行分隔
        step_two = step_one.split(':')
        # 拼接字典
        info_dict["姓名"] = step_two[1].split(',')[0].replace("'", "").strip()
        info_dict["密码"] = step_two[2].replace("'", "").strip()
        # 保存到列表中
        info_li.append(info_dict)
    return info_li


# 注册
def register():
    if os.path.exists('./info.txt') is not True:
        with open('./info.txt', mode='w', encoding='utf8') as f:
            f.write('')
    # 用户名列表
    name_li = []
    info_li = convert_data()
    # 接收注册信息
    person_info = {}
    name = input("请输入注册用户名:\n")
    # 获取用户列列表
    for i in info_li:
        name_li.append(i['姓名'])
    # 判断用户是否存在
    if name in name_li:
        print('用户已注册')
    else:
        password = input("请输入注册密码:\n")
        person_info['姓名'] = name
        person_info['密码'] = password
        # 写入注册信息
        with open('./info.txt', mode='a+', encoding='utf8') as info_data:
            info_data.write(str(person_info) + '\n')


# 登录
def login():
    if os.path.exists('./info.txt') is not True:
        print('当前无数据,请先注册')
    else:
        # 用户名列表
        name_li = []
        info_li = convert_data()
        name = input("请输入登录用户名:\n")
        password = input("请输入登录密码:\n")
        # 获取用户列列表
        for i in info_li:
            name_li.append(i['姓名'])
        # 判断用户是否存在
        if name in name_li:
            # 获取修改用户的索引
            modify_index = name_li.index(name)
            # 判断密码是否正确
            if password == info_li[modify_index]['密码']:
                print('登录成功')
            else:
                print('用户名或密码不正确')
        else:
            print('用户名或密码不正确')


# 注销
def cancel():
    if os.path.exists('./info.txt') is not True:
        print('当前无数据,请先注册')
    else:
        cancel_name = input("请输入注销的用户\n")
        cancel_password = input("请输入密码\n")
        # 用户名列表
        name_li = []
        info_li = convert_data()
        for i in info_li:
            name_li.append(i['姓名'])
        if cancel_name in name_li:
            # 获取注销用户的索引
            cancel_index = name_li.index(cancel_name)
            # 判断输入的密码是否正确
            if cancel_password == info_li[cancel_index]['密码']:
                info_li.pop(cancel_index)
                # 写入空数据
                with open('./info.txt', mode='w+', encoding='utf8') as f:
                    f.write('')
                for i in info_li:
                    with open('./info.txt', mode='a+', encoding='utf8') as info_data:
                        info_data.write(str(i) + '\n')
                print('用户注销成功')
            else:
                print('用户名或密码不正确')
        else:
            print('注销的用户不存在')


# 修改密码
def modify():
    if os.path.exists('./info.txt') is not True:
        print('当前无数据,请先注册')
    else:
        # 用户名列表
        name_li = []
        info_li = convert_data()
        modify_name = input("请输入用户名:\n")
        password = input("请输入旧密码:\n")
        # 获取用户列列表
        for i in info_li:
            name_li.append(i['姓名'])
        # 判断用户是否存在
        if modify_name in name_li:
            # 获取修改密码用户的索引
            modify_index = name_li.index(modify_name)
            # 判断密码是否正确
            if password == info_li[modify_index]['密码']:
                # 修改密码
                new_password = input("请输入新密码\n")
                info_li[modify_index]['密码'] = new_password
                with open('./info.txt', mode='w+', encoding='utf8') as f:
                    f.write('')
                for i in info_li:
                    with open('./info.txt', mode='a+', encoding='utf8') as info_data:
                        info_data.write(str(i) + '\n')
            else:
                print("用户名或密码不正确")
        else:
            print("用户名或密码不正确")


if __name__ == '__main__':
    welcome()
