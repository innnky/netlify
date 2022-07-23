#   SpringCloud

## 入门

+ 微服务技术栈

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719151842686.png" alt="image-20220719151842686" style="zoom:20%;" /> 

+ 技术实现

   <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719152023489.png" alt="image-20220719152023489" style="zoom:25%;" />

+ 版本 SpringBoot2.x SpringCloud H版

+ 版本对应

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719152835985.png" alt="image-20220719152835985" style="zoom:45%;" /> 

+ 本课程版本

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220719152943950.png" alt="image-20220719152943950" style="zoom:25%;" /> 

### 版本升级

+ 服务注册中心
  + x eureka 
  + v zookeeper
  + v consul
  + v Nacos 重点
+ 服务调用
  + v Ribbon
  + v LoadBalancer
+ 服务调用2
  + x Feign
  + v OpenFeign
+ 服务降级
  + x Hystrix
  + v Sentinel
+ 服务网关
  + x Zuul
  + v Gateway
+ 服务配置
  + x Config
  + v Nacos
+ 服务总线
  + x bus
  + v Nacos

### 编码构建

+ 关于maven
  + dependencyManagement作用:
    + 父项目中统一指定依赖的版本号,子项目中可以不指定版本号,更新版本时候只要改一处版本号所有子项目都会更新
    + 这里只是声明一个规范,只声明不引入,只有在子项目中使用dependencies中引入时才真正引入jar包
  + 跳过单元测试
    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220720154502101.png" alt="image-20220720154502101" style="zoom:33%;" /> 
  
+ 微服务构建
  + 日志记录: 
    + 类上方(需要lombok)@Slf4j 方法中log.info() 弹幕说不建议使用+进行拼接,建议使用{}占位符
    
  + 热部署
    + jrebel
    + devtools
    
  + 接口测试
    + apifox
    + apipost
    
  + 使用resttemplate 进行http接口调用
  
    ![image-20220722161158152](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722161158152.png)
  
  + 工程重构--新建一个api-common模块
  
    + 将实体类放进去
    + 使用maven install安装到本地仓库
    + 在需要使用的地方引入gav

## 服务注册中心

### eureka

+ 服务端

  + 依赖

  + ```
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
            </dependency>
    ```

  + yml

  + ```
    server:
      port: 7001
    
    spring:
      application:
        name: cloud-eureka-server7001
    
    eureka:
      instance:
        hostname: www.eureka7001.com
      client:
        fetch-registry: false  #不注册自己
        register-with-eureka: false # 不检索自己
        service-url:
          defaultZone: http://www.eureka7001.com:7001/eureka/
      server:
        #关闭自我保护机制，保证不可用服务立即被踢出
        enable-self-preservation: false
        eviction-interval-timer-in-ms: 2000 
    ```

  + 入口类加@EnableEurekaServer注解 启动后可以在7001端口访问

+ 客户端

  + 依赖

  + ```
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
            </dependency>
    ```

  + yml

  + ```
    
    eureka:
      client:
        service-url:
          defaultZone: http://www.eureka7001.com:7001/eureka/
      instance: #
        ip-address: 127.0.0.1
        instance-id: payment8001
        prefer-ip-address: true
       	# 发送心跳时间间隔
        lease-renewal-interval-in-seconds: 1
        lease-expiration-duration-in-seconds: 2
    ```

  + 入口类加@EnableEurekaClient注解

+ 集群

  + 服务端:
    + hostname用不同的
    + 此处互相填对方的地址, 相互注册,本来是自己注册自己      defaultZone: http://www.eureka7001.com:7001/eureka/
    + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722160317752.png" alt="image-20220722160317752" style="zoom:33%;" /> 此处看是否注册了对方
  + 客户端注册进eureka集群 此处填多个注册中心![image-20220722160357393](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722160357393.png)
  + 客户端本身是集群: 使用同一个服务名去注册就会被识别eureka为集群

+ 使用eureka获取微服务名称对应的服务

  + ![image-20220722161121845](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722161121845.png)

    + 此时不用写端口和地址,直接以服务名请求

    + 需要添加注解添加负载均衡的功能

       <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722161308438.png" alt="image-20220722161308438" style="zoom:33%;" />

+ 服务发现

  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722163503909.png" alt="image-20220722163503909" style="zoom:50%;" /> 
  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722161907231.png" alt="image-20220722161907231" style="zoom:33%;" /> 
  + 通过.getServices()获取服务清单列表
  + 通过.getIntences(服务名)通过服务名获取实例列表

+ Eureka自我保护

  + CAP中的AP 当某服务不可达,不会立刻将其删除,进入保护模式
  + ![image-20220722162536770](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722162536770.png)
  + ![image-20220722162550251](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722162550251.png)

### Zookeeper

+ 服务端

  + 在linux安装单独的软件服务端

+ 客户端

  + pom

  + ```xml
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-starter-zookeeper-discovery</artifactId>
            </dependency>
    ```

  + yml

  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722163425721.png" alt="image-20220722163425721" style="zoom:50%;" /> 

  + 版本冲突问题

    <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722163914276.png" alt="image-20220722163914276" style="zoom:33%;" /> 

+ zookeeper是临时服务节点, 没有心跳直接清除,重连后流水号会变化

+ 使用zookeeper获取微服务名称对应的服务地址

  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722164606816.png" alt="image-20220722164606816" style="zoom:33%;" /> 
  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722164632954.png" alt="image-20220722164632954" style="zoom:30%;" /> 
  + 貌似和eureka一样

### Consul

+ go语言编写

+ 服务端: docker安装 8500端口web管理后台

+ 客户端

  + POM

  + <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723103542069.png" alt="image-20220723103542069" style="zoom:33%;" /> 

  + yml

    <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723103615090.png" alt="image-20220723103615090" style="zoom:33%;" /> 

  + 启动类![image-20220723103644147](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723103644147.png)

  + 使用consul获取微服务名称对应的服务地址
  
    + 和前面的一样

### 总结

+ CAP理论

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723104957790.png" alt="image-20220723104957790" style="zoom:33%;" /> 

+ <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723105107522.png" alt="image-20220723105107522" style="zoom:33%;" /> 

+ AP保证可用性,同步失败时候可以返回旧值

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723105543564.png" alt="image-20220723105543564" style="zoom:33%;" /> 

+ CP保证一直性, 同步失败直接报错

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723105728538.png" alt="image-20220723105728538" style="zoom:33%;" /> 

## 服务调用

### Ribbon

+ LB负载均衡:

  + 集中式LB:Nginx
  + 进程内LB:逻辑集成到消费端,Ribbon

+ 使用

  + eureka client已经引入了ribbon

  + 在配置类中放一个bean即可使用, @LoadBalance 增加负载均衡作用

    <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220722161308438.png" alt="image-20220722161308438" style="zoom:33%;" /> 

  + RestTemplate 方法

    + postForObject  仅获得一个json串
    + getForEntity 可以同时包含状态码等其他信息

+ 更换负载均衡规则

  + IRule接口的各种实现类
  + 自带的规则<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723112523620.png" alt="image-20220723112523620" style="zoom:33%;" />



