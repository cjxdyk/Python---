
#此为一个空列表，后续可生成新列表
stu_info=[]

#print_menu()作用不大
def print_menu():
    print('='*30)
    print('学生管理系统 V10.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询所有学生信息')
    print('0.退出系统')
    print('='*30)

#add_stu_info()负责增加学生信息
def add_stu_info():
    new_name=input('请输入新学生的姓名：')
    new_sex=input('请输入新学生的性别：')
    new_phone=input('请输入新学生的手机号码：')
    #此处是生成一个新字典
    new_info=dict()
    new_info['name']=new_name
    new_info['sex']=new_sex
    new_info['phone']=new_phone
    #{'name': '张三', 'sex': '男', 'phone': '13536133391'}依次类推，生成一对对键值对
   
    stu_info.append(new_info)
    #[{'name': '张三', 'sex': '男', 'phone': '13536133391'}]依此类推，字典作为列表里的一个元素



#del_stu_info()负责删除学生信息，要将student参数上传

def del_stu_info(student):
    del_num=int(input('请输入要删除的序号：'))
    #**************student要为一个列表，方可被删除****************
    del student[del_num-1]
    print('删除成功！')
    



#modify_stu_info()负责修改学生信息，****应该后面调用******
def modify_stu_info():
    if len(stu_info)!=0:
        
        stu_id=int(input('请输入要修改的学生序号：'))
        new_name=input('请输入要修改的学生姓名：')
        new_sex=input('请输入要修改学生的性别：（男/女）')
        new_phone=input('请输入要修改学生的手机号码：')

        #按照逻辑，应该是0,1,2，将列表里面的元素即字典修改
        stu_info[stu_id-1]['name']=new_name
        stu_info[stu_id-1]['sex']=new_sex
        stu_info[stu_id-1]['phone']=new_phone

        
    else:
        print('学生信息表为空')


#show_stu_info()负责显示学生信息，只是输出结果影响不大



def show_stu_info():
    print('学生信息如下：')
    print('='*30)
    print('序号 姓名 性别 手机号码')
    i=1
    #遍历吧stu_info列表的字典元素取出来
    for tempInfo in stu_info:
        #print(tempInfo['name'])
        #print(f'{i},{tempInfo['name']},{tempInfo['sex']},{tempInfo['phone']}')
        print("%d %s %s %s"%(i,tempInfo['name'],tempInfo['sex'],tempInfo['phone']))
        i+=1
        

   
def main():
    while True:
        print_menu()
        key=input('请输入功能对应的数字：')
        #添加
        if key=='1':
            add_stu_info()

        #删除，传参是stu_info列表
        elif key=='2':
            del_stu_info(stu_info)

        #修改
        elif key=='3':
            modify_stu_info()

        #显示
        elif key=='4':
            show_stu_info()

        #退出
        elif key=='0':
            quit_confirm=input('亲，真的要退出吗？（Yes or No）:').lower()
            if quit_confirm=='yes':
                print('学习使用')
                break
            elif quit_confirm=='no':
                continue
            else:
                print('输入有误！')
if __name__ == '__main__':
    main()


