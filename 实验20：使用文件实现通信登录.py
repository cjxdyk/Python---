import os   #引用 os 模块
import pickle   #应用 pickle 模块

#这段代码用于检测文件存在与否，反之新建
Path = './Person.txt'   #全局变量,这里是通信录物理路径
#判断通信录是否存在,不存在则创建空通信录
if os.path.exists(Path) == False:   #判断通信录是否存在
    f = open((Path),'wb')   #以二进制写模式打开通信录
    temp = {'total':0}   #局部变量,用于计算通信录的人数
    pickle.dump(temp, f)   #将对象 temp 保存到 f 中
    f.close()   #关闭 f
else:
    pass   #空函数


#添加联系人
def add():   #自定义添加函数
    f = open((Path), 'rb')   #以二进制读模式打开通信录
    a = pickle.load(f)   #从 f 中读取信息为数组的形式
    f.close   #关闭 f
    b = 0   #自定义局部变量
    name = input('请输入要添加联系人的姓名:')   #获取输入,这里是姓名
    for key in a.keys():   #循环 key 为自定义,a.keys()为从通信录读出来所有 key
        b += 1   #自定义变量自增
        if key == name and b <= a['total']+1:   #判断,满足条件执行
            print("联系人已存在,添加失败!")
            break   #跳出循环
        if b == a['total'] + 1 and key != name:   #判断,满足条件执行
            number = input('请输入号码:')   #获取输入
            information = {name:number}   #赋值
            a['total'] += 1   # total+1
            a.update(information)   #更新 a 对象
            f = open((Path),'wb')   #以二进制写模式打开通信录
            pickle.dump(a, f)   #把 a 对象写入 f
            f.close()   #关闭 f
            print('添加成功')
            break   #跳出循环



#显示所有联系人
def showall():
    f = open((Path), 'rb')
    a = pickle.load(f)
    print("一共有{}个联系人.".format(a['total']))
    for key in a.keys():
        if key != 'total':
            print("{}:{}".format(key, a[key]))
    f.close()




#退出通信录
def exit():
    exec("quit()")

#查找，此函数是对字符串处理的
def search(name):
    f = open((Path), 'rb')
    a = pickle.load(f)
    b = 0
    for key in a.keys():
        b += 1
        if key == name and b <= a['total']+1:
            print("{}的号码是:{}".format(name, a[key]))
            break
        if b == a['total'] + 1 and key != name:
            print("联系人不存在")
            break



#删除联系人
def delete(name):
    f = open((Path), 'rb')
    a = pickle.load(f)
    f.close()
    b = 0
    for key in a.keys():
        b += 1
        if key == name and b <= a['total']+1:
            a.pop(name)
            a['total'] -= 1
            f = open(Path, 'wb')
            pickle.dump(a, f)
            f.close()
            print("删除成功!")
            break
        if b == a['total'] + 1 and key != name:
            print("联系人不存在!无法删除!")
            break

#修改
def change():
    x = input("请输入所要修改的联系人姓名:")
    f = open((Path), 'rb')
    a = pickle.load(f)
    f.close()
    b = 0
    for key in a.keys():
        b += 1
        if key == x and b <= a['total']+1:
            y = input("请输入修改后的号码:")
            a[key] = y
            f = open(Path, 'wb')
            pickle.dump(a, f)
            f.close()
            print("修改成功!")
            break
        
        if b == a['total'] + 1 and key != name: 
            print("联系人不存在")
            break



#界面
def point():
    print("******************************")
    print("显示提示信息:*")
    print("显示所有联系人:0")
    print("查找联系人:1")
    print("添加联系人:2")
    print("删除联系人:3")
    print("更改联系人资料:4")
    print("退出通信录:5")
    print("******************************")

point()
#主进程
while True:   #循环
    x = int(input("请输入您的选择:"))   #获取输入
    if x == 2:   #判断输入
        add()   #调用添加函数
        continue   #结束本次循环,重新开始下一轮循环
    elif x == 0:
        showall()   #调用显示全部函数
        continue   #结束本次循环,重新开始下一轮循环
    elif x ==5:
        exit()   #调用退出函数
    elif x ==1:
        name = input("请输入所要查找的联系人姓名:")
        search(name)   #调用查找函数,需要传一个参数:姓名
        continue   #结束本次循环,重新开始下一轮循环
    elif x ==3:
        name = input("请输入所要删除的联系人姓名:")
        delete(name)   #调用删除函数,需要传一个参数:姓名
        continue   #结束本次循环,重新开始下一轮循环
    elif x ==4:
        change()   #调用修改函数
        continue   #结束本次循环,重新开始下一轮循环
    elif x == '*':
        point()
    else:
        print("输入选项不存在,请重新输入!")
        break

#很有可能问题出在name上
