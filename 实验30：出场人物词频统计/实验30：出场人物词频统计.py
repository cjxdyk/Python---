#《三国演义》词频统计案例
import jieba
from bs4 import BeautifulSoup
import requests
import pandas as pd
from matplotlib import pyplot as plt

excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议","如何","主公","军士", "左右","军马","引兵","次日","大喜","天下","东吴","于是","今日","不敢","魏兵", "陛下","一人","都督","人马","不知","汉中","只见","众将","后主","蜀兵","上马", "大叫","太守","此人","夫人","先主","后人","背后","城中","天子","一面","何不", "大军","忽报","先生","百姓","何故","然后","先锋","不如","赶来","原来","令人", "江东","下马","喊声","正是","徐州","忽然","因此","成都","不见","未知","大败", "大事","之后","一军","引军","起兵","军中","接应","进兵","大惊","可以","以为", "大怒","不得","心中","下文","一声","追赶","粮草","曹兵","一齐","分解","回报", "分付","只得","出马","三千","大将","许都","随后","报知","前面","之兵","且说", "众官","洛阳","领兵","何人","星夜","精兵","城上","之计","不肯","相见","其言", "一日","而行","文武","襄阳","准备","若何","出战","亲自","必有","此事","军师","之中","伏兵","祁山","乘势","忽见","大笑","樊城","兄弟","首级","立于","西川","朝廷","三军","大王","传令","当先","五百","一彪","坚守","此时","之间","投降","五千","埋伏","长安","三路","遣使","英雄"}

txt = open("桃园结义.txt","r",encoding='utf8').read()
words = list(jieba.cut(txt))


counts = {}


for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1



#for word in excludes:
#        del counts[word]


for word in excludes:
    counts.pop(word, None)
print(counts)


items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

name=[]
times=[]
for i in range(30):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
    name.append(word)
    times.append(count)

print(name)
print(times)

id=[]
for i in range(1,31):
    id.append(i)

df = pd.DataFrame({
    'id':id,
    'name':name,
    'times':times,
})
df = df.set_index('id')
print(df)
df.to_excel('桃园结义.xlsx')
print("DONE!")
print('生成文件成功,下一步进行可视化!')

dirpath = '桃园结义.xlsx'
data = pd.read_excel(dirpath,index_col='id',sheet_name='Sheet1')
print('OK!,数据正常加载!')

plt.bar(data.name,data.times,color="#87CEFA")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('三国演义人物名字前三十名出现的次数',fontsize=16)
plt.xlabel('人名')
plt.ylabel('统计次数')
plt.xticks(data.name,rotation=90)
plt.tight_layout()
imgname = '三国.jpg'
plt.savefig(imgname)
plt.show()
print('柱状图生成完毕,程序执行完毕!')

