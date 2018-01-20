# DjangoBlog

基于`python3.5`和`Django2.0`的博客。   


## 主要功能：
- 文章，页面，分类目录，标签的添加，删除，编辑等。文章及页面支持`Markdown`，支持代码高亮。
- 支持文章全文搜索。
- 完整的评论功能，包括发表回复评论，以及评论的邮件提醒，支持`Markdown`。
- 侧边栏功能，最新文章，最多阅读，标签云等。
- 支持Oauth登陆，现已有Google,GitHub,facebook,微博登录。
- 支持`Memcache`缓存，支持缓存自动刷新。
- 简单的SEO功能，新建文章等会自动通知Google和百度。
- 集成了简单的图床功能。
- 集成`django-compressor`，自动压缩`css`，`js`。
- 网站异常邮件提醒，若有未捕捉到的异常会自动发送提醒邮件。
- 集成了微信公众号功能，现在可以使用微信公众号来管理你的vps了。
## 安装
使用pip安装：  
`pip install -Ur requirements.txt`

如果你没有pip，使用如下方式安装：    
OS X / Linux 电脑，终端下执行:  

    curl http://peak.telecommunity.com/dist/ez_setup.py | python
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

windows电脑：  
 下载 http://peak.telecommunity.com/dist/ez_setup.py 和 https://raw.github.com/pypa/pip/master/contrib/get-pip.py 这两个文件，双击运行。  

### 配置
配置都是在`setting.py`中.



`test`目录中的文件都是为了`travis`自动化测试使用的.不用去关注.或者直接使用.这样就可以集成`travis`自动化测试了.

`bin`目录是在`centos`环境中使用`Nginx`+`uwsgin`+`virtualenv`来部署的脚本和`Nginx`配置文件.可以参考我的文章:
http://joejoey.tk/article/2018/1/15/2.html

有详细的部署介绍.

若本地部署后发现静态文件无法加载.请将`settings.py`中的`DEBUG=False`修改为`DEBUG=True`即可.

## 运行

 修改`DjangoBlog/setting.py` 修改数据库配置，如下所示：

     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djangoblog',
            'USER': 'root',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 3306,
        }
    }

### 创建数据库

 终端下执行:

    ./manage.py makemigrations
    ./manage.py migrate
### 创建超级用户

 终端下执行:

    ./manage.py createsuperuser
### 创建测试数据
终端下执行:

    ./manage.py create_testdata
### 收集静态文件
终端下执行:  

    ./manage.py collectstatic --noinput
    ./manage.py compress --force
### 开始运行：
 执行：
 `./manage.py runserver`





 浏览器打开: http://127.0.0.1:8000/  就可以看到效果了。
 可以在这里查看已经搭建好的网站
 http://joejoey.tk/
 
 



**

博客框架

宝塔部署 centos+ nginx + uwsgi + django(python3)环境配置
**

环境需求： Centos 6 x86_64 Python3 搭建库包括可在github上查看https://github.com/JoeJoeyMa/Django2.0-Blog appdirs==1.4.3 bottle==0.12.13 certifi==2017.11.5 chardet==3.0.4 coverage==4.4.2 Django==2.0.1 django-appconf==1.0.2 django-autoslug==1.9.3 django-compressor==2.2 django-debug-toolbar==1.9.1 django-haystack==2.6.1 django-ipware==1.1.6 django-pagedown==1.0.4 django-uuslug==1.1.8 idna==2.6 jieba==0.39 jsonpickle==0.9.5 markdown2==2.3.5 mistune==0.8.3 olefile==0.44 packaging==16.8 Pillow==5.0.0 Pygments==2.2.0 PyMySQL==0.8.0 pyparsing==2.2.0 python-memcached==1.59 python-slugify==1.2.4 pytz==2017.3 rcssmin==1.0.6 requests==2.18.4 rjsmin==1.0.12 six==1.11.0 sqlparse==0.2.4 Unidecode==1.0.22 urllib3==1.22 webencodings==0.5.1 WeRoBot==1.2.0 Whoosh==2.7.4 xmltodict==0.11.0

安装需要所有库(已安装或有省略本步）
pip install -r requirements.txt

2.宝塔安装LNMP 使用宝塔还是方便很多的

Centos安装命令：

yum install -y wget && wget -O install.sh http://download.bt.cn/install/install.sh && sh install.sh

安装完成后登录面板会显示推荐一键安装 enter image description here

虽然官方文档并没有版本要求 但为避免BUG出现 安装错误的版本 我们不用一键安装 直接关闭

点击左边导航栏的软件管理页面 选择安装Nginx 版本使用1.8 enter image description here

等待安装完毕 enter image description here

所有程序安装完成 查看文档下一步

enter image description here

然后就要用到宝塔了 点击导航栏中的 网站 按钮 进入网站管理

点击添加站点 域名总应该知道怎么输入吧 都有提示

先输入域名 再选择目录 enter image description here 点击右边箭头指的地方选择网站根目录 enter image description here 然后项目内找到 settingt.py 文件 点击编辑

域名设置
修改为自己的域名
ALLOWED_HOSTS = [ '.com', 'com', ]

mysql 设置
修改为自己的配置
DATABASES = {

'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'name',   # 数据库名     改成自己刚刚添加站点时创建的  比如我刚刚添加的数据库根据域名自动生成
    'USER': 'user',  # 数据库用户名    连接本地数据库 用户名很随意可以用root也可以用数据库自己的用户名    但是如果使用其他主机的数据库就尽量不要用root
    'PASSWORD': 'pass',  # 数据库密码
    'HOST': '127.0.0.1',  # 如果数据库在本地就不用改    使用其他主机的数据库话改成其他主机的IP
    'PORT': '3306',   # 默认端口  不需要动

}
}

下一步我们回到我们的命令行 开始测试项目是否正常运行

首先自行切换到项目根目录 执行

python manage.py migrate # 通过djang ORM 建立所需数据库表
python manage.py runserver # 测试项目是否运行 如果没有问题 Ctrl + C 退出进程 开始创建管理员帐号 python manage.py createsuperuser 按照提示创建管理员帐号 创建完成后进行下一步

打开宝塔面板进入文件管理 enter image description here 编辑Nginx配置模版 uwsgi.ini

[uwsgi]

variables
projectname = DjangoBlog-master # 项目名字 projectdomain = 'www.joejoey.tk' # 项目域名

config
chdir= /www/wwwroot/joejoey.tk/blog/DjangoBlog-master plungins = python socket = 127.0.0.1:8080 # 运行端口 module = DjangoBlog.wsgi:application master = True vacuum = True

回到站点管理 点击设置 enter image description here enter image description here 里面内容全部删除 然后修改

server { listen 80; server_name joejoey.tk; # 改成你的域名 root /www/wwwroot/joejoey.tk/blog/DjangoBlog-master; # 改成你网站的根目录

#添加如下内容即可防止爬虫
location /media  {
    alias /www/wwwroot/joejoey.tk/blog/DjangoBlog-master/media;  # your Django project's media files - amend as required   模版中的/home/www改成上面创建网站的路径/www/wwwroot
    }

location /static
    {
alias  /www/wwwroot/joejoey.tk/blog/DjangoBlog-master/collectedstatic; #静态文件地址，js/css   模版中的/home/www改成上面创建网站的路径/www/wwwroot
    expires  12h;
    }

location /
    {
include uwsgi_params;
    uwsgi_pass 127.0.0.1:8080;
    }

}
最后运行项目

uwsgi uwsgi.ini
