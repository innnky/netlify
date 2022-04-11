 SpringMVC

+ 请求由SpringMVC内部的DispatcherServlet统一接收，并分发给Controller对象


## 引入

+ ![image-20220204160742894](https://home.innky.xyz:25566/images/image-20220204160742894.png)

+ 添加依赖SpringMVC servlet jsp

+ 在web.xml中注册DispatcherServlet

  ![image-20220131214732385](https://home.innky.xyz:25566/images/image-20220131214732385.png)

  +  默认是第一次访问Servlet时创建对象，使用load-on-startup在启动时创建

  + 中央调度器在初始化时候会**创建Spring容器**

    + 默认读取的Spring配置文件为/WEB-INFO/<servlet名>-servlet.xml

    + 使用<init-param>手动指定配置文件位置

      ![image-20220131215235002](https://home.innky.xyz:25566/images/image-20220131215235002.png)

  + 配置mapping

    ![image-20220131215529057](https://home.innky.xyz:25566/images/image-20220131215529057.png)

    

+ 创建index.jsp

+ 创建控制器类

  + 类上方加入@Controller
  + 方法上加入@RequestMapping
    + 可以放在方法上
    
    + 也可以放在类上
    
    + 可以指定多个value
    
      ![image-20220204084624035](https://home.innky.xyz:25566/images/image-20220204084624035.png)
  + 方法返回值ModelAndView
    + addObject(key,value)
    + setView("res.jsp")

+ 创建显示结果的jsp

+ 创建Spring配置文件

  + 声明组件扫描器，指定@Controller的包
  + 声明视图解析器

+ 两个过程

  + DispatcherServlet创建过程（理解）
  + 请求处理过程（理解）（转发流程图）

+ 用户访问控制：将页面文件放到WEB-INF目录下

  ![image-20220204084224443](https://home.innky.xyz:25566/images/image-20220204084224443.png)

+ 视图解析器

  + 配置：在spring配置文件添加bean

    ![image-20220204084454685](https://home.innky.xyz:25566/images/image-20220204084454685.png)

  + 可以省略前后缀

## 注解式开发

### RequestMapping

+ 放在类上方作所有请求地址的公共部分
+ 属性
  + value
  + method，值为RequestMethod枚举类型

### 参数接收

+ 四类参数
  + HttpServletRequest
  
  + HttpServletResponse
  
  + HttpSession
  
  + 请求中所传递的参数
  
    + 逐个接收
  
      ![image-20220204142450177](https://home.innky.xyz:25566/images/image-20220204142450177.png)
  
      + 框架会自动进行类型转换，拿到参数后可以直接使用（但可能会转换失败）
    
      + 如果希望能接收空的，基本数据类型可以换成包装类
    
      + 请求参数名称与函数名不同：在形参前加@RequestParam(value="请求参数名",required=请求是否必须有改参数)
    
      + post处理乱码：get无乱码，post有乱码
    
        + 在过滤器中设置，可以使用框架提供的CharactorEncodingFilter
    
        + 在web.xml中配置
    
          ![image-20220204155504305](https://home.innky.xyz:25566/images/image-20220204155504305.png)
    
          ![image-20220204155528573](https://home.innky.xyz:25566/images/image-20220204155528573.png)
    
    + 对象接收：一次接收多个参数
    
      + 处理器方法的形参是对象，其属性名与参数名一样
      + 框架先调用无参构造，再调用set方法为属性赋值
      + 可以一次接收多个对象，框架会自动进行同名赋值
      + 也可以使用List，但是前端的传参较为复杂，因此使用较少

### 返回值处理

+ ModelAndView：同时使用数据和视图

+ String：仅返回视图，可以是逻辑名称或完整路径
  + 逻辑名称需要配置视图解析器
  + 仅能返回数据，但也可以通过手动在request对象中设置值
  + 完整路径不能配置视图解析器
  
+ void：不返回视图和数据

  + 通过操作response返回数据来响应ajax

+ 返回Object：仅返回数据，与视图无关

  + 实现步骤

    + 添加依赖，默认使用jackson
    + 配置文件中加入`<mvc:annotation-driven>`注解![image-20220204204307899](https://home.innky.xyz:25566/images/image-20220204204307899.png)添加注解时候需要注意加的是哪个域下的![image-20220204204724749](https://home.innky.xyz:25566/images/image-20220204204724749.png)
    + 需要添加@ResponseBody注解

  + 框架的处理流程

    ![image-20220204205348252](https://home.innky.xyz:25566/images/image-20220204205348252.png)

  + 多个数据可以直接返回List，会自动转换成json数组

  + 有@ResponseBody时，返回String返回的是数据而不是视图

    + 默认会有乱码，需要加入，此处之前设置的filter不生效（@ResponseBody不走过滤器）![image-20220204210413587](https://home.innky.xyz:25566/images/image-20220204210413587.png)

### 中央调度器url-pattern"/"

+ Tomcat默认会自动处理静态资源![image-20220204211315782](https://home.innky.xyz:25566/images/image-20220204211315782.png)

+ jsp会自动转换为已映射的servlet

+ Default servlet("/")表示处理静态资源和其他未映射请求

+ 中央调度器使用"/"则替代了默认servlet的功能，但默认情况无法处理静态资源

+ 解决办法：

  1. 方法一：在Spring配置文件中添加![image-20220204212209345](https://home.innky.xyz:25566/images/image-20220204212209345.png)![image-20220204212500852](https://home.innky.xyz:25566/images/image-20220204212500852.png)

     创建了一个controller将请求转发给tomcat默认servlet

  2. 方法二：

     ![image-20220204213541360](https://home.innky.xyz:25566/images/image-20220204213541360.png)

     **表示当前目录以及子目录下的所有文件

     也需要加注解驱动

     ![image-20220204213741282](https://home.innky.xyz:25566/images/image-20220204213741282.png)
     
     + 可以将所有资源放到一个目录内
     
       ![image-20220204214034000](https://home.innky.xyz:25566/images/image-20220204214034000.png)

### 地址相关问题

+ ![image-20220204214552196](https://home.innky.xyz:25566/images/image-20220204214552196.png)

  ![image-20220204214819119](https://home.innky.xyz:25566/images/image-20220204214819119.png)

+ 使用不带/的地址时候可能会出下面问题

  ![image-20220204215120981](https://home.innky.xyz:25566/images/image-20220204215120981.png)
  
  + 解决方案
  
    ![image-20220205161402280](https://home.innky.xyz:25566/images/image-20220205161402280.png)
  

## SSM整合开发

+ 引入

  ![image-20220205074704748](https://home.innky.xyz:25566/images/image-20220205074704748.png)

+ 步骤

  + 加依赖![image-20220205074755891](https://home.innky.xyz:25566/images/image-20220205074755891.png)
  + 配置web.xml
    + 注册DispatcherServlet
    + 注册Spring监听器
    + 注册字符集过滤器
  + 创建service，controller，dao，实体类的包
  + 编写spirngmcv，spring，mybatis的配置文件及数据库属性配置文件
  + 写各种实现p52

## SpringMVC核心技术

### 重定向与转发

+ 区别

  ![image-20220205162823163](https://home.innky.xyz:25566/images/image-20220205162823163.png)

+ forward与redirect：忽略视图解析器，需要指定完整路径

  ![image-20220205163200000](https://home.innky.xyz:25566/images/image-20220205163200000.png)

  ![image-20220205163605487](https://home.innky.xyz:25566/images/image-20220205163605487.png)

+ 重定向参数传递p55

  ![image-20220205163740596](https://home.innky.xyz:25566/images/image-20220205163740596.png)

### 异常处理

+ 采用统一全局的异常处理方案，采用AOC思想，将业务逻辑与异常处理解耦合

+ 步骤

  + conroller中抛出异常

  + 创建一个用于全局异常处理的类

    + 类上方加入@ControllerAdvice

    + 方法上方加入@ExceptionHandler

      ![image-20220205165952382](https://home.innky.xyz:25566/images/image-20220205165952382.png)

    + 处理异常逻辑

      + 记录异常日志、数据库，发生时间等信息
      + 发送通知给技术人员
      + 通知用户

    + 处理未定义的异常（默认异常处理）：@ExceptionHandler后面不跟参数

  + 配置Spring配置文件

    ![image-20220205170534152](https://home.innky.xyz:25566/images/image-20220205170534152.png)

### 拦截器

+ 引入

  ![image-20220205213118443](https://home.innky.xyz:25566/images/image-20220205213118443.png)

+ 使用

  + 定义类实现HandlerInterceptor接口
  + 在springmvc配置文件中声明，指定拦截的uri

+ ![image-20220205213217481](https://home.innky.xyz:25566/images/image-20220205213217481.png)

+ HandlerInterceptor接口

  + preHandle

    ![image-20220205213616075](https://home.innky.xyz:25566/images/image-20220205213616075.png)

    ![image-20220205213641125](https://home.innky.xyz:25566/images/image-20220205213641125.png)

  + postHandle

    ![image-20220205213835052](https://home.innky.xyz:25566/images/image-20220205213835052.png)

  + afterHandle

    ![image-20220205213946554](https://home.innky.xyz:25566/images/image-20220205213946554.png)

+ 声明拦截器：在springmvc.xml中

  ![image-20220205214149972](https://home.innky.xyz:25566/images/image-20220205214149972.png)

+ 多个拦截器

  + 框架会将多个拦截器按照声明的顺序放入ArrayList中

  + 多个调度器的执行顺序

    ![image-20220205220226745](https://home.innky.xyz:25566/images/image-20220205220226745.png)

    ![image-20220205220045268](https://home.innky.xyz:25566/images/image-20220205220045268.png)

+ 与过滤器的区别

  + ![image-20220205220515236](https://home.innky.xyz:25566/images/image-20220205220515236.png)
  + 过滤器是Servlet中的对象（tomcat创建），拦截器是框架中的（Springmvc容器中）
  + 实现的接口不同
  + 过滤器是用来设置request, response的参数、属性的，侧重对数据的过滤，拦截器是用来验证请求的，能截断请求
  + 过滤器只有1个执行时间点，拦截器有3个
  + 过滤器可以处理jsp，js，html等，拦截器拦截Controller请求，只能拦截能被DispatcherServlet分发的请求

## SpringMvc处理流程

+ ![image-20220205221607367](https://home.innky.xyz:25566/images/image-20220205221607367.png)

+ ![image-20220205222133567](https://home.innky.xyz:25566/images/image-20220205222133567.png)

+ ![image-20220205222455322](https://home.innky.xyz:25566/images/image-20220205222455322.png)

+ 

  
