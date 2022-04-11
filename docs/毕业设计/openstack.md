# openstack

![image-20220304123830171](https://home.innky.xyz:25566/images/image-20220304123830171.png)

![image-20220304124137800](https://home.innky.xyz:25566/images/image-20220304124137800.png)

![image-20220304124419279](https://home.innky.xyz:25566/images/image-20220304124419279.png)

![image-20220304130138561](https://home.innky.xyz:25566/images/image-20220304130138561.png)

## KeyStone

![image-20220324090023412](https://home.innky.xyz:25566/images/image-20220324090023412.png)

![image-20220324090627004](https://home.innky.xyz:25566/images/image-20220324090627004.png)

![image-20220324090645086](https://home.innky.xyz:25566/images/image-20220324090645086.png)

关键字

![image-20220324090829937](https://home.innky.xyz:25566/images/image-20220324090829937.png)

+ 组件交互过程![image-20220324091228850](https://home.innky.xyz:25566/images/image-20220324091228850.png)

## 搭建openstack

+ 初始化各个节点，配置网络相关
+ 配置controller
  + 安装mariadb rabbitmq
  + 安装keystone认证服务
  + 安装Glance镜像服务
  + 安装nova控制器
  + 安装neutron控制器组件
  + 配置计算节点使用neutron
  + 配置块存储控制器租金啊
+ 配置conpute
  + 安装nova计算服务compute节点
  + 配置计算节点使用neutron
+ 配置network
  + 安装neutron
+ 配置block
  + 安装cinder

## Glance镜像

+ 组件![image-20220324093953508](https://home.innky.xyz:25566/images/image-20220324093953508.png)
+ 镜像唯一标识符![image-20220324094104341](/Users/xingyijin/Library/Application%20Support/typora-user-images/image-20220324094104341.png)
+ 镜像状态![image-20220324094123507](https://home.innky.xyz:25566/images/image-20220324094123507.png)
+ 用来测试的小镜像：cirros镜像

## Nova

+ 作用![image-20220324095005443](https://home.innky.xyz:25566/images/image-20220324095005443.png)
+ 构成![image-20220324095114161](https://home.innky.xyz:25566/images/image-20220324095114161.png)![image-20220324095140063](https://home.innky.xyz:25566/images/image-20220324095140063.png)
+ 。。。
+ mysql命令![image-20220324095944578](https://home.innky.xyz:25566/images/image-20220324095944578.png)

## neutron

+ ![image-20220324101212341](https://home.innky.xyz:25566/images/image-20220324101212341.png)
+ ![image-20220324101957320](https://home.innky.xyz:25566/images/image-20220324101957320.png)
+ <img src="https://home.innky.xyz:25566/images/image-20220324102157812.png" alt="image-20220324102157812" style="zoom: 33%;" />

## 仪表盘套件Horizon

## Cinder块存储



