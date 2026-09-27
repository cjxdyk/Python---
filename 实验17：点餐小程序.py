#all_entrees函数
def all_entrees():
    entrees={"酸菜鱼":68,
             "三杯鸭":98,
             "市师鸡":128,
             "清平鸡":78,
             "均安蒸猪":168,
             "深井烧鹅":108,
             "拆鱼羹":88,
             "顺德鱼生":135
             }
    return entrees
#print(all_entrees().get("顺德鱼生"))


#show_menu函数
def show_menu():
    #函数背调用了一次，键和值
    for x,y in all_entrees().items():
        print(x,":",str(y)+"元")
#total       
def total(entrees_dict):
    count=0
    li1 = list(entrees_dict.keys())
    li2 = list(entrees_dict.values())
    for i,j in zip(li1,li2):
        total_money = all_entrees().get(i)*j
        count+=total_money
    #total_money=all_entrees()[name]*num 
    #count+=total_money
    print("需要支付金额：",count,"元")

#主函数
def main():
    entrees_dict={}
    print("点菜小程序")
    show_menu()
    print("输入q完成下单")
    while True:
        entree_name=input("请输入下单的菜品：")
        if entree_name=='q':
            break
        if entree_name in [e_name for e_name in all_entrees().keys()]:  #增添元素
            entrees_num=input("请输入下单的数量：")
            if entrees_num.isdigit():
                entrees_dict[entree_name]=float(entrees_num)
            else:
                print('商品数量不合法')
        else:
            print('请输入正确的商品名称')
    #print(entrees_dict) #一般来说，字典要转换成列表才能方便计算
    '''
    li1 = list(entrees_dict.keys())
    li2 = list(entrees_dict.values())
    print(entrees_dict.keys(),type(list(entrees_dict.keys())))
    #这是成功的一步
    for i,j in zip(li1,li2):
        print(all_entrees().get(i)*j)
    #print(all_entrees().get(""))
    '''
    total(entrees_dict)
main()



#是重新生成一张列表再计算所花的钱
#生成新的字典没问题，问题可能出在total()函数
