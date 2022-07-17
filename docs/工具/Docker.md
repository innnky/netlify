# Docker

## 引入

+ 容器与虚拟器区别
  + 虚拟器缺点:占用资源多  冗余步骤多  启动慢
  + ![image-20220712170835895](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220712170835895.png)
  + ![image-20220712170856975](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220712170856975.png)

+ 容器

  + ![image-20220714152652800](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714152652800.png)
  + ![image-20220714152701225](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714152701225.png)

+ docker镜像文件类似于Java的类模板，而docker容器实例类似于java中new出来的实例对象。

+ 可以把容器看做是一简易版的Linux环境(包括root用户权限、进程空间、用户空间和网络空间等〉和运行在其中的应用程序。

+ docker工作原理

  ![image-20220714152907133](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714152907133.png)

+ 安装

  + 阿里云 镜像加速器 每人都有一个不同的加速地址

+ 区别总结 面试常问

  + ![image-20220714155015379](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714155015379.png)
  + ![image-20220714155110126](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714155110126.png)
  + 虚拟机是操作系统间的隔离 docker是namspace间的隔离 虚拟机的安全性比docker安全性做的好

## Docker常用命令

### 帮助启动类

 <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714155718157.png" alt="image-20220714155718157" style="zoom:33%;" /> 

### 镜像命令

+ docker images [选项] 列出本地镜像
  + -a 列出曾经有过的全部	
+ docker search [选项] xxxx 在远程仓库搜索
  + --limit 5 限制5条
+ docker pull 镜像[:TAG] 拉取远程镜像
+ docker system df 系统空间用量信息
+ docker stats
+ docker rmi 
  + -f 强制删除
  + -f 镜像id1:Tag 镜像id2:Tag 
  + 删除全部docker mi -f $(docker images -qa)
+ 虚悬镜像:
  + 仓库 标签都是\<none \>的镜像

### 容器命令

+ **创建**容器 docker run [OPTIONS] IMAGE [COMMAND] [ARG...] 

  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714161246136.png" alt="image-20220714161246136" style="zoom:33%;" /> 
  + --name=xxxxx (等效于--name xxxxx) 指定容器名称
  + -p 8888:8080 左边是宿主机端口(外),右边是docker(内)
  + --restart=always 该容器随docker自动启动
  + 例: docker run -it centos /bin/bash :以交互模式运行centos 并执行bash
  + **实践**
    + command 对每一个镜像应该有一个默认值

+ docker ps 列出所有在运行的容器

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714161912541.png" alt="image-20220714161912541" style="zoom:33%;" />

  + -a 列出历史上运行过的容器
  + -l 显示最近创建的容器
  + -n 5 只显示5条
  + -q 只显示容器编号

+ 退出容器<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714162304664.png" alt="image-20220714162304664" style="zoom:33%;" />

+ <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714162449857.png" alt="image-20220714162449857" style="zoom:50%;" />

+ docker rm 容器id或容器名称 删除已停止的容器

  + -f 强制删除

+ 重点

  + ![image-20220714163016830](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714163016830.png)

  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714163122239.png" alt="image-20220714163122239" style="zoom:33%;" />

  + -d启动ubuntu 会直接自杀 因为本身就是一个后台进程没有默认的前台

  + -d启动redis 没有问题,因为redis本身有一个前台进程

  + docker logs 容器id 查看运行日志

  + docker top 容器id 查看容器内运行的进程

  + docker inspect 容器id 查看容器内部细节 

  + 重新进入运行中的容器

    ![image-20220714163757715](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714163757715.png)

+ docker cp 容器ID:容器内路径 目的主机路径     从容器内拷贝文件到主机

+ docker export 容器ID>文件名.tar 

+ cat 文件名.tar | docker import - 镜像用户/镜像名：镜像版本号

## docker镜像详解

+ 联合文件系统

  + ![image-20220714164651566](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714164651566.png)
  + 镜像分层是为了复用

+ docker commit 创建一个新的镜像

  ![image-20220714165146739](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220714165146739.png)

+ 发布到阿里云

+ 私有库docker registry

  + 用docker安装并运行
  + ![image-20220715143956904](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715143956904.png)


## 容器数据卷

+ 坑![image-20220715144515145](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715144515145.png)

+ 例![image-20220715144620199](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715144620199.png)

+ 做什么

   <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715144737701.png" alt="image-20220715144737701" style="zoom:50%;" />

+ docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录 镜像名

+ 限制容器内只读 :ro <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715151231714.png" alt="image-20220715151231714" style="zoom:50%;" />

+ 容器卷继承<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715151509701.png" alt="image-20220715151509701" style="zoom:50%;" />

  + 就是将u1容器的卷创建规则复制过来了

+ ??如何后续追加容器数据卷

## docker安装常用软件

+ tomcat

  + 新版需要进去删除webapps 并将webapps.dist改为webapps才会显示默认访问页

+ mysql

  + 默认会有中文乱码问题

    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715160821787.png" alt="image-20220715160821787" style="zoom:33%;" /><img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715160835334.png" alt="image-20220715160835334" style="zoom:33%;" /> 

  + 挂数据卷

     <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715160330209.png" alt="image-20220715160330209" style="zoom:50%;" />

+ redis

  + 挂载

  + 编写conf

  + 启动

     <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220715163329355.png" alt="image-20220715163329355" style="zoom:50%;" />

## 高级安装

+ 主从复制

## Dockerfile

+ ![image-20220716153112665](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716153112665.png)

+ 用来构建镜像的第二种方法

+ ![image-20220716153600639](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716153600639.png)

+ 基础知识

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716153734127.png" alt="image-20220716153734127" style="zoom:33%;" /> 

+ 执行Dockerfile大致流程

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716153808678.png" alt="image-20220716153808678" style="zoom:33%;" /> 

+ 常用保留字

  + FROM 该镜像基于那个基础镜像 一般是在第一行

  + MAINTAINER 镜像维护者信息

  + RUN 镜像构建时执行的命令

    + shell格式 >> RUN 命令行命令
    + exec格式 >> <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716154451892.png" alt="image-20220716154451892" style="zoom:50%;" />

  + WORKDIR 指定登录进去后默认路径

  + USER 指定镜像的用户 默认root

  + ENV <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716154635094.png" alt="image-20220716154635094" style="zoom:33%;" />  就是设置linux环境变量

  + VOLUME 定义容器卷 相当于-v

  + ADD <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716155003278.png" alt="image-20220716155003278" style="zoom:33%;" />相当于copy加解压

  + COPY <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716155026271.png" alt="image-20220716155026271" style="zoom:33%;" />

  + CMD 启动容器后干的事情

    + 使用格式与RUN 一样
    + ![image-20220716155208070](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716155208070.png)
    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716155439740.png" alt="image-20220716155439740" style="zoom:50%;" /> 

  + ENTRYPOINT 类似CMD 但不会被覆盖 可以传参

    + ![image-20220716155653730](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716155653730.png)

    + 例子

      <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716155710346.png" alt="image-20220716155710346" style="zoom:50%;" /> 

  + EXPOSE 暴露端口

+ 构建![image-20220716161010914](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716161010914.png)

  + 需要加一个 .

+ 虚悬镜像

  + 构建时没有加名字比如 docker build .
  + 查询虚悬镜像![image-20220716161556821](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716161556821.png)
  + 删除全部虚悬镜像![image-20220716161619905](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716161619905.png)

## 微服务实战

+ 问题 expose 和 volume 有啥用?
+ 问题 -d 和 -it区别 如何体现在dockerfile中

## Docker网络

+ 网络命令 

  ![image-20220716164639835](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716164639835.png)

  + docker network ls

     ![image-20220716164550172](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716164550172.png )

+ 四大网络模式<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716165003440.png" alt="image-20220716165003440" style="zoom:50%;" />

+  bridge模式

  + 默认模式
  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716165736248.png" alt="image-20220716165736248" style="zoom:50%;" />

+ host模式 公用主机的网络

  + 在创建容器时候使用--network=host指定
  + ![image-20220716171742547](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716171742547.png)
  + 使用host 模式 -p没有意义了
  + ![image-20220716171617854](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716171617854.png)

+ none模式

  + --network=none
  + 没有网络配置

+ container模式 借用另一台容器的网络

  + --network container:mytomcat
  + 如果两个容器内有端口重复则会出错
  + 如果另一台容器关闭了则当前容器网络也没了

+ 自定义网络

  + docker network create xxxx
  + --network xxx
  + 使用自定义网络后可以直接使用容器名称解析到对应的ip,**可以直接使用名字ping通别的容器**
  + ![image-20220716173342195](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716173342195.png)

## DockerCompose容器编排

+ docker compose 做什么

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220716173857199.png" alt="image-20220716173857199" style="zoom:33%;" />

+ 两个要素

  + 服务service
  + 工程project

+ 三步骤

  + 编写Dockerfile 构建成为镜像
  + 编写docker-compose.yml定义业务单元,安排各个容器
  + 使用docker-compose up命令启动并运行整个应用,一键部署

+ 常用命令

  ![image-20220717094646091](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717094646091.png)

+ 例

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717100930540.png" alt="image-20220717100930540" style="zoom:33%;" /> <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717101723675.png" alt="image-20220717101723675" style="zoom:33%;" />

## portainer

+ 启动<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717101927640.png" alt="image-20220717101927640" style="zoom:67%;" />
+ 使用9000端口访问

## 容器监控

+ <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220717103846956.png" alt="image-20220717103846956" style="zoom:20%;" /> 
+ 
