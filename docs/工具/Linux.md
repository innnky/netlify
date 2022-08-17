# Linux

## 入门

+ 内核下载https://www.kernel.org/
+ vmware安装
+ centos安装
  + centos下载http://mirrors.163.com/centos/
  + 分区
    + ![image-20220622101850195](https://test1.jsdelivr.net/gh/innnky/images@master/uPic/image-20220622101850195.png) 
    + kdump 内核崩溃转存
+ VMware
  + VMware 网络连接模式
    + ![image-20220622102852121](https://test1.jsdelivr.net/gh/innnky/images@master/uPic/image-20220622102852121.png) 
  + 虚拟机克隆:直接拷贝一份或使用VMWare克隆功能(右键虚拟机-管理-克隆)
  + 虚拟机快照
  + 虚拟机迁移
  + VMTools:共享文件夹等功能

## 目录结构

+ 常用目录
  + /bin常用命令目录(还有/usr/bin /usr/local/bin)
  + /sbin 管理员命令
  + /home 普通用户目录
  + /root 管理员主目录
  + /lib 动态链接库
  + /etc 各种配置文件
  + /usr 用户安装的程序目录
    + /usr/local 安装的软件目录
  + /boot linux启动相关文件
  + /proc /sys /srv 别动
  + /dev 设备
  + /media 如u盘之类的设备
  + /mnt 挂载
  + /opt 安装文件放在该目录
  + /var 变化扩充的东西 如日志

## vi和vim

+ 常见快捷键
  + 正常模式
    + yy复制 5yy复制5行
    + p粘贴
    + dd删除
    + G最后行 gg首行
    + u撤销
    + 20 shift+g
    + 20 回车 向下20行
  + 命令模式
    + /进入查找
    + n查找下一个
    + 显示行号:set nu 去除:set nonu

## 关机和重启

+ 基本命令
  ![image-20220704172243480](https://test1.jsdelivr.net/gh/innnky/images@master/uPic/image-20220704172243480.png)
  + shutdown 默认代表一分钟后关机

## 用户管理

+ 基本命令
  + useradd 用户名 
    + 添加用户后会创建home目录,登录后会自动进入
    + 手动指定用户家目录![image-20220705104328712](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220705104328712.png)
  + passwd 用户名 >>>修改密码
    + 不带参数默认修改当前用户
  + userdel 用户名
    + 默认保留用户的家目录
    + userdel -r 用户名 同时删除家目录
  + id 用户名 >> 查询用户信息
  + su    -   用户名 >> 切换用户
  + logout 登出
  + whoami/who am i 查询当前用户/登录用户 (两个不一样如果登录后又切换了用户)
+ 用户组
  + 类似角色,对用户的权限统一管理
  + groupadd/del 添加/删除组
  + useradd -g 用户组 用户名 >> 添加用户时指定组
    + 前一节中,不指定组创建用户,会默认建一个和用户名相同的组
  + usermod -g 用户组 用户名 >> 修改用户组
+ 相关文件
  + ![image-20220705105713810](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220705105713810.png)
  + ![image-20220705105753159](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220705105753159.png)
  + ![image-20220705105823185](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220705105823185.png)

## 实用指令

+ 运行级别
  + ![image-20220705110335307](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220705110335307.png)
  + 修改系统启动运行级别 略
  + centos7通过单用户模式找回root密码
  
+ 帮助指令
  + man ls (获取ls命令的帮助信息)
    + -a 列出所有文件(包括隐藏文件)
    + -l 单行 等于ll
    + 选项可以组合 如-al
  + help cd 查看cd命令的帮助
  

### 文件目录相关指令

+ pwd  cd
+ !du -lh --max-depth=1 列出当前目录下所有文件夹的大小(递归)
+ ls
  + -a 全部文件
  + -l 单行显示
  + -h 人性化显示(文件大小显示)
  + ![image-20220706205359509](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706205359509.png)
    + 权限 [链接数量]或[目录子文件数量(包含隐藏,至少为2)] 用户 组 字节数 最后修改日期 文件名
+ mkdir (参数-p 创建多级)
+ rmdir 删除非空目录     (rm -rf)
+ touch 创建空文件
+ cp [选项] 源文件 目标文件
  + -r 递归复制目录
  + 覆盖重名文件\cp -r homr/bbb /opt
+ mv
  + mv 貌似不用-r
+ cat 仅查看(-n查看行号)
  + 使用管道 cat xxxxx | more
+ more指令 
  + ![image-20220706110314909](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706110314909.png)
+ less命令
  + less 文件名
  + ![image-20220706110430964](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706110430964.png)
+ echo [选项] [输出内容] 例 : echo $HOSTNAME
+ head 查看文件前几行(默认前10行)(-n 行数)
+ tail 查看最后几行 
  + -n 指定行数
  + -f 实时监控文件 (会阻塞控制台)
+ 输出重定向 > 覆盖 >> 追加
  + echo "hello" > aa.txt
  + ls -al > aa.txt
+ ln -s [源文件]  [软链接名] 建立符号链接
+ history [指令数量] 查看曾经执行的指令
  + 使用! 行号执行指令

### 日期时间类

+ date
  ```
  ，基本语法
  1) date  (功能描述：显示当前时间）
  2) date +%Y（功能描述：显示当前年份〕
  3) date +%m（功能描述：显示当前月份）
  4) date +%d （功能描述：显示当前是哪一天）
  5) date "+%Y-%m-%d %H:%M:%S"（功能描述：显示年月日时分秒）
  6) date -s"2020-11-03 20:02:10" 设置时间
  ```

+ cal 显示日历 (cal 2020 查看2020年日历)

### 搜索查找类

+ find 指令

  + find [搜索范围] [选项]

  + ```
    -name<查询方式> 按照指定的文件名查找模式查找文件
    -user<用户名> 查找屈于指定用户名所有文件
    -size <文件大小> 按照指定的文件大小查找文件
    -atime +10 10天前的文件
    -mtime 修改时间
    -ctime 创建时间
    
    find /home -name *.txt 
    find / -size +200M (+大于 -小于 =等于)
    ```

+ locate 

  + updatedb 建索引
  + 通过数据库(相当于索引查询)

+ grip 过滤查找 与管道配合使用(可以使用正则)

  + ![image-20220706113829159](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706113829159.png)
  + 案例![image-20220706114002429](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706114002429.png)

### 压缩和解压

+ gzip/guzip( gzip /home/hello.txt)
+ zip/unzip
  + ![image-20220706114452505](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706114452505.png)
+ tar
  + ![image-20220706114902612](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706114902612.png)

## 组管理和权限管理

+  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706115349056.png" alt="image-20220706115349056" style="zoom:33%;" />
+ 所有者
  + ll 查看文件所有者![image-20220706202501644](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706202501644.png)
  + 修改所有者  chown 用户名 文件名
    + chown newowner:newgroup 文件/目录 改变所有者和所在组
    + -R递归修改目录内的全部文件
+ 组
  + 创建组 groupadd 
  + 修改文件所在组 chgrp 组名 文件名
  + 修改用户所在组 usermod -g 新组名 用户名
    + 也可以使用-R进行递归修改

### 权限

![image-20220706204232969](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706204232969.png)

+ 权限 rwx 读 写 执行

  + 对于文件, w可以修改但不能删除,要删除文件需要有对文件所在目录的w权限才行
  + 作用到目录<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706204701281.png" alt="image-20220706204701281" style="zoom:67%;" />
  + 如果没有r权限,**虽然不能对目录进行ls操作**,但却**可以**读和写目录内的文件

+ 修改权限

  + chmod

    ![image-20220706205751169](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706205751169.png)

    <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220706210130739.png" alt="image-20220706210130739" style="zoom:50%;" /> 

  + 权限组修改后要**重新登录**后才会获得新组的权限

## 定时

### croud 定时任务

+ crontab [选项]
  + -e 编辑任务
  + -l 查询全部任务
  + -r 删除当前用户全部任务
  + service crond restart
+ 定时参数 ---  [参数] [待执行命令]
  + ![image-20220707155925119](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707155925119.png)
  + ![image-20220707160145429](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707160145429.png)
  + 例![image-20220707160038110](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707160038110.png)
  + ??月中的第几天 和 星期几 两者都指定了的话,是**与**还是**或**的关系??因为前面的很明显都是**与**的关系,但视频里说是**或**
  + 待执行命令也可以直接写xxx.sh 但当前用户必须要有执行权限
+ ![image-20220711160937315](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711160937315.png)目录下似乎会每天执行

### at定时任务

> 仅执行一次的定时任务

+ ps -ef | grep atd 检测atd进程是否在运行
+ 存在一个任务队列 每60秒检测执行一次队列
+ 命令
  + atq 查看当前全部任务
  + atrm [任务编号] 删除指定任务
  + at [选项] [时间]
  + 使用control + D 退出
+ 选项
  + ![image-20220707162031017](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707162031017.png)
+ 时间
  + ![image-20220707162303915](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707162303915.png)
  + 案例![image-20220707162945927](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707162945927.png)

## linux分区

+ 磁盘使用指令

  + 通过lsblk查看分区挂载情况(加上-f更详细的显示)
    ![image-20220707163448420](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707163448420.png)
    + 硬盘符号说明![image-20220707163737767](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707163737767.png)
  + 查看磁盘使用量 df -h
  + 查询特定目录用量 du -h (默认查询当前目录)
    + ![image-20220707165344092](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707165344092.png)
    + 例![image-20220707165539925](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707165539925.png)
  + 统计/opt下**文件**的数量 ![image-20220707165825908](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707165825908.png)
    + 使用正则表达式进行过滤
    + 使用wc统计数量
  + 统计/opt下全部文件的数量(递归统计)![image-20220707165958246](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707165958246.png)
  + tree 目录名

+ •如何增加一块硬盘

  ```
  虛拟机添加硕盘
  分区
  格式化
  挂载
  设置可以自动挂载
  ```

  + 添加硬盘后默认没有分区![image-20220707164249044](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707164249044.png)
  + 分区命令 fdisk /dev/sdb
    + 在交互界面输入错误按ctrl+退格进行删除
  + 格式化分区![image-20220707164606274](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707164606274.png)
  + 挂载![image-20220707164744851](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707164744851.png)
  + 卸载![image-20220707164854975](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707164854975.png)
  + 注:**用命令行挂载重启会失效**
  + 永久挂载
    + ![image-20220707165031878](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707165031878.png)
    + ![image-20220707165121265](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220707165121265.png)

## 网络

+ 手动修改网络配置![image-20220708105027238](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220708105027238.png)
  + ![image-20220708105236367](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220708105236367.png) 
+ 修改完成后重启服务或重启系统生效![image-20220708105331374](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220708105331374.png)
+ 使用主机名
  + 设置主机名 修改/etc/hostname
  + 查看主机名 hostname
  + win hosts文件 C: Windows\System32\drivers\etc\ hosts
  + linux hosts文件 /etc/hosts
+ 有关dns解析
  + 先在浏览器缓存中找
  + 再在本地DNS缓存中找
  + 再在hosts文件中找
  + 再请求dns服务器

## 进程

+ 分为前台和后台程序

+ 命令

  + ps 查看系统所有进程

    + 一般3个参数-aux 共同使用 查看详情

    + ![image-20220708111059474](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220708111059474.png)

      ![image-20220708111240743](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220708111240743.png)

    + 通常使用grep配合

    + -e全部进程 -f以全格式显示

  + pstree [选项] 以树状显示进程

    + -p显示进程号
    + -u显示用户

  + kill [选项] 进程号 >>>>>>>终止进程

    + 选项
      + -9 强制终止
    + 案例![image-20220708112413114](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220708112413114.png)

  + killall 进程名称 >>>>>>>通过名称终止,支持通配符

## 服务管理

+ service 管理指令

  + ![image-20220710150335477](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710150335477.png)
  + service 指令管理的服务在 /etc/init.d 查看
  + setup 查看全部系统服务

+ chkconfig 指令

  + 指定各个服务在不同运行级别的运行设置
  + Centos7.0 后，很多服务使用systemctl 管理
  + ![image-20220710151102223](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710151102223.png)

+ systemctl 指令

  + ![image-20220710151208894](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710151208894.png)
  + ![image-20220710151324101](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710151324101.png)

+ 防火墙服务

  + 查询进程的端口及协议![image-20220710152049284](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710152049284.png)
  + ![image-20220710151951052](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710151951052.png)
  + 关闭防火墙: systemctl stop firewalld    systmectl disable firewalld

+ 动态监控进程 (类似任务管理器)

  + top/htop [选项]

    + ![image-20220710152713072](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710152713072.png)

    + 交互操作

       ![image-20220710152729373](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710152729373.png)

      u监控用户

      k终止进程

+ 监控网络状态

  + netstat [选项]
  + ![image-20220710153020937](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710153020937.png) 
  +  **netstat -anp | grep xxx**

## RPM与Yum

+ rpm
  + 查询安装的rpm列表 
    + rpm -qa | grep xxx
  + rpm -q  xxx查询是否安装
    + rpm -qi  xxx查询安装信息
    + rpm -ql xxx 查询安装文件
    + rpm -qf 文件全路径名 查询文件所属的软件包
  + rpm -e RPM包名 (--nodeps 忽略依赖强制卸载)
  + rpm -ivh RPM包全路径名称 (安装 带提示 带进度条)
+ yum
  + 查询 yum list | grep firefox
  + 安装 yum install xxx

## JDK安装

+ 环境变量:编辑/etc/profile 文件(弹幕说在.bashrc中编辑)

  ![image-20220710155026798](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710155026798.png)

  使用source /etc/profile重新加载

## shell

+ ![image-20220710160303620](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710160303620.png) 

+ 执行sh脚本: 

  + 有执行权限: ./xxx.sh
  + 无执行权限: sh xxx.sh

+ 变量:系统变量和用户变量

  + 系统变量:(通过set 查看全部系统变量) $HOME @PWD等

  + 用户变量

    + 定义变量 变量名=值 (不要加空格!!!)

    + 撤销变量 unset 变量名

    + 输出变量 echo $变量名 (加引号也可以)

    + 定义静态变量 readonly 变量名=值(不能unset)

    + 定义注意事项

      ![image-20220710161140430](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710161140430.png) 

+ 环境变量

  + ![image-20220710161311231](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710161311231.png)

+ 注释 

  + #单行
  + :<<!    多行注释 !

+ 位置参数

  + ![image-20220710161704568](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710161704568.png) 

+ 预定义变量

  ![image-20220710161829215](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710161829215.png)

+ 运算符![image-20220710162336849](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710162336849.png)

  + 推荐使用第二种写法 ![image-20220710162612480](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710162612480.png)比较简洁

+ 分支

  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710162840210.png" alt="image-20220710162840210" style="zoom:50%;" />

  + 案例

     <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710163127284.png" alt="image-20220710163127284" style="zoom:33%;" />

  + 多分支

     <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710163220193.png" alt="image-20220710163220193" style="zoom:33%;" /> <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710163337126.png" alt="image-20220710163337126" style="zoom:33%;" /> 

+ 循环

  + for<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710163521963.png" alt="image-20220710163521963" style="zoom:50%;" /><img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710163732411.png" alt="image-20220710163732411" style="zoom: 50%;" />
    + 案例<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710163805506.png" alt="image-20220710163805506" style="zoom:33%;" /> <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710163934443.png" alt="image-20220710163934443" style="zoom:33%;" />
  + while<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220710164044292.png" alt="image-20220710164044292" style="zoom:50%;" />
  
+ read读取控制台参数

  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711150612469.png" alt="image-20220711150612469" style="zoom:50%;" />
  + 例![image-20220711150727867](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711150727867.png)
  
+ 函数

  + 系统函数
    + basename函数
      + ![image-20220711150848175](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711150848175.png)
      + 如basename /home/aaa/bbb.txt 返回bbb.txt
    + dirname函数 与basename 相反
  + 用户函数
    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711151048165.png" alt="image-20220711151048165" style="zoom:50%;" /> <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711151155353.png" alt="image-20220711151155353" style="zoom:50%;" />

## UBUNTU APT

+ 常用命令

  ![image-20220711153914009](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711153914009.png)

## 日志管理

+ /var/log/ 目录就是系统日志文件的保存位置

+ 系统常用日志

+ ![image-20220711155105043](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711155105043.png)

+ 日志管理服务rsyslogd

  + 配置文件/etc/rsyslog.conf
  + grep -v xxx 查询不包含xxx的行
  + 编辑文件时的格式为：\*.\*
    + 其中一个\*代表日志类型，第二个\*代表日志级别
    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711155722180.png" alt="image-20220711155722180" style="zoom:33%;" /><img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711155735985.png" alt="image-20220711155735985" style="zoom: 25%;" />

+ 日志轮替logrotate

  + 配置文件/etc/logrotate.conf

    + ![image-20220711160443704](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-2022071116
    + 0443704.png)
    + 也可以把单独规则写在logrotate.d目录下

  + 轮替规则

    ![image-20220711160808687](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220711160808687.png)

## 源码阅读

+  可以去研究linux0.01源码



## 待解决

+ 生产环境怎样查询cpu飙高
+ 生产环境怎样查询内存泄漏
+ 生产环境怎样查询报错日志



## 补充

+ && 与  ||

  + | 命令             | 作用                                |
    | ---------------- | ----------------------------------- |
    | 命令1 && 命令2   | 如果 命令1执行成功了, 才执行 命令2  |
    | 命令1 \|\| 命令2 | 如果 命令1 执行失败了, 才执行 命令2 |

  + mkdir 错误目录 || echo "提示创建目录失败"

+ & 与 nogui 相关问题

+ 

