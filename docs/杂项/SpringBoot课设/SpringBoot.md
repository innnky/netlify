## SpringBoot 目录结构

![image-20211221220724413](https://home.innky.xyz:25566/images/image-20211221220724413.png)

其中.properties或.yaml二选一

### `application.yaml`记录

修改端口：

```yaml
server:
  port: 9090
```

## 配置依赖包

<img src="https://home.innky.xyz:25566/images/image-20211221221119877.png" alt="image-20211221221119877" style="zoom:67%;" />

<img src="https://home.innky.xyz:25566/images/image-20211221221027516.png" alt="image-20211221221027516" style="zoom:50%;" />

还有许多

## 连接数据库

<img src="https://home.innky.xyz:25566/images/image-20211221221335845.png" alt="image-20211221221335845" style="zoom:50%;" />

<img src="https://home.innky.xyz:25566/images/image-20211221221359189.png" alt="image-20211221221359189" style="zoom:50%;" />

<img src="https://home.innky.xyz:25566/images/image-20211221221445555.png" alt="image-20211221221445555" style="zoom:50%;" />

看版本选择是否加.cj

<img src="https://home.innky.xyz:25566/images/image-20211221221529144.png" alt="image-20211221221529144" style="zoom:50%;" />



## 配置各种其他依赖包

代码1

## 扫描相关

### 步骤

1. application.yaml 中配置jdbc连接以及mybatis连接
   + mybatis需要指明实体类所在的包entity（之后可以用小写代替类名）
   + mybatis需要指明映射文件所在的位置
2. 创建映射文件的存放目录
3. 创建entity包，并在包中创建实体类JavaBean
4. 创建dao包，并在其中创建接口，接口中创建查询方法
5. 在程序入口类中添加注解`@MapperScan(basePackages ="")`指明dao层所在位置
6. 编写映射xml文件，其中包含SQL语句，并且要指明所对应的dao接口

### 一些坑

+ `password: "000508"`要加引号

## thymeleaf

+ 类似jsp但是底层是基于ajax **???从HTML源码来看并没有基于Ajax？？？疑问**
+ 添加依赖、在application配置中添加，指明templates目录（存放html）
+ html中要指明thymeleaf语法，`xmlns:th="http://www.thymeleaf.org"`

#### 存在疑问

### 数据传递

+ 在控制器函数形参中添加`Map<String,Object> map`之后向其中放元素，键便是在html中访问时候使用的名字
+ HTML使用带`th：`的来访问元素如：
  + `th:text="${key_string}` 显示文本，其中可以用key_string.xxx来访问成员
  + ` th:text="${element}" th:each="element:${assa}"`进行遍历
    + 还可以在**标签内部**使用`[[${element}]]`来遍历
    + 利用`[[${}]]`方式可以同时输出多个值如`[[${element.aa}]]...[[${element.bb}]]`

+ HTML中引用静态元素：

  + 引用maven包中的`<link th:href="@{/webjars/bootstrap/4.5.0/css/bootstrap.css}" rel="stylesheet">`

    <img src="https://home.innky.xyz:25566/images/image-20220103190321934.png" alt="image-20220103190321934" style="zoom:66%;" />

  + 引用静态文件`<link th:href="@{/asserts/css/signin.css}" rel="stylesheet">`

    <img src="https://home.innky.xyz:25566/images/image-20220103190554135.png" alt="image-20220103190554135" style="zoom:67%;" />

  + 有时候静态资源加载不出来要点击Buiid->Rebuld Project

+ 控制器中获取表单提交数据（以name读取），需要在函数中添加形参，并需要注解

  `public String index(@Param("username") String username, @Param("password") String password)`

+ 控制器中返回值可以写重定向，语法是"redirect:/aa"

---

## 数据库操作注解方式

+ 通过在接口中方法上添加注解的方式实现映射文件的绑定
+ 查询@Select("select....") 修改@Update() .....
+ 参数传递接口方法中传入参数
  + 在select语句中使用`#{id}`访问传入的String变量id如`"select * from student where id=#{id}"`
  + 使用#{name}也可以直接访问到传入的Javabean对象的name成员

#### 数据库时如果出现乱码，连接时加上characterEncoding=utf8以及数据库中存储也要是utf8

---

## 单元测试

1. 在test中新建类
2. 为类添加@SpringBootTest注解
3. 为测试方法添加@Test注解
4. 存疑

---

## SpringBoot配置文件

1. 新建config包.MyMvcConfig类
2. 在类上方加入`@Configuration`注解
3. 新建一个方法，加上`@Bean`注解，返回值为WebMvcConfigurer
4. 方法体中直接返回new一个接口，实现其`addViewControllers`方法
5. 使用`registry.addViewController("/asd").setViewName("success");`实现类似filter的重定位功能
   + 这样可以实现多对一的url关系

---

## 语言切换

1. springboot配置文件中添加

```yaml
sprint:
    messages:
      basename: lan.login
```

+ resource目录新建lan目录，存放login.properties等
+ web中直接使用`th:text="#{login.username}"`进行访问
+ **坑爹的点** ：在不重新编译的时候可能显示不出来
+ 新建一个继承自`LocaleResolver`的类
+ 重写方法（未操作成功）

```java
public Locale resolveLocale(HttpServletRequest request) {
    String l = request.getParameter("l");
    System.out.println("kkkkkkkkkkkkkkkkkkkkkkkkkkkkk");
    if(l==null){
        l="zh_CN";
    }
    Locale locale = null;
    if(!StringUtils.isEmpty(l)){
        String[] sp = l.split("_");
        locale = new Locale(sp[0],sp[1]);
    }
    return locale;
}
```

#### 坑爹！！！！没弄成功

---

## Swagger

1. 添加maven依赖

2. 配置文件添加是否开启

```
   swagger:
     enable: true
```

3. 创建配置包
   + 添加 `@EnableSwagger2` 和`@Configuration`注解
   + 通过`@Value(value = "${swagger.enable}")`为类实例变量绑定配置文件值
   + 创建返回Bean的方法（包含两个方法）
4. 在对应的方法上方添加对应的注解
4. 详细参考 [https://zhuanlan.zhihu.com/p/98075551](https://zhuanlan.zhihu.com/p/98075551)

### 坑

+ 不知道为什么会报空指针异常，在启动类添加`@EnableWebMvc`解决

+ 不知道为什么无法访问，报`No mapping for GET /swagger-ui.html` 创建类

 ```java
  @Configuration
  public class WebMvcConfigurer extends WebMvcConfigurationSupport /*WebMvcConfigurerAdapter*/ {
  
      @Override
      public void addResourceHandlers(ResourceHandlerRegistry registry) {
  
          registry.addResourceHandler("swagger-ui.html").addResourceLocations(
                  "classpath:/META-INF/resources/");
          registry.addResourceHandler("/webjars/**").addResourceLocations(
                  "classpath:/META-INF/resources/webjars/");
          super.addResourceHandlers(registry);
  
      }
  
  }
 ```

  后解决

`@RestController = @Controller + @ResponseBody`

---

## 拦截器

1. 在config包下新建一个实现`HandlerInterceptor`接口的类

   + 实现该类的`preHandle`方法，返回值true代表放行请求

2. 在自己的Configurer类中实现方法`addInterceptors()`

   + 使用`registry.addInterceptor(new 刚刚新建的类).addPathPatterns("/**")`拦截全部请求

   + 使用`registry.addInterceptor(new 刚刚新建的类).addPathPatterns("/**").excludePathPatterns("/index")`来放行部分请求(可以使用“.jpg”进行匹配格式)

3. 在控制器中方法中可以通过增加一个参数`HttpSession session`来获取请求中的session对象，使用.setAttribute()和getAttribute()获取和设置属性





---

## 部分代码汇总

1

```xml
	<dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
    <dependency>
        <groupId>org.webjars</groupId>
        <artifactId>jquery</artifactId>
        <version>3.5.1</version>
    </dependency>
    <dependency>
        <groupId>org.webjars</groupId>
        <artifactId>bootstrap</artifactId>
        <version>4.5.0</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.8.0</version>
  </dependency>
    <dependency>
      <groupId>io.springfox</groupId>
      <artifactId>springfox-swagger-ui</artifactId>
      <version>2.8.0</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>druid-spring-boot-starter</artifactId>
        <version>1.1.10</version>
    </dependency>
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
        <version>2.1.4</version>
    </dependency>

    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.2</version>
    </dependency>
```

2

```yaml
spring:
  application:
    name: springboottest1
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    url: jdbc:mysql://localhost:3306/stu
    username: root
    password: '000508'
    driver-class-name: com.mysql.jdbc.Driver
  thymeleaf:
    prefix: classpath:/templates/
mybatis:
  type-aliases-package: com.innky.entity
  mapper-locations: classpath:mapping/*.xml

server:
  port: 9090
```

3

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://www.mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.innky.dao.StudentDao">

    <select id="selectStudents" resultType="student">
        SELECT t.* FROM stu.student t ORDER BY name
    </select>
</mapper>
```
