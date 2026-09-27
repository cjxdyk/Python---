from pyecharts.charts import Bar
from pyecharts import options as opts

# x轴数据
x_data = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
y_data = [5, 20, 36, 10, 75, 90]

bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("服装", y_data)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="我的第一个图表", subtitle="这里是副标题")
    )
)

bar.render()
