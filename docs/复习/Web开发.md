# Web开发

## Spring

### IoC

+ BeanFactory和ApplicationContext

  + BeanFactory延迟初始化 有方法getBean(String beanName)
  + ApplicationContext基于BeanFactory

+ 管理Bean

  + @Autowired byType @Autowired + @Qualififier byName
  + @Scope 作用域
  + @PostConstruct、@PreDestroy 生命周期

+ 作用域

  ![image-20220502085502680](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502085502680.png)

+ 循环依赖问题

  + 能处理的: 单例模式下的setter循环依赖
    + 通过三级缓存解决,对象初始化第一步完成后提前放入singletonFactories(三级缓存)暴露出来(此时还未初始化完全)
  + 不能处理: 构造器循环依赖  非单例循环依赖

### AOP

+ AOP应用场景?
  + 事务处理
  + 日志记录
  + ...
+ AOP只能增强IoC容器中的Bean
+ CGLib性能高但创建时间长,对于需要频繁创建的对象可以使用JDK动态代理

### 事务

+ 分类:编程式事务 声明式事务

+ 事务传播行为

  ![image-20220502093950862](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502093950862.png)

+ ![image-20220502094144402](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502094144402.png)

## SpringMVC

+ 请求拦截
  + 拦截Controller:拦截器
  + 拦截包括静态资源的所有请求:过滤器
  + 拦截非Controller具体的Bean:AOP

## MyBatis

+ 分页: 手动编写分页效率高,mybatis分页是通过自动添加limit语句实现的,方便但效率低
+ 缓存机制
  + 一级缓存:默认启用不可关闭,SqlSession级别的缓存
    + 当方法参数完全相同时会返回缓存中的对象
  + 二级缓存:默认不启用,是SqlSessionFactory级别的缓存
    + 二级缓存是和命名空间绑定(及mapper文件)

## 其他

+ Spring定时任务线程池ThreadPoolTaskScheduler