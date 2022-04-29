

# Redis

## 引入

+ 默认端口6379
+ 安装
+ 命令行连接![image-20220225201243000](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225201243000.png)
+ select 5切换数据库
+ dbsize flushdb清空当前库 flushall清空全部库
+ 单线程+多路io复用

## 常用5大数据类型

+ key：

  + keys *
  + exists [key] 
  + type [key]
  + del [key] 直接删除
  + ulink [key] 非阻塞删除
  + expire [key] [time]
  + ttl [key]查看过期时间

+ 字符串String

  + 最基本的数据类型 是二进制安全的 最大512M
  + 常用命令
    + set [keyName] [keyValue] 多次设置覆盖之前的
    + get [keyName]
    + strlen key 字符串长度
    + append [key] [value]
    + **setnx** [key] [value] 不能覆盖替换，只能新建key（操作失败则跳过当前set）
    + incr/decr  [key]只能操作数字类型
    + incrby/decrby [key] [改变大小] 
    + 原子性：不会被线程调度打断的操作，incr等命令都是原子性的
    + msetnx [k1] [v1] [k2] [v2] ... 只有所有setnx都能执行成功才执行，否则一个都不执行
    + mset mget
    + getrange [key] [start] [end] 截取字符串范围
    + setrange key [start] [key] 从start位置覆盖当前字符串、
    + setex key 过期时间 value
  + 底层结构：简单动态字符串类似stringbuilder

+ 列表：

  + 底层是quicklist，两端插入效率高
    + ![image-20220225110648437](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225110648437.png)
  + 常用命令
    + lpush/rpush [key] [v1] [v2] .....
    + lpop/rpop [key] [count]
      + 值在键在，值光键亡
    + rpoplpush key1 key2 
    + lrange [key] [start] [end] 
    + 可以使用-1表示最后一个元素
    + lindex [key] [index]
    + llen [key] 获取列表长度
    + linsert [key] before [value] [nvalue] 在value前面加nvalue
    + lrem [key] [count] [value] 在value前面删除count个元素 不删除自身
    + lset [key] i [value]

+ 集合

  + 常用命令
    + sadd key v1 v2 ...
    + smembers key
    + sismember key value 查询在key中是否存在value值
    + scard key 返回元素个数
    + srem key value1 value2...
    + spop key 随机删除并返回一个值
    + srandmember key  [count] 随机取n个值 不删除
    + smove [source] [destination] [value] 移动值
    + sinter/sunion/sdiff k1 k2 返回交并差集
  + 数据结构：类似java中的hashset

+ hash

  + 类似Map<String,Object> field：value

  + 命令

    + hset <key><field><value>   给<key>集合中的 <field>键赋值<value>

      hget <key1><field>      从<key1>集合<field>取出 value 

      hmset <key1><field1><value1><field2><value2>...   批量设置hash的值

      hexists <key1><field>           查看哈希表 key 中，给定域 field 是否存在。 

      hkeys <key>                              列出该hash集合的所有field

      hvals <key>                               列出该hash集合的所有value

      hincrby <key><field><increment>为哈希表 key 中的域 field 的值加上增量 1  -1

      hsetnx <key><field><value>将哈希表 key 中的域 field 的值设置为 value ，当且仅当域 field 不存在

  + 数据结构 ziplist hashtable

+ Zset

  + 类似treeset

  + zadd <key><score1><value1><score2><value2>…

  + **zrange <key> <start> <stop> [WITHSCORES]** 

  + zrangebyscore key min max [withscores] [limit offset count]

    返回有序集 key 中，所有 score 值介于 min 和 max 之间(包括等于 min 或 max )的成员。有序集成员按 score 值递增(从小到大)次序排列。 

    zrevrangebyscore key maxmin [withscores] [limit offset count]        

    同上，改为从大到小排列。 

  + zincrby <key><increment><value>   为元素的score加上增量

  + zrem <key><value>删除该集合下，指定值的元素

    zcount <key><min><max>统计该集合，分数区间内的元素个数 

    zrank <key><value>返回该值在集合中的排名，从0开始。

  + 数据结构 hash+跳表

## 配置文件

+ 单位
+ 包含关系
+ 网络相关配置
  + 远程访问
    + bind 远程连接需要删掉
    + protect-mode要设为false
  + timeout 0永不超时
  + tcp-keepalive
+ 通用配置
  + pidfile
  + loglevel 日志级别
  + logfile日志文件路径 默认为空
  + database默认有16个库
+ 安全配置
+ LIMITS

## 发布订阅

+ 频道

  ![image-20220225114737741](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225114737741.png)

+ ![image-20220225114823726](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225114823726.png)客户端连接

+ 订阅channel![image-20220225114857221](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225114857221.png)

+ 发布信息![image-20220225114908756](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225114908756.png)

## 新数据类型

+ Bitmaps
  + setbit<key><offset><value>
  + getbit<key><offset>
  + bitcount<key>[start end] 统计1数量
  + bitop and(or/not/xor) <destkey> [key…]
+ HyperLogLog
  + 用于解决基数问题，类似set但不能存储元素，只能统计数量
  + pfadd <key> <element>
  + pfcount <key> [key ...] 
  + pfmerge <destkey><sourcekey> [sourcekey ...]
+ Geographic
  + geoadd <key> < longitude><latitude><名称> [longitude latitude member...] 添加 
  + geopos <key><member> [member...]  取值
  + geodist<key><member1><member2> [m|km|ft|mi ] 获取两个位置之间的直线距离
  + georadius<key>< longitude><latitude>radius m|km|ft|mi  以给定的经纬度为中心，找出某一半径内的元素

## jedis

+ 引入依赖

  ```xml
  <dependency>
  <groupId>redis.clients</groupId>
  <artifactId>jedis</artifactId>
  <version>3.2.0</version>
  </dependency>
  
  ```

+ 创建对象`Jedis jedis = new Jedis("192.168.137.3",6379);`

+ 测试是否连接成功`String pong = jedis.ping();`

+ 关闭连接`jedis.close();`

### 操作redis

+ jedis实例方法
  + .keys("*")
  + .set(k,v) .get(k) .mset(k1,v1,k2,v2) .mget(k1,k2)
  + .lpush(k, v) 
  + .sadd(k, v1,v2) .smembers(key)
  + .....
+ 实例：手机验证码
  + 生成个位随机数![image-20220225202508276](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225202508276.png)
  + key命名![image-20220225202616960](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225202616960.png)
  + setex(k, t, val)

## SpringBoot 整合

+ 引入starter

  ```xml
  <dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-data-redis</artifactId>
  </dependency>
  
  <!-- spring2.X集成redis所需common-pool2-->
  <dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-pool2</artifactId>
  <version>2.6.0</version>
  </dependency>
  
  ```

+ 修改配置文件

  ```properties
  #Redis服务器地址
  spring.redis.host=192.168.140.136
  #Redis服务器连接端口
  spring.redis.port=6379
  #Redis数据库索引（默认为0）
  spring.redis.database= 0
  #连接超时时间（毫秒）
  spring.redis.timeout=1800000
  #连接池最大连接数（使用负值表示没有限制）
  spring.redis.lettuce.pool.max-active=20
  #最大阻塞等待时间(负数表示没限制)
  spring.redis.lettuce.pool.max-wait=-1
  #连接池中的最大空闲连接
  spring.redis.lettuce.pool.max-idle=5
  #连接池中的最小空闲连接
  spring.redis.lettuce.pool.min-idle=0
  
  ```

+ 创建配置类

+ 在Controller中使用

  ```java
  @RestController
  @RequestMapping("/redisTest")
  public class RedisTestController {
      @Autowired
      private RedisTemplate redisTemplate;
  
      @GetMapping
      public String testRedis() {
          //设置值到redis
          redisTemplate.opsForValue().set("name","lucy");
          //从redis获取值
          String name = (String)redisTemplate.opsForValue().get("name");
          return name;
      }
  }
  ```

## 事务

+ 事务用来防止运行期间其他命令插队
+ 命令
  + Multi 组队将命令放到队列中
  + Exec执行命令
  + 组队过程中Discard放弃组队
+ 例![image-20220225204419087](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225204419087.png)
+ 关于出错
  + 组队期间出错所有命令都不执行
  + 运行期间某条命令出错，其他命令能成功执行

### 事务冲突问题

+ 悲观锁：操作前上锁
+ 乐观锁：在数据上加上版本：适用于多读的场景
  + WATCH <key>
  + 执行了这句之后知道提交执行事务命令期间若<key>被修改则放弃事务
  + unwatch

### Redis事务三特性

+ Ø 单独的隔离操作 
+ Ø 没有隔离级别的概念 
+ Ø 不保证原子性 

### 秒杀案例

+ 通过ab模拟![image-20220225212356487](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225212356487.png)
+ ab --help
+ -n请求次数 -c并发数 -T contentType -p postfile  
+ 使用事务
  + watch![image-20220225213700357](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225213700357.png)
  + 开启事务![image-20220225213737347](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225213737347.png)
  + 执行![image-20220225213801551](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225213801551.png)
+ 乐观锁导致库存遗留问题
  + 解决方案：使用lua脚本（可以写redis原子操作）
  + ![image-20220225215151845](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220225215151845.png)
  + 思索：貌似是变成悲观锁了，用javaSyndronized似乎也可以？
    + 用lua大概是可以使用redis内部的多路复用？或许性能更高？

## 持久化

弹幕说这里好多文档上有的没讲

## RDB

+ 以指定的时间间隔将数据集的快照写入磁盘
+ 默认开启
+ 写时复制
+ 修改配置文件 /etc/redis.conf
  + dbfilename
  + dir ./
  + stop writes on bgsave error
  + rdb xxxx 是否压缩 是否校验
  + save指定写入时机 
+ save手动保存 bgsave自动保存

## AOF

+ Append Only File
+ 配置文件
  + appendonly 默认关闭 
  + appendonlyfile 我忍存储位置
  + appendfsync always/everysecond/no
+ aof与rdb同时开启时优先从aof中恢复
+ 服务启动时会自动加载当前目录下aof文件
+ 异常恢复![image-20220226122008615](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226122008615.png) <filename>
+ 重写压缩操作：大于64M*(1+100%)时候使用rewrite压缩

## 读写复制

+ 1主多从
+ 作用![image-20220226151643440](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226151643440.png)
+ 配置：
  + 创建多份配置文件
  + 公共配置关闭aof
  + 在分配置文件中引入公共的include
  + 分配置![image-20220226152221745](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226152221745.png)
  + 启动三个redis服务![image-20220226154048378](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226154048378.png)
  + 在从机执行![image-20220226152652714](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226152652714.png)（默认都是主服务器)
+ linux![image-20220226152516827](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226152516827.png)
+ 查看主从模式![image-20220226152618479](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226152618479.png)
+ 在从机中只能使用读操作，不能写

+ 特点

  + 一主两仆

    + 从服务器重启后需要重新设置主服务器

    + 从服务器重连后会自动同步

    + 主服务器宕机 从服务器不做任何事情

    + 主从同步通过rdb文件

      ![image-20220226154536015](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226154536015.png)

  + 薪火相传

    + 从服务器可以再挂从服务器![image-20220226154819276](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226154819276.png)

  + 反客为主

    + 使用![image-20220226155005764](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226155005764.png)将从机变成主机

+ 哨兵模式：反客为主自动版本

  + 步骤
    + ![image-20220226155333840](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226155333840.png)
    + 哨兵配置文件中![image-20220226155416140](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226155416140.png)
      + 最后一个参数为投票通过数量
    + 从机配置文件中修改优先级![image-20220226160740852](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226160740852.png)
      + 值越小优先级越高
    + 启动哨兵进程![image-20220226155457699](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226155457699.png)
  + 主机宕机后选择一个从机作为主服务器，原主机重新启动只能变成从机
  + 存在复制延时
  + 哨兵可以有多个（弹幕）
  + 选择从机![image-20220226160827296](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226160827296.png)
  + java连接（貌似是只要连哨兵？）

## 集群

+ 解决：容量不够、并发写
+ redis3.0：无中心化集群
+ 责任链？？
+ 水平扩容，每个节点只存储1/N
+ 使用步骤
  + 创建很多配置文件一个集群至少有3个主节点
  + 分配置文件中修改集群相关配置![image-20220226162818773](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226162818773.png)
  + 启动所有节点
  + 合并所有节点
    + ![image-20220226163305041](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226163305041.png) <ip1> <ip2> ....
      + 其中![image-20220226163343952](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226163343952.png)
      + 貌似需要在src目录下执行
      + 命令执行成功返回总slot数量，以及插槽在各主机的范围分配
  + 以![image-20220226163709160](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226163709160.png)连接（-c以集群连接)
  + 查看节点信息![image-20220226163721644](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226163721644.png)
+ ![image-20220226163942705](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226163942705.png)
+ 设值时通过key计算出目标插槽，通过插槽值确定存在哪个机器中
+ 添加多个值：使用分组![image-20220226164447461](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226164447461.png)
  + 计算插槽使用user计算
+ 集群命令
  + ![image-20220226164639014](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226164639014.png)查询key对应的插槽
  + ![image-20220226164822931](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226164822931.png)
  + ![image-20220226164611346](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226164611346.png)
+ 集群貌似会自动开启哨兵
+ ![image-20220226165053840](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226165053840.png)某段主从全挂掉后其他能否提供服务
+ Jedis操作集群
  + 连接![image-20220226165305079](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226165305079.png)
  + 可以用set存多个ip![image-20220226165359925](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226165359925.png)
+ 不足![image-20220226165440700](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226165440700.png)

## Redis应用问题

### 缓存穿透

+ 服务器压力突然增大
+ redis命中率降低，导致一直访问数据库
+ 原因：出现非正常url访问
+ 
  + 对空置作缓存：将有效时间设短
  + 设置可访问的白名单：使用bitmap设置可访问的白名单，不在白名单的禁止访问
  + 采用布隆过滤器
  + 进行实时监控

### 缓存击穿

+ 现象
  + 数据库访问压力瞬时增大
  + redis并出现大量key过期，且redis正常运行
+ 原因
  + 某个刚过期的key突然被大量访问
+ 解决方案：
  + 预先设置热门数据
  + 实时调整热门key的过期时间
  + 使用锁（会降低效率）

### 缓存雪崩

+ 现象
  + 数据库压力过大
  + 极少时间段key大量过期
+ 解决方案：
  + 构建多级缓存
  + 使用锁或队列
  + 设置过期标志更新缓存
  + 将缓存失效时间分散开

### 分布式锁

+ 使用setnx实现分布式锁

  + 申请锁setnx key1 10
  + 设置过期时间解决占了锁一直不释放的问题expire
  + 释放锁del key1
  + 使用![image-20220226200911054](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226200911054.png)同时上锁和设置ttl

+ 使用java代码实现

  ![image-20220226201328111](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226201328111.png)

+ 误删除别人的锁：

  + 上锁的时候将uuid存入![image-20220226201740216](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226201740216.png)
  + 释放锁的时候检查是否uuid是否一样再删除

+ 删除的原子性：使用lua脚本实现

## Redis新功能

+ acl![image-20220226203009667](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226203009667.png)
  + acl list展现用户权限列表
  + acl cat
  + acl setuser <username>
  + acl whoami
  + ......
+ IO多线程
  + 默认不开启![image-20220226203052516](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226203052516.png)
+ 工具支持cluster(集群)

## 应用

+ 对象缓存的两种方式

  ![image-20220326160752375](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220326160752375.png)

+ 
