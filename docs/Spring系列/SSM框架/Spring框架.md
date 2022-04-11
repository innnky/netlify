# Spring

+ 轻量
+ 针对接口编程，解耦合
+ Aop编程
+ 方便集成其他框架

## 控制反转IOC

+ 概念：Inversion of Control 把对象的创建、赋值、管理工作交给代码以外的容器实现

+ 作用：实现不同功能时减少对代码的改动（解耦合）

+ ![image-20220129095143297](https://home.innky.xyz:25566/images/image-20220129095143297.png)

+ 技术实现：DI依赖注入

+ 实现步骤：

  + 添加maven依赖
  + 创建类（接口及实现类）
  + 创建配置文件
  + 使用

+ 添加依赖

  ![image-20220129104906772](https://home.innky.xyz:25566/images/image-20220129104906772.png)

+ 配置文件 applicationContext.xml

  + beans是根标签
  + bean子标签 用来创建对象
    + id属性自定义名称 class属性为全限定名称 
    + scope="prototype" 同一个对象创建多次

+ 使用

  + 步骤

    + 创建容器ApplicationContext 使用其实现类ClassPathXmlApplicationContext("从类路径开始的spring配置文件路径")
    + 调用容器的getBean("beanid")获取bean

  + 代码![image-20220129100514516](https://home.innky.xyz:25566/images/image-20220129100514516.png)

  + 创建时机:spring容器创建时会创建所有bean

  + 获取容器中所有的对象

    ![image-20220129101126915](https://home.innky.xyz:25566/images/image-20220129101126915.png)

  + spring创建对象默认调用的是无参构造方法

+ ![image-20220129104626595](https://home.innky.xyz:25566/images/image-20220129104626595.png)

### DI依赖注入

>  创建对象给属性赋值

+ 实现方式

  + 基于XML的di实现
  + 基于注解的di实现
+ 语法分类

  + set注入:使用set方法进行注入
  + 构造注入:调用有参构造方法进行注入

### XML实现

+ set设值注入

  + 简单类型![image-20220129102109573](https://home.innky.xyz:25566/images/image-20220129102109573.png)

  + 引用类型

    ![image-20220129103428881](https://home.innky.xyz:25566/images/image-20220129103428881.png)

+ 构造注入(了解)

  ![image-20220129103834785](https://home.innky.xyz:25566/images/image-20220129103834785.png)

  + 构造注入若是按序传参则可以省略index

+ 细节

  + 设值注入只要有"set属性"方法就可以执行(不一定非要有属性)
  + 即使是int型的变量,xml语法规定必须放在双引号中
  + spring配置文件中创建对象不用关心顺序
  + spring容器中的对象默认是**单例**的

+ 引用类型自动注入

  + 按名称注入（byName）

    ![image-20220129132239490](https://home.innky.xyz:25566/images/image-20220129132239490.png)

  + 按类型注入

    ![image-20220129132623293](https://home.innky.xyz:25566/images/image-20220129132623293.png)

    + 如果匹配多个会直接报错

+ 多配置文件

  + 分配方式

    + 按模块分
    + 按类的功能：事务相关、数据库相关

  + 实现方式

    + 单独指定

      ![image-20220129134948425](https://home.innky.xyz:25566/images/image-20220129134948425.png)

    + 使用通配符

      ![image-20220129135204040](https://home.innky.xyz:25566/images/image-20220129135204040.png)

      + 必须在某一级目录下
      + 不能包含自己

### 注解实现

+ 使用步骤

  + maven依赖spring-context(会间接加入spring-aop)

  + 类中加注解

  + 配置文件中扫描

    ![image-20220129140123412](https://home.innky.xyz:25566/images/image-20220129140123412.png)

+ 注解

  + @Component(value = "xxx")
    + 等同于<bean id ="xxx" class="全限定类名">，创建的对象是唯一的
    + value=可以省略
    + 甚至可以不指定value 省略()
      + 默认首字母小写
    
  + ![image-20220129141114169](https://home.innky.xyz:25566/images/image-20220129141114169.png)
    + 用法和Component一样，但有不同的功能
    + 用来给项目对象分层
    
  + @Value 简单属性赋值
  
    + 放在属性上方
    + 放在set方法上方
  
  + @Autowired()
  
    + byType方式（默认）![image-20220129200117899](https://home.innky.xyz:25566/images/image-20220129200117899.png)
  
    + byName方式
  
      ![image-20220129195950142](https://home.innky.xyz:25566/images/image-20220129195950142.png)
  
  + @Resource：来自jdk，Spring提供支持，为引用赋值
  
    + 属性上方，无需set方法，推荐
    + set方法上方
    + 绑定方式
      + 默认是byName，若失败载使用byType
      + 只使用byName方式：使用属性name=""
  
+ 扫描多个包

  1. 使用多次组件扫描器
  2. 在包名处使用“;”分隔多个包
  3. 扫描父包（会递归扫描子包）

+ 注解方式与xml的区别

  + 代码经常改动时使用xml，不经常改的使用注解
  + 注解使用方便，阅读方便，

+ 属性配置文件

  + ![image-20220129201107308](https://home.innky.xyz:25566/images/image-20220129201107308.png)
  + ![image-20220129201126457](https://home.innky.xyz:25566/images/image-20220129201126457.png)
  + myage是test.propertieis中的key

+ IOC解耦合：实现业务对象之间的解耦合例如service和dao对象的解耦合

## 面向切面编程AOP

> 基于动态代理 两种方式都可以 是动态代理的规范化

+ Aspect：切面，目标类所添加的额外功能

  + 特点：一般是非业务方法，可独立使用

+ Orient：面向

+ Programming

+ 如何理解面向切面编程

  ![image-20220129204328548](https://home.innky.xyz:25566/images/image-20220129204328548.png)

+ 术语

  + JoinPoint：连接点，连接业务方法和切面的位置
  + PointCut：切入点，多个连接点方法的集合
  + Advice：通知。切面功能执行的时间

+ ![image-20220129204948689](https://home.innky.xyz:25566/images/image-20220129204948689.png)

+ 技术实现

  + Spring内部实现了AOP，主要在事务处理中使用
  + aspectJ框架，spring内部已经集成
    + 注解方式
    + xml配置文件方式

+ AOP作用

  ![image-20220130083138683](https://home.innky.xyz:25566/images/image-20220130083138683.png)

+ 什么时候用

  ![image-20220130083444103](https://home.innky.xyz:25566/images/image-20220130083444103.png)

  

### aspectj

+ ![image-20220129205324224](https://home.innky.xyz:25566/images/image-20220129205324224.png)

+ 切入点表达式

  ![image-20220129205608456](https://home.innky.xyz:25566/images/image-20220129205608456.png)

  + 使用

    <img src="https://home.innky.xyz:25566/images/image-20220129210122611.png" alt="image-20220129210122611" style="zoom:50%;" />

  + 举例

    <img src="https://home.innky.xyz:25566/images/image-20220129210206837.png" alt="image-20220129210206837" style="zoom:50%;" />

    <img src="https://home.innky.xyz:25566/images/image-20220129210230033.png" alt="image-20220129210230033" style="zoom:50%;" />

+ 实现步骤p52

  + 加入依赖spring 与aspectj
  + 创建目标类以及实现类
  + 创建切面类
    + 类上方加@Aspect注解
    + 方法上方加入@Before等注解
  + 创建配置文件
    + 声明目标对象
    + 声明切面对象
    + 声明自动代理生成器
  + 创建测试类

### 注解开发

+ 切面类@Aspect

  + 定义方法

    ![image-20220130081519371](https://home.innky.xyz:25566/images/image-20220130081519371.png)

  + 通知注解

    + @Before(value="切面表达式")

      + 在方法前执行，不改变方法执行结果

      + 同一个目标方法可以被注入多次

      + ![image-20220130083932554](https://home.innky.xyz:25566/images/image-20220130083932554.png)

        通过getArgs()获取参数

        + 如果有JoinPoint参数，则必须是第一个参数

    + @AfterReturning

      + ![image-20220130084443227](https://home.innky.xyz:25566/images/image-20220130084443227.png)

      + 方法定义

        ![image-20220130084612844](https://home.innky.xyz:25566/images/image-20220130084612844.png)

        + 可以通过参数获取返回值

    + @Around

      + ![image-20220130085314928](https://home.innky.xyz:25566/images/image-20220130085314928.png)

      + 方法定义

        ![image-20220130085243008](https://home.innky.xyz:25566/images/image-20220130085243008.png)

        + pgp.proceed()调用原先的方法
        + ProceedingJoinPoint继承自JoinPoint也可获取传入参数信息

    + @AfterThrowing

      + ![image-20220130090056065](https://home.innky.xyz:25566/images/image-20220130090056065.png)

      + 方法定义

        ![image-20220130090035882](https://home.innky.xyz:25566/images/image-20220130090035882.png)

    + @After

      + ![image-20220130090327764](https://home.innky.xyz:25566/images/image-20220130090327764.png)

+ @PointCut

  + ![image-20220130090712770](https://home.innky.xyz:25566/images/image-20220130090712770.png)
  + 之后便可以使用下方的方法名()代替定义的切入点表达式

+ 自动代理生成器

  + ![image-20220130081924236](https://home.innky.xyz:25566/images/image-20220130081924236.png)

+ 测试

  + 通过Spring获取目标对象并执行目标方法
  + 自己的理解
    + 生成代理对象的时候似乎是直接把原来的目标对象覆盖了
  + 目标类没有接口则自动使用CGlib动态代理
  + 期望在有接口时使用cglib![image-20220130091016832](https://home.innky.xyz:25566/images/image-20220130091016832.png)

## 集成MyBatis

+ 步骤

  ![image-20220130091924577](https://home.innky.xyz:25566/images/image-20220130091924577.png)

  ![image-20220130091953754](https://home.innky.xyz:25566/images/image-20220130091953754.png)

+ 使用Spring创建Druid连接池

  ![image-20220130093154895](https://home.innky.xyz:25566/images/image-20220130093154895.png)

+ 使用Spring创建SqlSessionFactory

  ![image-20220130094435640](https://home.innky.xyz:25566/images/image-20220130094435640.png)

+ 使用Spring创建dao对象

  ![image-20220130095003405](https://home.innky.xyz:25566/images/image-20220130095003405.png)

  spring整合mybatis时事务自动提交

+ 将数据库相关的配置单独放一个配置文件中，在主配置文件中引入

  ![image-20220130095934352](https://home.innky.xyz:25566/images/image-20220130095934352.png)

  使用${jdbc.url}进行访问p77

## Spring事务处理

+ 引入

  ![image-20220130101405044](https://home.innky.xyz:25566/images/image-20220130101405044.png)

  ![image-20220130101924360](https://home.innky.xyz:25566/images/image-20220130101924360.png)

  ![image-20220130102214302](https://home.innky.xyz:25566/images/image-20220130102214302.png)

  ![image-20220130102828317](https://home.innky.xyz:25566/images/image-20220130102828317.png)

  ![image-20220130103144642](https://home.innky.xyz:25566/images/image-20220130103144642.png)


### 注解方式

+ 中小项目，注解方案@Transactional

  + 注解属性指定隔离级别等属性

  + 步骤：

    + 声明事务管理器对象

      ![image-20220130105346237](https://home.innky.xyz:25566/images/image-20220130105346237.png)

    + 开启事务注解驱动（注意不要加错包中，是spring tx）

      ![image-20220130105331220](https://home.innky.xyz:25566/images/image-20220130105331220.png)

    + 在**公共**方法上方添加注解@Transactional

      ![image-20220130105320951](https://home.innky.xyz:25566/images/image-20220130105320951.png)

      + ![image-20220130105803395](https://home.innky.xyz:25566/images/image-20220130105803395.png)

### 配置文件方式

+ 大型项目 配置文件，使用aspectj框架

  + 声明式，与源代码完全分离

  + 使用步骤p93

    + 加入aspectj依赖

    + 声明事务管理器对象![image-20220130105346237](https://home.innky.xyz:25566/images/image-20220130105346237.png)

    + 声明方法需要的事务

      ![image-20220130113212526](https://home.innky.xyz:25566/images/image-20220130113212526.png)

      ![image-20220130113427200](https://home.innky.xyz:25566/images/image-20220130113427200.png)

    + 配置aop

      ![image-20220130113752275](https://home.innky.xyz:25566/images/image-20220130113752275.png)

## Web与Spring

使用监听器创建Spring容器对象![image-20220130115224873](https://home.innky.xyz:25566/images/image-20220130115224873.png)

获取容器

![image-20220130115730026](https://home.innky.xyz:25566/images/image-20220130115730026.png)