# SpringCloud Alibaba

## 引入

+ 总依赖在父项目的dependencyManagement引入
  ![image-20220728170143472](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728170143472.png)

## Nacos

+ 注册中心+配置中心

### 注册中心

+ 替代euruka和config+Bus

+ 安装: github下载 startup.cmd/sh运行

+ web后台: IP:8848/nacos 账号密码都是nacos

+ 基本使用

  + POM(替代euruka)![image-20220728195132406](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728195132406.png)

  + yml![image-20220728195252718](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728195252718.png)
  + 主启动![image-20220728195314069](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728195314069.png) 

  + nacos服务列表查看

+ 消费者进行服务调用

  + 自带ribbon负载均衡
  + 放一个RestTemplate 的Bean(要负载均衡需要加@LoadBalance)
  + 使用时注入进行访问

+ 与其他注册中心对比

  + 同时支持AP和CP,支持切换

    ![image-20220728205959571](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728205959571.png)

  + 默认都是AP

### 配置中心

+ 使用

  + POM

  + ![image-20220728210341131](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728210341131.png)

  + YML(bootstrap.yml)

  + ![image-20220728210455433](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728210455433.png)

  + 弹幕表示port discovery都可以不写从配置中心拉取,弹幕表示基本这里尽可能少填,会变的尽量都放配置中心

  + 动态刷新config

    ![image-20220728210623254](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728210623254.png)

  + 新建配置中Data id规则

    ![image-20220728210810236](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728210810236.png)

    + 例![image-20220728210921625](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728210921625.png)

+ 分类配置管理

  + nacos按照 namespace+group+Data ID

  + namespace区分部署环境 group+Data ID 逻辑区分对象

  + ![image-20220728211912583](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728211912583.png)

  + namespace:默认public

    + 如有开发 测试 生产 创建3个namespace

  + group: 默认DEFAULT_GROUP

  + ```
    Group默认是DEFAULT GROUP， Group可以把不同的微服务划分到同一个分组里面去
    
    Service就是微服务；
    一个Service可以包含多个Cluster（集群），Nacos默认Cluster是DEFAULT， Cluster是对指定微服务的一个虚拟划分。
    北方说为了容灾，一个Service微服务分别部署在了杭州机房和广州机房，
    文时就可以给杭州机房的Service微服务起一个集群名称 (HZ），给广州机房的Service微服务起-个集群名称（GZ） ，还可以尽量让同一个机房的微服务互相调用，以提升性能。
    
    最后是Instance，就是微服务的实例。
    ```

  + 三种方案

    + 方案1

    + ```
      默认空间＋默认分组＋新建dev和test两个DatalD
      通过spring.profile.active属性就能进行多环境下配置文件的读取
      ```

    + 方案2

    + ``` 
      通过建DEV分组和TEST分组
      config:
          server-addr: 1ocalhost:8848 #Nacos 作为配雪中心地加
          file-extension：yam1＃指定yamL格式的配置
          group: TEST GROUP
      ```

    + 方案3

    + ```
      namespace方案
      config:
          server-addr: 1ocalhost:8848 #Nacos 作为院置中心他处
          file-extension：yam1#指定yanl格式的既置
          group: DEV GROUP
          namespace: 7d8fof5a-6a53-4785-9686-dd460158e5d4
      ```

### Nacos集群

+ 架构模式<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728213735700.png" alt="image-20220728213735700" style="zoom:33%;" />

  + 默认自带一个嵌入式数据库derby作持久化,但多节点数据一致性会存在问题
  + 集群使用集中化存储方式,仅支持mysql

+ 单机使用MySQL步骤

  <img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728214140280.png" alt="image-20220728214140280" style="zoom:33%;" />

  + nacos/conf目录下有sql和配置文件

+ 配置nacos集群

  + 先是同单机使用MySQL配置

  + 编辑cluster.conf![image-20220728215259569](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728215259569.png)

  + 修改端口

    ![image-20220728215812502](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220728215812502.png)

  + 使用nginx负载均衡

    + 负载均衡配置到nacos集群

## Sentinel

+ 安装运行:jar文件直接运行

+ 8080端口访问web控制台 用户名密码都是sentinel

+ 使用

  + POM![image-20220729103246200](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729103246200.png)

  + YML

    ![image-20220729103433053](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729103433053.png)

  + sentinel默认为懒加载模式,微服务启动没有反应,访问controller之后会出现在控制台中

+ 控制台

  + 实时监控可以看请求实时流量等各种信息
  + 簇点链路 查看所有的rest接口

### 流控规则

+ 将流量监控和业务逻辑代码分开

+ ![image-20220729104109089](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729104109089.png)

+ 增加流控规则:可以在簇点链路或流控规则菜单中都可以配置

  ![image-20220729104249764](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729104249764.png)

+ 参数解释

  + 流控效果-快速失败:默认情况,直接返回报默认错误
  + 流控效果-预热:在qps达到 阈值/coldFactor(默认3) 时候 经过预热时长后达到阈值 慢慢的把流量放开<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729110517439.png" alt="image-20220729110517439" style="zoom:15%;" />
  + 排队等待:类似于消息队列流量削峰?
  + 流控模式-直接:自己资源达到阈值后限流
  + 流控模式-关联:关联别人的资源达到阈值后限流 例如:支付服务挂了限制订单服务

### 服务降级

+ 与流控的区别? 流控是外部的(访问频率等) 熔断降级是内部的

+ 之前没有半开状态,现在似乎也有了(弹幕)

+ 降级策略

  ![image-20220729111159888](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729111159888.png)

+ 降级规则

  ![image-20220729110840920](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729110840920.png)

+ 配置![image-20220729113554426](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729113554426.png)

### 热点规则

+ 根据传进来的具体参数进行限流
+ 兜底方法@SentinelResource(类似于HystrixCommamd)
  + ![image-20220729151955543](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729151955543.png)
+ ![image-20220729152157675](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729152157675.png)
  + 第0个参数在1秒内访问qps大于1直接熔断降级
  + 此处第0个参数是指Controller中的第0个而不是用户传参数的顺序
+ 参数例外项
  + 当参数为特殊值时不被限流或有另一套限流规则
  + ![image-20220729154454882](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729154454882.png)
+ @SentinelResource只针对在Sentinel后台配置的规则失败后的兜底方法,而程序本身出运行时异常不处理

### 系统自适应限流

+ ![image-20220729154859074](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729154859074.png)
+ ![image-20220729155002580](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729155002580.png)
+ 阈值类型
  + 入口QPS 全局控制
  + 大部分见名知意

### @SentinelResource

+ ![image-20220729161016292](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729161016292.png)

  + 其中getMapping会生成一条"/testHotKey"的记录 SentinelResource会同时生成一个"testHotKey"的记录,两者是不一样的(均可以用来配置簇点规则)
    + 疑问?多个url的资源名称能不能一样?
    + 疑问?是否用这个来区分同一url的不同HTTP方法?

+ blockHandler兜底方法: 针对在web控制台配置的降级 限流规则被触发时对应的处理方法

  ![image-20220729161845386](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220729161845386.png)

  + 使用自定义的类编写兜底方法与业务逻辑分开

    ![image-20220731194755839](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220731194755839.png)

  + 这个类就是一个普通的类,没有任何继承,但里面的兜底方法必须是静态方法

  + ![image-20220731194906650](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220731194906650.png)

  + 注(弹幕提醒):

    + 兜底方法的参数和返回值必须写<img src="https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220731195231862.png" alt="image-20220731195231862" style="zoom:15%;" />
    + 只有按资源名配置才生效,按URL不行

+ fallBack兜底方法: 针对函数执行中抛出的各种运行时异常对应的处理方法![image-20220731202340175](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220731202340175.png)

  + fallBack方法的参数为控制器员参数,外加一个Throwable e
  + fallBack方法返回值为原返回值
  + 也可以像blockHandler一样配置在外面的类里
  + fallBack可以忽略一些指定的异常![image-20220731203237069](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220731203237069.png)


### 整合OpenFeign

+ POM没有要求
+ YML要激活![image-20220731203436875](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/07/image-20220731203436875.png)
+ 其他和hystrix整合openfeign貌似一样(存疑)

### 持久化

+ 持久化进nacos

  + POM

    ![image-20220801150539624](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/08/image-20220801150539624.png)

  + ![image-20220801150645223](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/08/image-20220801150645223.png)

+ 貌似要在nacos里面写json

## Seata分布式事务

+ 跨数据源的多数据库统一调度

+ 例如下单库 账户库 库存库在不同的库中要保证一致性

+ 一次业务操作需要跨多个数据源或需要跨多个系统讲行远程调用就会产生分布式事务问题

+ ![image-20220801151515645](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/08/image-20220801151515645.png)

+ ![image-20220801152334755](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/08/image-20220801152334755.png)

+ 下载安装:

  + 一个压缩包,解压后再bin内运行seata-server.bat
  + conf目录下修改配置(弹幕说新版本直接看readme.md)
    + 分组(事务组)名称
    + 修改存储模式为db store模块 指定连接信息,并执行同目录下db_store.sql
    + 将注册中心修改为nacos

+ 使用:

  + 业务数据库:每个业务库都要执行seata里的一个脚本,创建一个回滚日志表

  + POM (要剔除自带的使用指定版本)![image-20220801154447171](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/08/image-20220801154447171.png)

  + YML(貌似应该是和seata在nacos中注册名为准)

    ![image-20220801154601852](https://test1.jsdelivr.net/gh/innnky/images2@main/uPic/08/image-20220801154601852.png)

  + 创建file.conf(新版可以直接在yml中配置)

  + 



