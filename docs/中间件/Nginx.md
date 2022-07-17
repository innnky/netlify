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

+ 

