# 基于python3+tornado 实现的类似禅道的系统
##  背景：目前市面上有很多bug管理工具，但是各有各的特点，最著名，最流行的就是禅道，一个偶然的机会接触到了python  ，学到tornado后，就想着去怎么去用到实处，后来发现自己公司的除了禅道就记录bug没有什么可以用的工具了。
## 语言：python3 第三库 ：tornado，qiniu(用于云存储文件)，数据库用sqlite
##  why  use tornado？很多人其实会这么问我，我感觉tornado可以实现异步，虽然现在代码还没有用到异步，我感觉还是很不错的框架，值得学习，现在很多公司都在用，个人感觉这是一个不错的，值得我们大家去学习的框架。
## 功能：1.个人中心，2.用例管理 3.bug管理 4.设备管理 5.测试网盘 6.版本记录 7.报告管理 8.用户管理 等，所有的用户都需要登录后才能进行操作，
##  使用说明，需要安装tornado 、xlrd、xlwt、sqlalchemy和qiniu，需要注册七牛账号密码，在untils目录下的shangChuan.py需要填写响应的key才可以上传，文件下载的链接冲七牛下载，预览文件也是来自七牛提供的云存储，下载复制后，运行run.py 即可，
## 主要的功能就是上述，其他功能如下展示：
#  结构：
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E4%B8%BB%E8%A6%81%E7%BB%93%E6%9E%84.png)
# 效果图
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E9%A6%96%E9%A1%B5.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E7%94%A8%E4%BE%8B%E7%AE%A1%E7%90%86.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/用户管理.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E8%AE%BE%E5%A4%87%E7%AE%A1%E7%90%86.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E7%89%88%E6%9C%AC%E8%AE%B0%E5%BD%95.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/bug%E7%AE%A1%E7%90%86.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E6%8A%A5%E5%91%8A%E7%AE%A1%E7%90%86.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E6%B5%8B%E8%AF%95%E7%BD%91%E7%9B%98.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E6%B7%BB%E5%8A%A0bug.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E6%B7%BB%E5%8A%A0%E6%8A%A5%E5%91%8A.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E6%B7%BB%E5%8A%A0%E7%94%A8%E4%BE%8B.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E6%B7%BB%E5%8A%A0%E7%94%A8%E6%88%B7.png)
![Alt text](https://github.com/liwanlei/tornado_guanli/blob/master/img/%E6%B7%BB%E5%8A%A0%E8%AE%BE%E5%A4%87.png)


