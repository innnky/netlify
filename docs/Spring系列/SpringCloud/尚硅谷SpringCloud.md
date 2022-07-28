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
  
  + 使用比较繁琐,
  
    + 要在主启动类扫描的包外面建配置类
  
    + ```java
      @Configuration
      public class MySelfRule {    @Bean    public IRule myRule() {        // 定义为随机       
        return new RoundRobinRule();    }}
      ```
  
    + 在启动类上加注解@RibbonClient(name = "CLOUD-PAYMENT-SERVICE", configuration = MySelfRule.class)
  
    + name必须是大写

### OpenFeign

+ 内置了ribbon,进行了封装,简化编程

+ 使用

  + POM

  + ```xml
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-starter-openfeign</artifactId>
            </dependency>
    ```

  + 启动类添加@EnableFeignClients

  + 新建一个业务类**接口**(弹幕说不需要@Component),内部方法的写法和Controller一样![image-20220723172153035](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723172153035.png)

+ 超时配置

+ ```yml
  #设置feign客户端超时时间
  ribbon:
    ReadTimeout: 5000
    ConnectTimeout: 5000
  ```

+ 日志配置

  + 日志级别 ![image-20220723173528097](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723173528097.png)

  + 配置类

    ![image-20220723173603140](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723173603140.png)

  + yml

  ```yml
  logging:
    level:
      com.atguigu.springcloud.service.PaymentFeignService: debug
  ```

## 服务降级

### Hystrix

+ ![image-20220723174108900](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220723174108900.png)

+ 作用:服务降级 服务熔断 接近实时的监控

+ 概念

  + 服务降级 fallback
    + 兜底方案,保证调用防的线程不会被长时间不必要的占用
    + 触发降级的条件
    + ![image-20220725102514022](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725102514022.png)

  + 服务熔断 break
    + 保险丝到达最大访问量时触发熔断, 之后调用降级

  + 服务限流 flowlimit
    + 秒杀等高并发排队有序进行

+ 使用

  + POM

    ![image-20220725103517797](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725103517797.png)

  + 工具JMeter

    + 高并发压力测试

  + 解决

    ![image-20220725105118893](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725105118893.png)

  + 为service添加服务降级

    ![image-20220725105410384](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725105410384.png)

  + 主启动类添加注解@EnableCircuitBreaker(据说已过时,使用@EnableHystrix)

  + 虽然只写了超时属性,但出现运行时异常也会熔断

  + 服务降级一般放客户端

+ 高级

  + 全局的Fallback

    + 没有配的用全局的,单独配置了的走自己的
    + 将这个注解放在目标service类上方,影响整个service类![image-20220725112618575](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725112618575.png)
    + ![image-20220725113338850](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725113338850.png)

  + 将代码解耦合

    + 异常: 运行时 超时 宕机

    + 对FeignClient的业务层接口配置fallback

    + 步骤

      + 在yml启用

        ![image-20220725113146799](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725113146799.png)

      + 对FeignClient的业务层接口配置fallback, 目标指向自己写的一个实现了当前接口的类

        ![image-20220725113947020](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725113947020.png)

      + 对于该实现类,则每一个方法的实现就是fallback方法(并放入容器)

+ 服务熔断

  + ![image-20220725155545307](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725155545307.png)
  + 使用:
    + 在降级的基础上加东西
    + ![image-20220725162410894](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725162410894.png)
    + 服务降级(失败)次数比例高于阈值会触发熔断,从close进入open 此时所有的请求都进入fallback, 到达设定时长进入半开状态,部分请求调用服务若成功率高于一定程度则回复链路回到close
    + ![image-20220725162906652](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725162906652.png)

+ 服务限流:以阿里巴巴为准

+ Hystrix工作流程https://github.com/Netflix/Hystrix/wiki/How-it-Works

+ 图形化控制台![image-20220725163702640](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725163702640.png)

+ 入口类加![image-20220725163753283](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220725163753283.png)之后访问localhost/hystrix

## 网关

### gateway

+ ![image-20220726155529353](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726155529353.png)

+ gateway特性![image-20220726155730727](/Users/xingyijin/Library/Application%20Support/typora-user-images/image-20220726155730727.png)

+ servlet3支持异步非阻塞

+ 核心概念

  + 路由
  + 断言
  + 过滤

+ 工作流程

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726160436032.png" alt="image-20220726160436032" style="zoom:25%;" />

+ 使用

  + POM

    ![image-20220726160640499](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726160640499.png)

  + YML方式进行配置

    ![image-20220726160951792](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726160951792.png)

  + 编码方式进行配置

    ![image-20220726161745672](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726161745672.png)

+ 通过微服务名进行动态路由

  + ![image-20220726162216825](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726162216825.png)
  + lb 负载均衡
  + url 后面直接填服务名

+ pridicate断言: 所有条件全为true才能访问

  + ![image-20220726162455830](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726162455830.png) 
  + After 在规定时间之后访问才能生效
    + ![image-20220726162847403](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726162847403.png)
  + Before Between 和上面类似
  + Cookie: 前面是cookie 名称,后面是正则表达式
    + ![image-20220726163033670](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726163033670.png) 
  + Header: 前面是属性名称,后面是正则表达式
    + ![image-20220726163338988](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726163338988.png)
  + ....

+ fileters过滤器

  + GateWay Filter 用于单一路由的过滤器
    + ![image-20220726163613703](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220726163613703.png)
    + 有很多,例如添加请求头 添加请求参数之类的 
  + Global Filter 全局的过滤器
    + 有十多个自带的
  + 自定义全局过滤器
    + 创建一个类实现GlobalFilter 和Ordered
    + 在filter方法中写自己的逻辑
    + 放入容器

## 服务配置

### Config

+ 原理图

  ![image-20220727102153978](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727102153978.png)

+ 使用步骤服务端

  + github新建一个仓库保存配置文件

  + POM

    ![image-20220727102121343](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727102121343.png)

  + YML

    ![image-20220727102309108](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727102309108.png)

  + 启动类加注解

     ![image-20220727102351799](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727102351799.png)

  + 启动后即可使用http://hostname:port/分支名称/配置文件名.yml 访问到git仓库中根目录的配置文件

  + 读取配置文件

    ![image-20220727102907898](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727102907898.png)

    + 其中最后一个读取到的是json串
    + 第二个不标分支,使用配置中心YML中指定的默认分支

+ 使用客户端

  + POM![image-20220727103334914](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727103334914.png)

  + bootstrap.yml

    ![image-20220727103644214](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727103644214.png)

    + 会读取到master/config-dev.yml的配置文件

+ 客户端配置动态刷新

  + 客户端添加监控依赖![image-20220727104605188](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727104605188.png)
  + 暴露监控![image-20220727104633069](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727104633069.png)
  + 在@Value的类上方加入![image-20220727104717942](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727104717942.png)
  + 修改配置后需要发一个post请求刷新一下客户端配置文件![image-20220727104948254](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727104948254.png)


### Bus消息总线

+ 是什么

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727202147907.png" alt="image-20220727202147907" style="zoom:15%;" /> <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727203753421.png" alt="image-20220727203753421" style="zoom:15%;" />

+ 通过订阅主题实现消息的广播

+ 实现自动刷新全部客户端

  + 第一种:利用消息总线触发客户端/bus/refresh 从而通知全部客户端
  + 第二种:利用消息总线触发服务端,通知总控 更合理
    + config服务端 
      + 添加POM(整合了bus和rabbitMq)
        ![image-20220727205008869](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727205008869.png)
      + YML
        + rabbitMQ的连接配置
        + bus的暴露配置![image-20220727205144931](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727205144931.png)

    + config客户端
      + POM一样
      + YML只要配置连接信息

    + 之后只需要刷新config服务端 http://IP:port/actuator/bus-refresh

+ 实现局部通知

  + ![image-20220727210057214](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727210057214.png)
  + 上方为全局通知,下方定点局部通知
  + **? 为什么是微服务名称加端口号??? 如果是同一个微服务在不同主机上的集群,端口号一样怎么办??**


## CloudStream

+ 消息驱动

  ![image-20220727210919168](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727210919168.png)

+ ```
  立用程序通过 inputs 或者outputs 来与 Spring Cloud Stream中binder对象交互。通过我们配置来binding（綁定）而 Spring Cloud Stream 的binder对象负责与消息中间件交互。所以，我们只需要搞清楚如何与 Spring Cloud Stream 交互就可以方便使用消息驱动的方式。
  ```

+ 基本就是适配器模式

+ 通过Binder作为中间层屏蔽底层的差异

+ 基本概念![image-20220727212023440](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727212023440.png)

+ 注解

  + @Input
  + @Output
  + @StreamListener
  + @EnableBinding

+ 使用

  + 生产者

    + POM

      ![image-20220727212332410](/Users/xingyijin/Library/Application%20Support/typora-user-images/image-20220727212332410.png)

    + YML

      ![image-20220727212422143](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727212422143.png)

    + 启动类没变化

    + 建一个接口,以及其实现类,

      ![image-20220727213009284](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727213009284.png)

  + 消费者

    + pom一样,yml修改成input![image-20220727213506845](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727213506845.png)
    + ![image-20220727213706232](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220727213706232.png)
    
  + 通过group避免消息重复消费
  
    + 默认是在不同的组中,同一个消息会被广播至不同的组中,而同一个组中的消费者竞争关系,不会重复消费
    + 对于rabbitmq 默认每一个消费者创建一个queue
    + 配置组:![image-20220728162500754](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728162500754.png)

## sleuth链路跟踪

+ zipkin安装:jar直接运行

  + 9411端口访问web

+ trace 和span

  ![image-20220728163939567](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728163939567.png)

+ 在需要监控的客户端引入POM

  ![image-20220728164026437](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728164026437.png)

+ YML

  ![image-20220728164113049](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728164113049.png)

