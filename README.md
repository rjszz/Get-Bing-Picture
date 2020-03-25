# python3 脚本获取Bing背景图片

### 功能

部署到Linux服务器，每天自动获取Bing图片存放到服务器



### 环境

Linux

Python3 环境

Python 包环境：requests、bs4 (使用pip3安装)



### 部署步骤：

1. 将`bing.py`上传至服务器，建议放在自己新建的独立文件夹中
2. 对`bing.py`关键之处进行更改：

- 对于第42行的`/home/j/Bing/picture/`，更改为自己存放图片的位置，这里表示图片将存放在``/home/j/Bing/picture`这个文件夹之下

3. 使用`crontab`(一般自带)添加定时任务，步骤如下([crontab教程](https://www.jianshu.com/p/838db0269fd0))：

   输入`crontab -e`，进行任务编辑，键入以下内容

   ```bash
   SHELL=/bin/bash
   PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
   
   00 6 * * * /usr/bin/python3 /home/j/Bing/bing.py >> /home/j/Bing/log 2>&1
   ```

   表示在每天6:00运行bing.py脚本，可自定义的有(**路径一律使用绝对路径**)：

   `00 6 * * *  `    表示脚本时间

    ` /usr/bin/python3`   Python3的环境

   `/home/j/Bing/bing.py`   需要运行的脚本

   `>> /home/j/Bing/log 2>&1`  输出重定向，表示将 标准输出和错误输出 重定向至`/home/j/Bing/log`文件中，可有可无

4. 部署好之后就可以每隔一段时间利用`scp`命令将图片拷贝至本地

