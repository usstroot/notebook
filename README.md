## 欢迎来到 Cloud Studio

我们在 Machine Learing 环境中为您预先安装了 IPython、jupyter、ggplot、pandas、
tensorflow、scikit-learn，您可以方便地在您的专用小主机中使用它们。

下面以 ggplot+jupyter 的使用为例，简单介绍一下环境的使用。


## 1.切换环境
首先，请您将运行环境切换为 Machine Learning 环境。

![图片](https://dn-coding-net-production-pp.qbox.me/80e34fa3-90b1-407e-b9be-9482ec69e84f.png)

## 2.启动 jupyter
打开 terminal，由于 pandas 库问题。需要先运行 `sudo sed -i 's/pandas.lib/pandas/g' /usr/local/lib/python3.5/dist-packages/ggplot/stats/smoothers.py` , 然后在 terminal 中运行 `jupyter notebook --ip=0.0.0.0` 来启动 jupyter。
运行成功后，Terminal 中可以查看 token。

## 3.创建访问链接
将端口号设置为 `8888`, 点击【+】生成访问链接。
![图片](https://dn-coding-net-production-pp.qbox.me/b461af40-5a0d-4761-8254-55fb3969c43d.png)

## 4.登录 jupyter
打开访问链接，使用步骤 2 中的 token 登录 jupyter。

![图片](https://dn-coding-net-production-pp.qbox.me/e2b14eb1-9cfe-4a85-8aae-dd8fdee44b07.png)

## 5. 创建 Notebook

创建 Python3 Notebook。
![图片](https://dn-coding-net-production-pp.qbox.me/51400f8c-89b1-4fd1-b2da-50f58479dae7.png)

## 6.开始使用
输入框中输入代码，在上方点击运行，就可以开始使用啦。下面以导入数据及画图举例。

6.1 准备数据。
![图片](https://dn-coding-net-production-pp.qbox.me/2e3fb676-f1d8-4110-bb20-7fd0d7de8b2e.png)

```
import ggplot as gp 
import pandas as pd
meat = gp.meat
```
6.2 画图，此处以散点图为例。

![图片](https://dn-coding-net-production-pp.qbox.me/6e3f54f9-bfae-4bfd-baa8-7c266620af33.png)

```
p=gp.ggplot(gp.aes(x='date',y='beef'),data=meat)+gp.geom_point(color='red')+gp.ggtitle(u'散点图')
print (p)
```

_**注：您也可以在操作完第 4 步登录 Jupyter 之后，直接在【File】中打开我们的示例文件 MLDemo.ipynb 并运行。**_

Happy Coding！

![logo](https://dn-coding-net-production-pp.qbox.me/0905c8a9-5b33-4819-83d4-3cd0528b0c86.png)
