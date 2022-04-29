# vhr

## SpringSecurity

+ ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131743891.png)

  + 默认principal为一个字符串，认证走完会变成一个对象（自己定义的Hr）对象返回回去
    + 因此之后获取hr对象就可以直接用getPrincipal（）方法获取
  + 再执行完认证之后会擦除密码信息返回给前端

+ 配置放行静态页面文件（在SpringSecurity 的配置文件中重写方法）

+ ```java
  @Override
  public void configure(WebSecurity web) throws Exception {
      web.ignoring().antMatchers("/css/**", "/js/**", "/index.html", "/img/**", "/fonts/**", "/favicon.ico", "/verifyCode");
  }
  ```

+ ```xml
   <div class="markdown-body">
       <VueMarkdown :source="value" v-highlight></VueMarkdown>
   </div>
  ```

+ 

## 异常处理

采用了自定义实现一个CustomExceptionResolver，之后使用@Bean放入容器即可?????

+ 自定义一个类加上@RestControllerAdvice
+ 在方法上方加入@ExceptionHandler(异常类.class)

p30

## mybatis总结

+ 数据封装
  + 将多列数据封装进对象:使用`<association>`标签
  + 将多行数据封装进List:使用`<collection>`标签
+ 模糊查询
  + 使用${}进行拼接
  + 使用concat函数配合#{}拼接 

## 登录

+ 在el-form 中指定规则,规则为json对象
  + ![image-20220330093634957](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330093634957.png)
  + 之后将input包裹在el-form-item中,使用prop指定属性名称(用来和规则中校验属性名称进行匹配 )
  + 回车键登录![image-20220330165913125](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330165913125.png)

+ 在js中使用Element组件

  ![image-20220330130609579](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330130609579.png)

+ 创建代理

  + 新建vue.config.js
  + ![image-20220330131612110](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330131612110.png)

+ 封装axios(见代码)

+ 窗口存值window.sessionStorage.setItem('user', JSON.stringify(resp.obj))

+ router跳转有两个方法

  + push()
  + replace()

+ 将方法注册为实例方法

  ![image-20220330145203409](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330145203409.png)

  + 调用的时候直接![image-20220330145231299](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330145231299.png)

    

## home页面搭建

+ padiing在框的内部![image-20220330145551606](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330145551606.png)
+ 获取sessionStorage![image-20220330145759288](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330145759288.png)
+ 下拉框:
  + 在最外层元素绑定command方法,内部选项指定command属性
  + 之后点击哪一个选项会将其绑定的属性作为参数传入方法
+ 获取所有路由路径![image-20220330152023138](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330152023138.png)
+ 侧边栏如果添加router属性则不用手动写跳转,会自动以index为路由路径跳转

## 菜单数据

+ 菜单数据存放

  + ![image-20220330162546160](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330162546160.png)
  + vuex用来做数据共享:存储公共的数据

+ 使用Vuex

  + 定义

    ![image-20220330163217388](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330163217388.png)

  + 使用:在main.js中引入并在vue声明中使用 

  + 使用:![image-20220330164352530](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330164352530.png)

+ 元组解包![image-20220330164104067](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330164104067.png)

+  require为动态导入,也就是可以不用在文件开头import

+ 使用路由守卫加载菜单数据

  + 判定是正常跳转还是刷新跳转

    ![image-20220330164946419](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330164946419.png)

  + 添加路由![image-20220330165114296](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330165114296.png)

  + store配合conputed使用

  + 注销登录时需要清空store数据

+ 面包屑导航:从router中获取数据

  ![image-20220330170046832](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220330170046832.png)

+ 未登录后跳转相关

  + 添加redirect参数![image-20220331094431250](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220331094431250.png)
  + 获取当前地址栏中的请求参数redirect![image-20220331094510085](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220331094510085.png)
  + 浏览器访问可以省略斜杠,ajax不可以省略
  + insertSelective就是只上传不为空的字段
  + 加载页面时候调用方法应该放在mounted方法中(vue1中放在created)
  + eltable加入自定义列按钮![image-20220331102646334](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220331102646334.png)
  + 

## 职位管理

### 日期处理

+ 在model类中添加![image-20220402170722500](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220402170722500.png)

### Json对象拷贝

+ ![image-20220402171441082](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220402171441082.png)

### 提交与接收数组参数

+ 后端![image-20220402171654528](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220402171654528.png)
+ 前段![image-20220402172238976](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220402172238976.png)

## 权限组

+ 使用图标做按钮![image-20220405094028974](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405094028974.png) type="text"

+ 三层树形结构查询

  ![image-20220405095556701](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405095556701.png)

+ 同一个ref有多个的情况下 会自动获得一个数组,可以使用index取得想要的那一项![image-20220405101615608](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405101615608.png)

## 未登录跳转登录页

+ 后端返回401状态码
+ 前段在请求处理中根据状态码进行跳转

## 部门管理

+ 树形数据递归查询:

  + 使用mybatis![image-20220405105455565](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405105455565.png)
  + 即当为children属性赋值时,会去调用select属性的方法(自身)变完成了递归(将此列查出的id作为新的属性传入递归方法)
  + 递归的入口为树形数据的顶层节点id

+ vue watch

  ![image-20220405110030821](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405110030821.png)

  + 监控filterText值的变化

+ 定义存储过程

  + ![image-20220405111245578](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405111245578.png)

  + mybatis调用存储过程

    ![image-20220405111832459](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405111832459.png)

  + 接口方法返回值为空

## 操作员管理

+ 查询若不适用左连接可能出现为空值
+ 登录加载框![image-20220405154202174](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405154202174.png)
+ 可以放在任何位置,变量也是自己取名![image-20220405154638497](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405154638497.png)
+ 最简单只需要给一个v-loading属性即可

## 员工管理

+ 奇怪的语法![image-20220405161052525](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405161052525.png)

+   表格固定列右侧![image-20220405163544104](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405163544104.png)

+ input属性,出现一个清空的按钮![image-20220405164941873](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405164941873.png)

  + 也有回调![image-20220405165036452](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405165036452.png)

+ 日期选择器

  ![image-20220405170505104](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405170505104.png)

+ mysql还有枚举类型??

+ localStorage??sessionStorage???

+ 删除弹框![image-20220405193010253](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405193010253.png)

### 导出数据

+ 返回文件时候的Controller的返回参数![image-20220405194347276](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405194347276.png)

+ 导出excel工具类

  ![image-20220405194613201](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405194613201.png)

  ......

+ 文件上传保存![image-20220405195323521](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220405195323521.png)

+ p102

+ 自定义转换器(字符转转日期)

  ![image-20220406202329194](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220406202329194.png)

+ 
