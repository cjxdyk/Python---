class QuantityError(Exception):
    def __init__(self, err="输入无效"):
        super().__init__(err)


li = []

def shopping():
    all_total = 0
    goods_dict = {"五常大米": 45.00, "五丰河粉": 29.90, "农家大米": 45.00, "纯香香油": 22.90}
    print('名称   价格')
    print('按 q 退出')
    for name, price in goods_dict.items():
        print(f"{name} {price}￥")
    while True:
        # 购物车列表
        cart_dict = {}
        # 商品名称
        goods_name = input("请输入选购的商品名称:\n")
        if goods_name == 'q':
            break
        # 商品数量
        else:
            try:
                goods_num = int(input("请输入选购的数量:\n"))
                cart_dict['名称'] = goods_name
                cart_dict['数量'] = goods_num
                li.append(cart_dict)
                if goods_num < 0:
                    raise QuantityError
            except QuantityError as error:
                print(error)
                print("商品数量默认为 1")
                cart_dict['数量'] = 1
                judge = input("是否修改商品数量:Y or N:\n")
                if judge == 'Y' or judge == 'y':
                    new_goods_num = int(input("请输入商品数量:"))
                    cart_dict['数量'] = new_goods_num
                else:
                    cart_dict['数量'] = 1
    for i in li:
        total = goods_dict[i['名称']] * i['数量']
        all_total += total
    print(f'总消费{all_total}元')


if __name__ == '__main__':
    shopping()
