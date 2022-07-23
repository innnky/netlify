# Nginx

## 引入

+ 主要概念
  + 反向代理
    + 正向代理:配置代理服务器,通过代理服务器间接访问互联网
    + 反向代理:客户端无需任何配置,客户端对代理是无感知的
    + 对外暴露的是代理服务器的ip和端口,隐藏目标服务器的ip
  + 负载均衡
  + 动静分离
    + 将动态资源和静态资源分开放在不同服务器中,使用nginx进行转发
+ 高可用

## 安装及常用命令

+ 直接用docker安装
  + 可以先启动一个临时的,然后将配置文件拷贝出来,之后删除
  + 启动容器时将刚刚拷贝出来的配置文件挂载上去
+ 常用命令
  + nginx 启动
  + nginx -v 查看版本号
  + nginx -s stop 关闭
  + nginx -s reload 重新加载nginx配置文件

## nginx配置文件

+ 3大部分

  + 全局块

    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717170816443.png" alt="image-20220717170816443" style="zoom:50%;" /> 

  + events块

    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717170901032.png" alt="image-20220717170901032" style="zoom:50%;" /> 

  + http块

    + http全局块

      <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717170948806.png" alt="image-20220717170948806" style="zoom:50%;" />

    + server块

      + 主要配置内容

## nginx配置实例

### 配置反向代理

+ 实例1 192.168.17.129 转发至8080tomcat

  ![image-20220717172152426](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717172152426.png)

+ 实例2 <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719103007803.png" alt="image-20220719103007803" style="zoom:33%;" />

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719105244235.png" alt="image-20220719105244235" style="zoom:50%;" />

  + location 指令说明
    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719105450110.png" alt="image-20220719105450110" style="zoom:33%;" /> 
    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719105518250.png" alt="image-20220719105518250" style="zoom:50%;" /> 


### 配置负载均衡

+ 实例 浏览器地址栏输入地址 http://192.168.17.129/edulahtml，负载均衡效果，平均 8080和 8081 端口中。

  + 在http块中加入<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719105854827.png" alt="image-20220719105854827" style="zoom:50%;" />
  + 在目标server中加入规则<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719105948238.png" alt="image-20220719105948238" style="zoom: 50%;" />

+ 负载均衡策略

  + 轮询 (默认)

  + 权重weight策略(权重默认为1)
    <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719110210894.png" alt="image-20220719110210894" style="zoom:50%;" />

  + ip hash (每一个ip地址固定访问一台机器)

    <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719110304605.png" alt="image-20220719110304605" style="zoom:50%;" />

  + fair 按服务器响应时间分配

    <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719110359285.png" alt="image-20220719110359285" style="zoom:50%;" />

### 动静分离

+ 浏览器缓存![image-20220719110757146](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719110757146.png)

+ 设置静态资源文件路径

  ![image-20220719111148465](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719111148465.png)

### 配置高可用集群

+ 原理<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719112050429.png" alt="image-20220719112050429" style="zoom:50%;" />



## 原理

+ nginx启动后有两个进程master worker
  + 原理![image-20220719115500791](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719115500791.png)
  + (生产者消费者模式)
  + ![image-20220719115728954](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719115728954.png)
  + 
