# PythonDataMining [在线浏览 [ 推荐 ]](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/tree/master/)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FLinXueyuanStdio%2FPythonDataMining.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FLinXueyuanStdio%2FPythonDataMining?ref=badge_shield)


在学院的书架上发现了一本不带脑子就能看懂的书《Python数据挖掘与实战》

- pdf 在当前目录`./`下，有 [黑白图中文版](https://github.com/LinXueyuanStdio/PythonDataMining/blob/master/Python%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%E5%85%A5%E9%97%A8%E4%B8%8E%E5%AE%9E%E8%B7%B5.pdf) 和 [彩色图表补充](https://github.com/LinXueyuanStdio/PythonDataMining/blob/master/Python%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%E5%85%A5%E9%97%A8%E4%B8%8E%E5%AE%9E%E8%B7%B5_%E5%BD%A9%E5%9B%BE.pdf)
  - pdf 体积略大(8.8Mb)，github 直接打开比较慢，建议`clone`或`fork`

- 随书附带的代码在`./BOOK_CODE`文件夹下面，全英文
  - 原书有些数据集不包含在内，因为这些数据需要从其他网站上下载，而网站已经更新，书编写时的数据很难再找到
  - 有些数据还要翻墙才拿得到，比如第六章”使用朴素贝叶斯进行社交媒体挖掘”时，数据集需要通过`twitter`的`API`来获取，要在代码里翻墙
  - 我根据书中的需要，一个一个重新把数据集找到，放到`./data`目录下（包括书编写时的数据、需要翻墙的数据）

- 阅读笔记在当前目录`./`下，这是在随书附带的代码的基础上做的中文版
- 最后，厚着脸皮要 star ，嘤嘤嘤~~


## 本地浏览

环境：python3.x, jupyter notebook

```sh
pip install notebook # 安装笔记本
jupyter notebook # 启动笔记本
```


## 笔记目录

1. [数据挖掘流程简单示例10min.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/0.%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%E6%B5%81%E7%A8%8B%E7%AE%80%E5%8D%95%E7%A4%BA%E4%BE%8B10min.ipynb)
2. [用近邻算法分类.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/1.%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E5%88%86%E7%B1%BB.ipynb)
3. [用决策树预测获胜球队.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/2.%E5%86%B3%E7%AD%96%E6%A0%91%E9%A2%84%E6%B5%8B%E8%8E%B7%E8%83%9C%E7%90%83%E9%98%9F.ipynb)
4. [用亲和性分析推荐电影.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/3.%E4%BA%B2%E5%92%8C%E6%80%A7%E5%88%86%E6%9E%90%E6%8E%A8%E8%8D%90%E7%94%B5%E5%BD%B1.ipynb)
5. [用转换器抽取特征.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/4.%E7%94%A8%E8%BD%AC%E6%8D%A2%E5%99%A8%E6%8A%BD%E5%8F%96%E7%89%B9%E5%BE%81.ipynb)
6. [用朴素贝叶斯进行社会媒体挖掘.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/5.%E6%9C%B4%E7%B4%A0%E8%B4%9D%E5%8F%B6%E6%96%AF%E8%BF%9B%E8%A1%8C%E7%A4%BE%E4%BC%9A%E5%AA%92%E4%BD%93%E6%8C%96%E6%8E%98.ipynb)
7. [用图挖掘找到感兴趣的人.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/6.%E7%94%A8%E5%9B%BE%E6%8C%96%E6%8E%98%E6%89%BE%E5%88%B0%E6%84%9F%E5%85%B4%E8%B6%A3%E7%9A%84%E4%BA%BA.ipynb)
8. [用神经网络破解验证码.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/7.%E7%94%A8%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E7%A0%B4%E8%A7%A3%E9%AA%8C%E8%AF%81%E7%A0%81.ipynb)
9. [作者归属问题.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/8.%E4%BD%9C%E8%80%85%E5%BD%92%E5%B1%9E%E9%97%AE%E9%A2%98.ipynb)
10. [新闻语料分类.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/9.%E6%96%B0%E9%97%BB%E8%AF%AD%E6%96%99%E5%88%86%E7%B1%BB.ipynb)
11. [用深度学习进行图象分类.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/10.%E7%94%A8%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E8%BF%9B%E8%A1%8C%E5%9B%BE%E8%B1%A1%E5%88%86%E7%B1%BB.ipynb)
12. [大数据处理.ipynb](http://nbviewer.jupyter.org/github/LinXueyuanStdio/PythonDataMining/blob/master/11.%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86.ipynb)

## 问题解决记录

0. [Python Tweepy 翻墙抓取Twitter信息](https://linxueyuanstdio.github.io/2017/10/13/2017-10-11-python-proxy/)







## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FLinXueyuanStdio%2FPythonDataMining.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FLinXueyuanStdio%2FPythonDataMining?ref=badge_large)
