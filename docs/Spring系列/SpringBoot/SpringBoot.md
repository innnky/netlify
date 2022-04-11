# SpringBoot

## 基础

### 引入

+ 微服务

+ maven阿里云镜像(配置settings.xml)

  ```xml
  <mirrors>
        <mirror>
          <id>nexus-aliyun</id>
          <mirrorOf>central</mirrorOf>
          <name>Nexus aliyun</name>
          <url>http://maven.aliyun.com/nexus/content/groups/public</url>
        </mirror>
    </mirrors>
   
    <profiles>
           <profile>
                <id>jdk-1.8</id>
                <activation>
                  <activeByDefault>true</activeByDefault>
                  <jdk>1.8</jdk>
                </activation>
                <properties>
                  <maven.compiler.source>1.8</maven.compiler.source>
                  <maven.compiler.target>1.8</maven.compiler.target>
                  <maven.compiler.compilerVersion>1.8</maven.compiler.compilerVersion>
                </properties>
           </profile>
    </profiles>
  
  ```

+ 创建springboot项目

  + 添加父工程以及依赖


```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.3.4.RELEASE</version>
</parent>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

</dependencies>
```

  + 创建启动类

    + 添加@SpringBootApplication
    + 创建main方法
      + SpringApplication.run(MainApplication.class,args)
    + 创建controlloer

  + 配置文件左右配置项目

    + [https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#application-properties](https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#application-properties)

  + 打包

    + 添加插件

      ```xml
       <build>
              <plugins>
                  <plugin>
                      <groupId>org.springframework.boot</groupId>
                      <artifactId>spring-boot-maven-plugin</artifactId>
                  </plugin>
              </plugins>
          </build>
      ```

    + 运行maven package命令

### 自动配置

+ 子项目会自动引入父项目的依赖
  + spring-boot-dependencies
  + 引入依赖不用写版本号
+ 自定义依赖版本

  + 添加properties标签，其中配置自定义的依赖版本
    + （使用的是maven的就近原则）
+ 使用starter
  https://docs.spring.io/spring-boot/docs/current/reference/html/using-spring-boot.html#using-boot-starter
+ spring入口run方法返回ioc容器
+ ![image-20220217100656077](https://home.innky.xyz:25566/images/image-20220217100656077.png)
  + 第一个注解顶三个下面的注解
+ 主程序所在的包极其子包都能被自动扫描，无需配置包扫描

  + 也可以手动指定![image-20220215160924695](https://home.innky.xyz:25566/images/image-20220215160924695.png)
+ ![image-20220215161026559](https://home.innky.xyz:25566/images/image-20220215161026559.png)
+ 自动配置项按需加载

#### 注解

+ 添加组件

  + **@Configuragion**

    + 等同于之前的spring配置文件

    + 使用**@Bean**添加组件

      + 方法名为组件id，返回值为组件示例
      + 方法参数：先试图byName注入，再尝试byType在容器中找同类的对象传入
      + 也可以将该注解放在类上方

    + 配置类本身也是组件

    + 注解属性proxyBeanMethod是否代理配置类方法

      + 外界无论对配置类注册组件的方法调用多少遍都是返回同一个对象

      + 解决组件依赖问题

        ![image-20220217094651501](https://home.innky.xyz:25566/images/image-20220217094651501.png)

      + false启动速度比较快

      + true类似xml中ref引用注入

  + @Import写在任意组件类上方（如controler）

    + ![image-20220217095044022](https://home.innky.xyz:25566/images/image-20220217095044022.png)
    + 调用无参构造，默认名字是全类名

  + @Conditional

    + 条件装入：当满足某条件时候进行组件注入
    + 叠了多个时候似乎是'与'的关系
    + 有很多子注解，使用子注解指定条件
      + @ConditionOnBean:当存在bean时注入
        + 加在类上
        + 加在Configuration组件的类注册方法上

  + @InportResource

    + 导入原来的xml配置文件

+ 配置绑定

  + @ConfigurationProperties(prefex="核心配置文件中属性的前缀")
    + 加在组件类的上方
  + @EnableConfigurationProperties(目标组件.class)
    + 加在Configuration组件类上方
    + 开启目标类的自动配置
    + 将目标类注册到容器中
    + （例如使用第三方类的功能）
    + 貌似还是需要在目标类上指定前缀

#### 自动配置原理

+ ![image-20220217100839821](https://home.innky.xyz:25566/images/image-20220217100839821.png)
+ 启动时默认全部加载，使用条件装配按需配置
+ ![image-20220217102944239](https://home.innky.xyz:25566/images/image-20220217102944239.png)
+ SpringBoot会自动配各种组件，但如果用户配了就以用户的有限

总结：

- SpringBoot先加载所有的自动配置类  xxxxxAutoConfiguration
- 每个自动配置类按照条件进行生效，默认都会绑定配置文件指定的值。xxxxProperties里面拿。xxxProperties和配置文件进行了绑定

- 生效的配置类就会给容器中装配很多组件
- 只要容器中有这些组件，相当于这些功能就有了

- 定制化配置

- - 用户直接自己@Bean替换底层的组件
  - 用户去看这个组件是获取的配置文件什么值就去修改。

+ debug=true 显示自动配置报告

#### 小技巧

+ 好玩的

  ![image-20220217153212971](https://home.innky.xyz:25566/images/image-20220217153212971.png)

+ lombok

  ![image-20220217153443871](https://home.innky.xyz:25566/images/image-20220217153443871.png)

  依赖-安装插件-@Data@ToString@AllArgConstructor@Slf4j(记录日志)

+ ![image-20220217153820707](https://home.innky.xyz:25566/images/image-20220217153820707.png)

  ctrl f9刷新项目

  弹幕说推荐jrebel（付费的 热更新）

+ Spring Initializer

## 配置文件

+ yaml

  + 默认字符串不用加引号
    + 单引号相当于raw格式类似python r'sds\nss'
    + 双引号可以使用转义
  + 列表[ ] 或 -
  + 字典{} 即行内可以直接和json一样
  + yaml和.properties共存则都生效
  + 默认日期格式用2019/9/11

+ ![image-20220217160010136](https://home.innky.xyz:25566/images/image-20220217160010136.png)

  编写自己的yml有自动提示

  打包插件

  ![image-20220217160151396](https://home.innky.xyz:25566/images/image-20220217160151396.png)

## Web开发

### 静态资源

+ 静态资源目录![image-20220217161015341](https://home.innky.xyz:25566/images/image-20220217161015341.png)

  可以直接/直接访问

  + 映射的是/**先找controller，找不到再找静态资源

+ 改变静态资源访问前缀和目录

  ![image-20220217161412899](https://home.innky.xyz:25566/images/image-20220217161412899.png)

  ![image-20220217161547367](https://home.innky.xyz:25566/images/image-20220217161547367.png)

  （弹幕说已过时，以弹幕为准）

  ![image-20220217192037873](https://home.innky.xyz:25566/images/image-20220217192037873.png)

+ webJars 以jq为例

  ![image-20220217161932839](https://home.innky.xyz:25566/images/image-20220217161932839.png)

  + 可以以webjars/访问到默认静态文件路径内的文件

+ 欢迎页与网站图标

  + 静态目录index.html
    + 配置访问前缀后似乎会出问题
  + 创建能处理index的controller
  + 小技巧：
    + 按住shift点刷新
    + ctrl + f5
    + 调试 网络 禁用缓存

### 请求映射

+ rest风格

  + 路径都一样，使用请求方法来区分增删改查

  + rest风格发请求必须这样写

  + ![image-20220217200737559](https://home.innky.xyz:25566/images/image-20220217200737559.png)

  + SpringBoot中需要手动开启（新版本默认开启）

    ![image-20220217200937183](https://home.innky.xyz:25566/images/image-20220217200937183.png)

  + 控制器中可以直接使用method来区分请求

    + 或者直接写PostMapping PutMapping DeleteMapping GetMapping
    + 可以一次传入多个值![image-20220219205601271](https://home.innky.xyz:25566/images/image-20220219205601271.png)

  + 原理：使用一个过滤器包装了的请求，并修改了方法

+ ![image-20220217203239870](https://home.innky.xyz:25566/images/image-20220217203239870.png)

### 参数传递

+ 路径变量@PathVariable

  ![image-20220217203531008](https://home.innky.xyz:25566/images/image-20220217203531008.png)

  发参数时这样发![image-20220217203639991](https://home.innky.xyz:25566/images/image-20220217203639991.png)

+ 获取请求头@RequestHeader

  ![image-20220217203825638](https://home.innky.xyz:25566/images/image-20220217203825638.png)

+ @RequestParam

  + 可以加默认值![image-20220223160643367](https://home.innky.xyz:25566/images/image-20220223160643367.png)
  + 拿到所有的请求参数放入map中

  ![image-20220217204005866](https://home.innky.xyz:25566/images/image-20220217204005866.png)

+ 获取cookie![image-20220217204104596](https://home.innky.xyz:25566/images/image-20220217204104596.png)

+ @RequestBody表单提交的数据

+ @RequestAttribute 类似jsp中获取request域中的属性

+ @MatrixVarible

  ![image-20220217204815304](https://home.innky.xyz:25566/images/image-20220217204815304.png)

  <img src="https://home.innky.xyz:25566/images/image-20220217205013958.png" alt="image-20220217205013958" style="zoom:50%;" />

  + 默认关闭（默认移除分号）

  + 开启方法：

    + 法1替换默认的WebMvcConfigurer=>创建一个实现WebMvcConfigurer的类重写configPathMatch方法放入容器

    ![image-20220217205705760](https://home.innky.xyz:25566/images/image-20220217205705760.png)

    + 法2使用bean直接返回一个WebMvcConfigurer
    + ![image-20220217205951514](https://home.innky.xyz:25566/images/image-20220217205951514.png)
  
+ 参数接收map类型和model默认是放在request域中放数据（返回的是同一个对象，但类型转成了不同的接口）

+ 原理：p32-
  + HamdlerMapping寻找能处理的handler-z>找controller
  + 遍历controler的方法参数, 在argumentResolvers中寻找能解析当前遍历到的方法参数的
  + ......
  + 自定义类型参数原理
  + 。。。策略模式
  + 自定义Converter
    + 在自定义WebMvcConfigurer中重写addFormatters方法
    + 调用rigistry.addConvertier

### 数据响应

+ 响应json springboot web的starter添加了相应的json依赖
  + 原理：
    1. 找到能处理ResponseBody的MethodRoesesser
    2. 找到能转换Object对象的Converter

+ 内容协商

  + 返回XML：

    + 引入依赖

      ```xml
      <dependency>
          <groupId>com.fasterxml.jackson.dataformat</groupId>
          <artifactId>jackson-dataformat-xml</artifactId>
      </dependency>
      ```

    + 因为浏览器默认的请求头Accept![image-20220219192322597](https://home.innky.xyz:25566/images/image-20220219192322597.png)

      中xml的优先级高于json，因此在导入了xml包后会自动返回xml

  + 原理：

    1. 找出客户端能接收的内容类型
       + 默认是基于请求头的内容协商
       + 可以开启基于请求参数的内容协商
    2. 找出服务器能产生的内容类型
    3. 双层遍历找出匹配的
    4. 所有匹配的按权重进行排序找出最佳匹配

  + 实现基于请求参数的内容协商

    + ![image-20220219194142258](https://home.innky.xyz:25566/images/image-20220219194142258.png)
    + 之后浏览器使用?format=xml就可以指定格式

  + 实现自定义MessageConverter

    + WebMvcConfigurer中重写![image-20220219195111542](https://home.innky.xyz:25566/images/image-20220219195111542.png)
    + 实现HttpMessageConverter
      + ![image-20220219195441528](https://home.innky.xyz:25566/images/image-20220219195441528.png)

  + 自定义内容协商策略

    + WebMvcConfigurer中重写

      ![image-20220219203817585](https://home.innky.xyz:25566/images/image-20220219203817585.png)

    + 添加自定义功能时候很可能覆盖原先框架的功能

### 视图解析

+ Thymleaf

  + 依赖

    ![image-20220219204421117](https://home.innky.xyz:25566/images/image-20220219204421117.png)

  + ![image-20220219204628230](https://home.innky.xyz:25566/images/image-20220219204628230.png)

  + 默认的视图解析器为template目录，后缀是.html

  + 配置项目默认前缀![image-20220219205241232](https://home.innky.xyz:25566/images/image-20220219205241232.png)

  + 通过/xxx.html是无法访问到模板引擎中的页面的，所有模板引擎的页面必须通过控制器转发才能够访问到

  + 解决登录后url刷新问题（表单重复提交问题）:使用redirect

    ![image-20220219210207787](https://home.innky.xyz:25566/images/image-20220219210207787.png)

+ Java se语法 Array.asList(...)将传入的所有参数转为列表

+ 请求参数放在请求域中

+ 原理

  + 通过遍历viewResolvers找到能处理的视图解析器
  + 通过视图解析器得到view方法

### 拦截器

+ 注册拦截器

  + WebMvcConfigurer中重写addInterception

    ![image-20220220103219906](https://home.innky.xyz:25566/images/image-20220220103219906.png)

  + 配置拦截路径addPathPatterns() .excludePathPatterns（）
  
+ 放行静态资源

  + 方法一： ![image-20220220103715295](https://home.innky.xyz:25566/images/image-20220220103715295.png)
  + 方法二 ：配置静态资源前缀路径：![image-20220220103745660](https://home.innky.xyz:25566/images/image-20220220103745660.png)


+ 原理：
  + ![image-20220220104733163](https://home.innky.xyz:25566/images/image-20220220104733163.png)
  + ![image-20220220104910019](https://home.innky.xyz:25566/images/image-20220220104910019.png)

### 文件上传

+ 前端

  + 上传多文件

    ![image-20220220105305672](https://home.innky.xyz:25566/images/image-20220220105305672.png)

+ 控制器获取上传文件及多文件

  ![image-20220220105727820](https://home.innky.xyz:25566/images/image-20220220105727820.png)

+ 保存到本地

  ![image-20220220105853678](https://home.innky.xyz:25566/images/image-20220220105853678.png)

+ 配置前缀 spring.servlet.multipart

### 异常处理

+ 默认机器返回json 浏览器返回html

+ 默认自定义错误页面
  + 静态资源目录error下 404 5xx
  + 模板引擎也行
  
+ 错误页面在模板中可以直接去到错误信息
  + [[${message}]]  
  
+ 原理
  + ErrorMvcAutoConfigurer
  
  + ![image-20220220190206090](https://home.innky.xyz:25566/images/image-20220220190206090.png)
  
  + 抛出异常：
  
    + 会寻找能够处理该异常的异常解析器（如手动配置的ExceptionHandler）（以及DefaultErrorAttributes会将异常数据写入request域）
    + 默认没有任何解析器能处理异常，则该异常会被转发到’/error‘
      + 如果有ExceptionHandler能处理异常，则相当于其代替controller得到mv
      + 如果异常有标注Http状态码则会被![image-20220220201307098](https://home.innky.xyz:25566/images/image-20220220201307098.png)处理，但依然会被![image-20220220202450946](https://home.innky.xyz:25566/images/image-20220220202450946.png)转发到error
    + 由![image-20220220195646836](https://home.innky.xyz:25566/images/image-20220220195646836.png)
      + 寻找能够解析的视图解析器，默认只有![image-20220220195926316](https://home.innky.xyz:25566/images/image-20220220195926316.png)
      + 解析出error/404 5xx.html
      + 400错误一般是传参错误，可以将404.html改成4xx.html
  
  + 自定义异常标注Http状态码![image-20220220201140243](https://home.innky.xyz:25566/images/image-20220220201140243.png)
  
  + 自定义异常解析器
  
    ![image-20220220201954181](https://home.innky.xyz:25566/images/image-20220220201954181.png)
  
    因为默认自定义异常解析器会在最后，而前面的异常解析器已经返回了mv了，所以轮不到它，使用Order提高其优先级

### 原生组件注入

+ 注册原生组件

  + 方法1

    + 首先要在启动类上方扫描![image-20220220202704211](https://home.innky.xyz:25566/images/image-20220220202704211.png)
    + 在servlet上方加入![image-20220220202615456](https://home.innky.xyz:25566/images/image-20220220202615456.png)
    + 在filter上方加入![image-20220220202906131](https://home.innky.xyz:25566/images/image-20220220202906131.png)
    + 在listener上方加入![image-20220220202932486](https://home.innky.xyz:25566/images/image-20220220202932486.png)

  + 方法2

    + 在容器中放入Bean(要包裹一层)

      ![image-20220220203101765](https://home.innky.xyz:25566/images/image-20220220203101765.png)![image-20220220203224062](https://home.innky.xyz:25566/images/image-20220220203224062.png)
      
      + 添加初始化参数：.addInitParameter

+ DispatcherServlet原理，配置项是spring.mvc

  + 也是通过Bean方式启用

+ 切换web服务器![image-20220220204455954](https://home.innky.xyz:25566/images/image-20220220204455954.png)

  + 首先排除tomcat依赖，再加入undertow的依赖![image-20220220204658463](https://home.innky.xyz:25566/images/image-20220220204658463.png)
  + 定制
    + 配置文件主要再server前缀
    + 手动放一个![image-20220220204923330](https://home.innky.xyz:25566/images/image-20220220204923330.png)
    + 使用定制化器![image-20220220205006522](https://home.innky.xyz:25566/images/image-20220220205006522.png)
    + ![image-20220220205019696](https://home.innky.xyz:25566/images/image-20220220205019696.png)通过在容器中放一个定制化器来改变系统的默认规则

### 定制化原理总结

+ 修改配置文件；
+ **xxxxxCustomizer；**

- **编写自定义的配置类   xxxConfiguration；+** **@Bean替换、增加容器中默认组件；视图解析器** 
- **Web应用 编写一个配置类实现** **WebMvcConfigurer 即可定制化web功能；+ @Bean给容器中再扩展一些组件**
- @EnableWebMvc + WebMvcConfigurer —— @Bean  可以全面接管SpringMVC（导致WebMvcAutoConfiguration直接失效），所有规则全部自己重新配置； 实现定制和扩展功能

### 套路

+ 整合新功能基本都是
  + 场景starter** **- xxxxAutoConfiguration - 导入xxx组件 - 绑定xxxProperties --** **绑定配置文件项** 

## 数据库

### 原生sql

+ 导入starter

  ```xml
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-data-jdbc</artifactId>
      </dependency>
  ```

+ 导入mysql驱动

  ```xml
      <dependency>
          <groupId>mysql</groupId>
          <artifactId>mysql-connector-java</artifactId>
          </dependency>
  
  配置版本
      <properties>
          <java.version>1.8</java.version>
          <mysql.version>5.1.49</mysql.version>
      </properties>
  ```

+ 数据源配置前缀spring.datasource

  ```yaml
  spring:
    datasource:
      url: jdbc:mysql://localhost:3306/db_account
      username: root
      password: 123456
      driver-class-name: com.mysql.jdbc.Driver
  ```

+ 自己没有配置数据源的时候会自动配置数据源

  + starter自动配置了![image-20220223100337159](https://home.innky.xyz:25566/images/image-20220223100337159.png)数据源

+ 容器中已经自动放了一个jdbcTemplate对象，配置前缀是spring.jdbc.template

  ```java
  @Autowired
  JdbcTemplate jdbcTemplate;
  ```

### Druid

+ 引入依赖

  ```xml
      <dependency>
          <groupId>com.alibaba</groupId>
          <artifactId>druid</artifactId>
          <version>1.1.17</version>
      </dependency>
  ```

+ 手动导入数据源

  + 写一个配置类，向容器中放一个Druid数据源
  + 使用@ConfigurationProperties("spring.datasource")绑定属性
  + 配置监控页：在容器中放一个ServletRegistrationBean（包裹一个StatViewServlet对象）
    + 数据源添加过滤器![image-20220223103535793](https://home.innky.xyz:25566/images/image-20220223103535793.png)
  + 配置![image-20220223103711863](https://home.innky.xyz:25566/images/image-20220223103711863.png)
    + 在容器中放一个Filter
  + https://github.com/alibaba/druid/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98

+ 使用starter

  ```xml
  <dependency>
     <groupId>com.alibaba</groupId>
     <artifactId>druid-spring-boot-starter</artifactId>
     <version>1.1.17</version>
  </dependency>
  ```

  + 配置项

    + 扩展配置项 **spring.datasource.druid**
    + DruidSpringAopConfiguration.**class**,   监控SpringBean的；配置项：**spring.datasource.druid.aop-patterns**

    - DruidStatViewServletConfiguration.**class**, 监控页的配置：**spring.datasource.druid.stat-view-servlet；默认开启**

    -  DruidWebStatFilterConfiguration.**class**, web监控配置；**spring.datasource.druid.web-stat-filter；默认开启**

    - DruidFilterConfiguration.**class**}) 所有Druid自己filter的配置

  + 配置示例


```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/db_account
    username: root
    password: '000508'
    driver-class-name: com.mysql.cj.jdbc.Driver
    
    druid:
      aop-patterns: com.atguigu.admin.*  #监控SpringBean
      filters: stat,wall     # 底层开启功能，stat（sql监控），wall（防火墙）

      stat-view-servlet:   # 配置监控页功能
        enabled: true
        login-username: admin
        login-password: admin
        resetEnable: false

      web-stat-filter:  # 监控web
        enabled: true
        urlPattern: /*
        exclusions: '*.js,*.gif,*.jpg,*.png,*.css,*.ico,/druid/*'
      filter:
        stat:    # 对上面filters里面的stat的详细配置
          slow-sql-millis: 1000
          logSlowSql: true
          enabled: true
        wall:
          enabled: true
          config:
            drop-table-allow: false

    
```

### Mybatis

+ 导入starter

  ```xml
      <dependency>
          <groupId>org.mybatis.spring.boot</groupId>
          <artifactId>mybatis-spring-boot-starter</artifactId>
          <version>2.1.4</version>
      </dependency>
  ```

+ 配置前缀mybatis

  + 实例：

    ```yaml
    mybatis:
      config-location: classpath:mybatis/mybatis-config.xml  #全局配置文件位置
      mapper-locations: classpath:mybatis/mapper/*.xml  #sql映射文件位置
    ```

  + 之后就和之前一样使用mybatis（idea似乎可以装插件）

    + 创建全局配置文件（里面配置项留空，因为都配好了）（可以不写）
      + 使用mybatis.configuration属性中修改总配置文件信息
      + 如开启驼峰命名映射
        + 配置文件![image-20220223110855434](https://home.innky.xyz:25566/images/image-20220223110855434.png)
        + 等效于![image-20220223110941879](https://home.innky.xyz:25566/images/image-20220223110941879.png)
    + 创建mapper/接口名.xml namespace指定接口类名 添加标签绑定方法
    + 创建实体类与接口（接口需要标注@Mapper注解）

  + 注解方式使用：

    + 直接在接口方法上加注解@Select @Update
    + 可以与mapper文件配合使用

  + 可以在增加的时候将自增的主键放到传入参数的id属性中![image-20220223112211543](https://home.innky.xyz:25566/images/image-20220223112211543.png)

+ 总结步骤

  + 引入mybatis-starter
  + **配置application.yaml中，指定mapper-location位置即可**

  - 编写Mapper接口并标注@Mapper注解

  - 简单方法直接注解方式

  - 复杂方法编写mapper.xml进行绑定映射

  - *@MapperScan("com.atguigu.admin.mapper") 简化，其他的接口就可以不用标注@Mapper注解*

### MyBatisPlus

+ 使用mybatisx插件

+ 引入starter

  ```xml
      <dependency>
          <groupId>com.baomidou</groupId>
          <artifactId>mybatis-plus-boot-starter</artifactId>
          <version>3.4.1</version>
      </dependency>
  ```

+ 前缀**mybatis-plus**

+ ![image-20220223155315881](https://home.innky.xyz:25566/images/image-20220223155315881.png)设置表中不存在的元素

+ 简化mapper：继承BaseMapper

+ ![image-20220223155417936](https://home.innky.xyz:25566/images/image-20220223155417936.png)当表名和实体类名不同时使用该注解

+ 简化业务层：接口继承IService，实现类继承ServiceImpl![image-20220223160012696](https://home.innky.xyz:25566/images/image-20220223160012696.png)

+ ![image-20220223160727457](https://home.innky.xyz:25566/images/image-20220223160727457.png)

+ 分页插件![image-20220223161048693](https://home.innky.xyz:25566/images/image-20220223161048693.png)

+ 重定向传参![image-20220223161639100](https://home.innky.xyz:25566/images/image-20220223161639100.png)

## 单元测试

+ 引入starter

  ![image-20220223162017366](https://home.innky.xyz:25566/images/image-20220223162017366.png)

  + 兼容junit4

+ 简介

  ![image-20220223162224804](https://home.innky.xyz:25566/images/image-20220223162224804.png)

### 常用注解

+ @DisplayName("测试显示名称")
  + 可以标在方法、类上方
+ @Test
+ @BeforeEach 在其他各个单元测试执行之前执行
+ @AfterEach
+ @BeforeAll @AfterAll
  + 必须是静态方法
  + 在类上运行测试的时候在所有测试开始结束的时候执行
+ @Disabled 跳过当前测试
+ @TimeOut()
  + ![image-20220223163008008](https://home.innky.xyz:25566/images/image-20220223163008008.png)
  + 超出时间出异常
+ @SpringBootTest是符合注解，包含了
+ @RepeatTest(6)重复测试5次

### 断言

+ 断言机制在运行结束后会有详细的测试报告

+ 导包![image-20220223163842153](https://home.innky.xyz:25566/images/image-20220223163842153.png)

  因为主要是静态方法

+ 简单断言

  + 相等![image-20220223163626379](https://home.innky.xyz:25566/images/image-20220223163626379.png)
  + 同一对象![image-20220223163704802](https://home.innky.xyz:25566/images/image-20220223163704802.png)
  + 前面的断言执行失败，后面的代码都不会执行

+ 数组断言![image-20220223164017562](https://home.innky.xyz:25566/images/image-20220223164017562.png)

+ 组合断言

  + ![image-20220223164048528](https://home.innky.xyz:25566/images/image-20220223164048528.png)
  + ![image-20220223164128148](https://home.innky.xyz:25566/images/image-20220223164128148.png)
  + 所有断言都成功才成功

+ 异常断言

  + ![image-20220223164351838](https://home.innky.xyz:25566/images/image-20220223164351838.png)

+ 超时断言

+ 快速失败![image-20220223164447993](https://home.innky.xyz:25566/images/image-20220223164447993.png)

### 前置条件

+ ![image-20220223164732427](https://home.innky.xyz:25566/images/image-20220223164732427.png)
+ 区别：
  +  断言会测试失败
  + 前置条件失败会跳过该次测试，和disabled一样
+ 用来在不同条件下执行不同的测试方法

### 嵌套测试

+ 使用内部类，并且在内部类上方加上@Nested
+ 内层的测试可以驱动外层的（beforeEach之类的），外层的不能驱动内层的

### 参数化测试

+ ![image-20220223165715802](https://home.innky.xyz:25566/images/image-20220223165715802.png)
+ 需要添加![image-20220223165742588](https://home.innky.xyz:25566/images/image-20220223165742588.png)注解（代替@Test)
+ 通过标注![image-20220223165832527](https://home.innky.xyz:25566/images/image-20220223165832527.png)之类的注解知名参数
+ ![image-20220223170017209](https://home.innky.xyz:25566/images/image-20220223170017209.png)

## 指标监控

+ Sprint Actuator

+ 引入starter

  ```xml
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-actuator</artifactId>
      </dependency>
  ```

+ 通过 http://localhost:8080/actuator/** 使用

+ 开启web暴露所有监控断点

  ```yaml
  management:
    endpoints:
      enabled-by-default: true #暴露所有端点信息
      web:
        exposure:
          include: '*'  #以web方式暴露
  ```

+ /beans /conditions自动配置 /configprops配置属性 /env /metrics查看所有指标名 /metrics/指标名

+ 监控端点

  + 最常用的

    + **Health：监控状况**
    + **Metrics：运行时指标**

    - **Loggers：日志记录**

+ 对端点的具体配置

  ![image-20220223211355600](https://home.innky.xyz:25566/images/image-20220223211355600.png)

+ 禁用全部端点后手动开启部分端点

  ```yaml
  management:
    endpoints:
      enabled-by-default: false
    endpoint:
      beans:
        enabled: true
      health:
        enabled: true
       
  ```

+ 定制端点

  + 定制健康信息：实现接口，并放入容器（类名必须以Indicator结束）![image-20220223212332368](https://home.innky.xyz:25566/images/image-20220223212332368.png)![image-20220223212318538](https://home.innky.xyz:25566/images/image-20220223212318538.png)

  + 定制info信息

    + 法一：配置文件

      ```yaml
      info:
        appName: boot-admin
        version: 2.0.1
        mavenProjectName: @project.artifactId@  #使用@@可以获取maven的pom文件值
        mavenProjectVersion: @project.version@
      ```

    + 法二：编写实现类-实现InfoContributer（类名结尾命名最好Contributer）![image-20220223212827105](https://home.innky.xyz:25566/images/image-20220223212827105.png)

  + 定制matrics信息

    ```java
    class MyService{
        Counter counter;
        public MyService(MeterRegistry meterRegistry){
             counter = meterRegistry.counter("myservice.method.running.counter");
        }
    
        public void hello() {
            counter.increment();
        }
    }
    
    
    //也可以使用下面的方式
    @Bean
    MeterBinder queueSize(Queue queue) {
        return (registry) -> Gauge.builder("queueSize", queue::size).register(registry);
    }
    ```

+ 新增监控端点

  ```java
  @Component
  @Endpoint(id = "container")
  public class DockerEndpoint {
  
      @ReadOperation
      public Map getDockerInfo(){
          return Collections.singletonMap("info","docker started...");
      }
  
      @WriteOperation
      private void restartDocker(){
          System.out.println("docker restarted....");
      }
  
  }
  ```

+ 图形化监控

  + 创建一个独立的项目做服务器

    + 引入starter

    ![image-20220223213943988](https://home.innky.xyz:25566/images/image-20220223213943988.png)

    + 启动类添加注解

    ![image-20220223214003640](https://home.innky.xyz:25566/images/image-20220223214003640.png)

    + 修改端口（避免冲突）

  + 在客户端

    + 引入starter![image-20220223214149583](https://home.innky.xyz:25566/images/image-20220223214149583.png)

    + 配置监控服务器地址

      ![image-20220223214354115](https://home.innky.xyz:25566/images/image-20220223214354115.png)

      注意preferip

## 高级特性

### Profiles

+ 创建多个不同环境的配置文件

  ![image-20220224091954816](https://home.innky.xyz:25566/images/image-20220224091954816.png)

+ 在主配置文件中声明当前使用的环境

  ![image-20220224092033702](https://home.innky.xyz:25566/images/image-20220224092033702.png)

+ 指定了环境后同名配置文件以环境配置优先

+ 命令行方式指定环境![image-20220224092258912](https://home.innky.xyz:25566/images/image-20220224092258912.png)

  命令行方式也可以改别的配置项，且命令行方式优先级最高

+ 条件装配

  + 在指定环境下才放入容器，根据环境切换配置

  ![image-20220224092833703](https://home.innky.xyz:25566/images/image-20220224092833703.png)

  + 也可以表在配置类的方法上方

  ![image-20220224092905664](https://home.innky.xyz:25566/images/image-20220224092905664.png)

+ profile分组

  ![image-20220224093231480](https://home.innky.xyz:25566/images/image-20220224093231480.png)

### 外部化配置

+ 配置来源

  ![image-20220224093822403](https://home.innky.xyz:25566/images/image-20220224093822403.png)

+ 可以放配置文件的位置

  ![image-20220224094000829](https://home.innky.xyz:25566/images/image-20220224094000829.png)

  + 后面的覆盖前面的

### 自定义starter

+ 结构![image-20220224095712516](https://home.innky.xyz:25566/images/image-20220224095712516.png)

  + 创建starter包：

    + 引入自动配置包
    + 引入各种依赖

  + 创建自动配置包：

    + 清理项目结构![image-20220224100122731](https://home.innky.xyz:25566/images/image-20220224100122731.png)

    + 编写类，但不要放入容器

      ![image-20220224100107659](https://home.innky.xyz:25566/images/image-20220224100107659.png)

    + 编写自动配置类

      ![image-20220224100232121](https://home.innky.xyz:25566/images/image-20220224100232121.png)

    + 在类资源路径下创建文件![image-20220224100715279](https://home.innky.xyz:25566/images/image-20220224100715279.png)

      ![image-20220224100658876](https://home.innky.xyz:25566/images/image-20220224100658876.png)

  + 将两个项目Clean Install

## SpringBoot原理解析

+ 启动过程

  + 创建spring应用
  + 运行SpringApplication

+ 自定义监听事件

  + 实现接口![image-20220224110232173](https://home.innky.xyz:25566/images/image-20220224110232173.png)

  + 在![image-20220224110304418](https://home.innky.xyz:25566/images/image-20220224110304418.png)文件中指定加载![image-20220224110416621](https://home.innky.xyz:25566/images/image-20220224110416621.png)

    还有几个是直接放容器中就能生效

[集成swagger](https://www.jianshu.com/p/55cbce0ecb16)
