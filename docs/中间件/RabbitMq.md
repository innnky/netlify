

# RabbitMq

## 引入

+ 功能

  + 流量消峰
  + 应用解耦
  + 异步处理

+ 概念

  ![image-20220221093606377](https://home.innky.xyz:25566/images/image-20220221093606377.png)

+ 6大核心工作模式

  ![image-20220221093711018](https://home.innky.xyz:25566/images/image-20220221093711018.png)

+ 安装

  + [win](https://www.cnblogs.com/saryli/p/9729591.html)

    + 命令

      ```powershell
      .\rabbitmqctl.bat stop
      .\rabbitmqctl.bat start_app
      ```

      

  + [centos](https://www.cnblogs.com/lipg/p/14291863.html) [centos2](https://blog.csdn.net/yexiaomodemo/article/details/80473411)

  + [github-page](https://github.com/rabbitmq/rabbitmq-server/releases?page=6)

+ 简单模式使用

  + 添加依赖

    + maven坐标![image-20220221104513615](https://home.innky.xyz:25566/images/image-20220221104513615.png)
    + 弹幕说![image-20220221104445437](https://home.innky.xyz:25566/images/image-20220221104445437.png)

  + 建立连接![image-20220221104808601](https://home.innky.xyz:25566/images/image-20220221104808601.png)

  + 获取信道![image-20220221104826372](https://home.innky.xyz:25566/images/image-20220221104826372.png)

  + 声明队列![image-20220221105120907](https://home.innky.xyz:25566/images/image-20220221105120907.png)

  + 发送消息![image-20220221105255125](https://home.innky.xyz:25566/images/image-20220221105255125.png)

  + 在另一个类中接受消息

    ![image-20220221110921321](https://home.innky.xyz:25566/images/image-20220221110921321.png)

## WorkQueue

+ 工作队列（任务队列）
+ 各个线程交替接受消息
+ ![image-20220221164918555](https://home.innky.xyz:25566/images/image-20220221164918555.png)
+ 貌似所有的代码都和简单模式一样（只是启动了多个消费线程）
+ 应该是默认就是工作队列

### 消息应答

+ 自动应答：尽量少使用
+ 手动应答：
  + ![image-20220221173313940](https://home.innky.xyz:25566/images/image-20220221173313940.png)
  + multiple参数：（批量应答）相当于tcp累计确认
  + 实例：
    + ![image-20220221193932309](https://home.innky.xyz:25566/images/image-20220221193932309.png)
+ 消息不会丢失，未应答断开连接时消息会重新入队，交给其他消费者处理

### 持久化

+ 队列持久化	

  + 创建队列的时候第二个参数durable设为true

    ![image-20220221195643243](https://home.innky.xyz:25566/images/image-20220221195643243.png)

+ 消息持久化

  + 发送消息时候将第三个参数设置

    ![image-20220221195751637](https://home.innky.xyz:25566/images/image-20220221195751637.png)

### 不公平分发

+ 在所有的消费者的信道都加入 参数传1

  ![image-20220221195951886](https://home.innky.xyz:25566/images/image-20220221195951886.png)

+ 预取值参数不是1就是预取值

  ![image-20220221202036987](https://home.innky.xyz:25566/images/image-20220221202036987.png)

+ 弹幕说：该值类似于信道的缓存，即可以一次接收多少条未经确认的消息（最多堆积多少消息）

+ ![image-20220221202352281](https://home.innky.xyz:25566/images/image-20220221202352281.png)

## 发布确认

+ 队列向生产者发确认消息

+ 使用：在生产者信道调用![image-20220221204716987](https://home.innky.xyz:25566/images/image-20220221204716987.png)

+ 发布确认模式：

  + 单个确认发布：同步的

    + 使用waitForConfirms（）等待获取确认

      ![image-20220221205209559](https://home.innky.xyz:25566/images/image-20220221205209559.png)

  + 批量确认发布

    + 发了多条消息后调用一次waitForConfirms（）累计确认
    + 但是出错无法知道具体是哪条出错

  + 异步批量确认

    + 只管发送，当有没收到的broker会通知发送方重传

    + 实现：

      + 添加监听器，需要传入成功回调和失败回调

        ![image-20220221210653409](https://home.innky.xyz:25566/images/image-20220221210653409.png)

        + 回调参数![image-20220221210722984](https://home.innky.xyz:25566/images/image-20220221210722984.png)

      + 处理未确认的消息![image-20220221210938393](https://home.innky.xyz:25566/images/image-20220221210938393.png)

        + 视频中使用了一个**线程安全**的Map，在发送消息时将发布的下一个id与当前放在Map中![image-20220221211610612](https://home.innky.xyz:25566/images/image-20220221211610612.png)
        + 在回调确认时候在Map中删除已确认的消息
          + 注：如果为批量确认要单独处理![image-20220221212449066](https://home.innky.xyz:25566/images/image-20220221212449066.png)

## 交换机

+ 发布、订阅模式

  ![image-20220221212835224](https://home.innky.xyz:25566/images/image-20220221212835224.png)

### Exchanges

+ 类型

  ![image-20220221213043524](https://home.innky.xyz:25566/images/image-20220221213043524.png)

+ 声明一个交换机![image-20220221213943370](https://home.innky.xyz:25566/images/image-20220221213943370.png)

  + 声明多次交换机似乎不影响

+ 无名exchange 使用""表示默认交换

+ 创建临时队列

![image-20220221213237724](https://home.innky.xyz:25566/images/image-20220221213237724.png)

+ 绑定：交换机通过不同的RoutingKey绑定不同的队列

  ![image-20220221214218245](https://home.innky.xyz:25566/images/image-20220221214218245.png)

+ Fanout：交换机模式，将消息广播给绑定的所有的队列，该模式绑定时候RoutingKey随便填（可以直接填空串），只要绑定了就行

  + 使用交换机后就是使用RoutingKey来确认给哪个队列发消息了，不用使用队列的名称
    + 猜想：可能默认的无名exchange交换机是使用队列名称进行绑定的

+ Direct：交换机模式，根据绑定RoutingKey进行路由
  + 声明![image-20220221215914742](https://home.innky.xyz:25566/images/image-20220221215914742.png)
  + 支持多对一、一对多（实现类似fanout的方式和多个key映射到同一个队列）

+ Topic：routingkey为点分的单词列表

  + 可以使用统配规则

  ![image-20220222085350338](https://home.innky.xyz:25566/images/image-20220222085350338.png)

  + ![](https://home.innky.xyz:25566/images/image-20220222085436668.png)
  + 声明![image-20220222085704561](https://home.innky.xyz:25566/images/image-20220222085704561.png)


##  死信队列

+ 来源

  ![image-20220222090627324](https://home.innky.xyz:25566/images/image-20220222090627324.png)

+ 出现如上问题转发到死信交换机转发至死信队列

+ 使用

  + 死信交换机与死信队列和普通的一样

  + 不过在声明普通队列时候需要带上参数，指明死信交换机与死信routingkey

    ![image-20220222095336424](https://home.innky.xyz:25566/images/image-20220222095336424.png)

  + 创建死信发生条件

    + 在发送消息的时候也设置了ttl？？？![image-20220222095753931](https://home.innky.xyz:25566/images/image-20220222095753931.png)

    + 创建队列时指定最大队列长度

      ![image-20220222101132348](https://home.innky.xyz:25566/images/image-20220222101132348.png)

    + 拒绝消息，且需要设置不放回队列![image-20220222101401133](https://home.innky.xyz:25566/images/image-20220222101401133.png)

## 整合SpringBoot

+ 添加依赖

  ```xml
  <dependency>
     <groupId>org.springframework.boot</groupId>
     <artifactId>spring-boot-starter-amqp</artifactId>
  </dependency>
  <dependency>
      <groupId>org.springframework.amqp</groupId>
      <artifactId>spring-rabbit-test</artifactId>
      <scope>test</scope>
  </dependency>
  ```

+ 修改配置文件连接信息

  ```properties
  spring.rabbitmq.host=localhost
  #spring.rabbitmq.port=
  spring.rabbitmq.username=guest
  spring.rabbitmq.password=guest
  ```

+ 创建配置类，在其中声明交换机和队列

  + 使用@Bean创建交换机

    ![image-20220222105435294](https://home.innky.xyz:25566/images/image-20220222105435294.png)

  + 创建队列，使用Builder![image-20220222105638310](https://home.innky.xyz:25566/images/image-20220222105638310.png)

  + 声明绑定

    ![image-20220222110145735](https://home.innky.xyz:25566/images/image-20220222110145735.png)

+ 发送消息

  + 自动注入模板对象![image-20220222110627620](https://home.innky.xyz:25566/images/image-20220222110627620.png)

  + 使用模板对象发送消息

    ![image-20220222110702826](https://home.innky.xyz:25566/images/image-20220222110702826.png)

  + 发送消息设置参数

    ![image-20220222112535042](https://home.innky.xyz:25566/images/image-20220222112535042.png)

+ 接受消息：创建监听器

  + 创建一个消费者类（使用@Component注解放入容器）
  + 在类的方法上方加入@RabbitListener()注解
    + ![image-20220222111113565](https://home.innky.xyz:25566/images/image-20220222111113565.png)
    + Message的包不能导错![image-20220222111022733](https://home.innky.xyz:25566/images/image-20220222111022733.png)
    + Channel也不能导错包（弹幕说用不到的可以不写）

## 延迟队列

+ 使用场景

  ![image-20220222101928446](https://home.innky.xyz:25566/images/image-20220222101928446.png)

+ 其实就是利用死信队列延迟ttl

+ 设置ttl

  + 队列设置ttl  =》仅适用于该队列

    + 队列ttl其实是当前第一个元素的等待时间限制
    + 就是说，队列并发得到5个消息未被处理，则没过ttl时间送走一个，而不是同时被送走

  + 发送的消息设置ttl =》比较灵活，可以自定义时间

    + 当发送多条时候

      ![image-20220222113006932](https://home.innky.xyz:25566/images/image-20220222113006932.png)

  + **同时生效时会怎样：按短的来**

+ 延迟插件 [插件列表](rabbitmq.com/community-plugins.html) 其中的 rabbitmq_delayed_message_exchange

  + 拷贝至plugin目录-> rabbitmq-plugins enable rabbitmq_delayed_message_exchange

  + 原理：延迟在交换机里

    ![image-20220222151845342](https://home.innky.xyz:25566/images/image-20220222151845342.png)

  + 使用：

    + 创建延迟交换机返回CostomExchange

      ![image-20220222152250653](https://home.innky.xyz:25566/images/image-20220222152250653.png)

    + 但是要配置参数type为direct

    + 发送消息时候要指定延时时间

      ![image-20220222152546616](https://home.innky.xyz:25566/images/image-20220222152546616.png)

## 发布确认高级

### Spring方式发布确认

+ 需要在配置文件中开启

  ![image-20220222154029371](https://home.innky.xyz:25566/images/image-20220222154029371.png)

  + 默认是NONE
  + simple模式可以向之前一样实现同步确认

+ 发送消息时候附带上CorelationData

  ![image-20220222155732500](https://home.innky.xyz:25566/images/image-20220222155732500.png)

+ 实现一个 RabbitTemplate.ConfirmCallback放入容器中

  + 接口方法参数

    ![image-20220222155058266](https://home.innky.xyz:25566/images/image-20220222155058266.png)

    ![image-20220222155109925](https://home.innky.xyz:25566/images/image-20220222155109925.png)

  + 将该对象注入到rabbitTemplate中![image-20220222155454427](https://home.innky.xyz:25566/images/image-20220222155454427.png)

### 回退消息

+ 默认routing无效直接丢弃

+ 启用回退

  ![image-20220222160257848](https://home.innky.xyz:25566/images/image-20220222160257848.png)

+ 实现回退回调接口

  ![image-20220222160411741](https://home.innky.xyz:25566/images/image-20220222160411741.png)

+ 实现方法

  ![image-20220222160619600](https://home.innky.xyz:25566/images/image-20220222160619600.png)

  + 新版只有一个参数![image-20220222160535575](https://home.innky.xyz:25566/images/image-20220222160535575.png)

### 备份交换机

+ 原理：当发现不可路由时交给备份交换机

  ![image-20220222161259111](https://home.innky.xyz:25566/images/image-20220222161259111.png)

+ 实现：交换机绑定备份交换机--使用ExchangeBuilder

  ![image-20220222161336735](https://home.innky.xyz:25566/images/image-20220222161336735.png)

+ 当备份交换机和回退回调同时存在时，备份交换机有限

## 其他知识点

### 幂等性

+ 消息重复消费
+ 解决方案
  + 唯一id+指纹码机制
  + 利用redis原子性
+ 利用 redis 执行 setnx 命令

### 优先级队列

+ 原理：![image-20220222162348129](https://home.innky.xyz:25566/images/image-20220222162348129.png)
+ 使用：
  + 在声明队列时候添加最大优先级参数![image-20220222162537775](https://home.innky.xyz:25566/images/image-20220222162537775.png)
  + 发送消息时候需要声明消息优先级![image-20220222162711895](https://home.innky.xyz:25566/images/image-20220222162711895.png)
  + 当消息积压在mq时候会按优先级进行排序

### 惰性队列

+ 直接存贮在磁盘，性能差
+ 当消息大量堆积的时候使用惰性队列节省内存
+ 内存中只存储索引
+ ![image-20220222162948981](https://home.innky.xyz:25566/images/image-20220222162948981.png)

### 集群

+ 搭建步骤
  + 不同机器修改hostname![image-20220222163523635](https://home.innky.xyz:25566/images/image-20220222163523635.png)
  + 配置hosts文件 将ip与主机名称绑定
  + 将cookie文件复制为同一个
  + 重启主机
  + 使用命令加入节点![image-20220222163754395](https://home.innky.xyz:25566/images/image-20220222163754395.png)
  + 可以链式添加所有的集群
  + 之后访问任意一台等同于访问一个整体
  + 脱离集群命令

+ 镜像队列
  + 默认交换机在集群中只存储1份
  + 使用镜像队列进行备份
  + 宕机会再复制一份，一直保持多份
  + 使用：
    + 在任一节点添加一个策略Policy

### 高可用负载均衡

+ 使用Haproxy+Keepalive

![image-20220222164718602](https://home.innky.xyz:25566/images/image-20220222164718602.png)

### federation联邦交换机

+ 启用插件![image-20220222164925654](https://home.innky.xyz:25566/images/image-20220222164925654.png)
+ 与镜像队列的区别：镜像队列是基于集群的，这个上下游同步是独立服务器的

### 联邦队列

![image-20220222165506682](https://home.innky.xyz:25566/images/image-20220222165506682.png)

### shovel

![image-20220222165729860](https://home.innky.xyz:25566/images/image-20220222165729860.png)

安装插件![image-20220222165748832](https://home.innky.xyz:25566/images/image-20220222165748832.png)

