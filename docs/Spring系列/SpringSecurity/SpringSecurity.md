

# SpirngSecurity

## 引入

### 权限管理

+ 认证
+ 授权
+ 解决方案
  + Shiro
  + SpringSecurity

### 整体架构

![image-20220228183844030](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228183844030.png)

+ 认证
  + AuthenticationManager
    + 为接口，仅有一个方法
    + 若抛出异常则认证失败，正常返回则认证成功
    + ![image-20220228184302104](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228184302104.png)也继承自AuthenticationManager，管理多个子的AuthenticationManager
  + Authentication
    + 接口方法的入参和返回值
    + 保存认证及认证成功信息
  + SecurityContextHolder
    + 获取登录后的用户信息
    + 请求时认证信息与线程绑定存入SecurityContextHolder
    + 请求结束将信息存入session
    + 下次请求自动从session中取出认证信息并存入SecurityContextHolder供使用
+ 授权
  + AccessDecisionManager
    + 决定此次访问是否允许 
  + AccessDecisionVoter
    + AccessDecisionManager保存多个Voter，会遍历所有的voter真正投票
  + ConfigAttribute
    + 保存角色授权信息

### 基本使用

+ 引入starter![image-20220228201930890](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228201930890.png)

+ 默认会保护所有页面，未登录重定向至/login 默认用户名user 密码在控制台中

+ 原理

  + 用的不是原生的filter
  + 使用![image-20220228202813104](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228202813104.png)（由spring框架实现)整合进原生filter
  + ![image-20220228202949820](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228202949820.png)管理springsecurity链
  + 原理图<img src="https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228203112134.png" alt="image-20220228203112134" style="zoom:50%;" />
  + 各种过滤器。。。

+ 自动配置原理

  + ![image-20220228204256079](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228204256079.png)在未自定义这两个bean时候会使用默认拦截

    + 默认的拦截规则![image-20220228204406608](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228204406608.png)

  + 默认重定向到login的原理

    ![image-20220228204655171](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228204655171.png)

  + ![image-20220228210550278](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228210550278.png)在未自定义以上4个类时会自动配置一个基于内存的![image-20220228210636942](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228210636942.png)

    + 其默认会产生一个user 配置文件前缀为spring.security.user.xxx
    + 可以修改默认的用户密码

+ 自定义的两个类：会覆盖默认的

  + WebSecurityConfigurerAdapter 拓展SpringSecurity所有默认配置
  + UserDetailService  单方法：传入用户名获取用户信息

## 自定义认证

### 自定义资源权限规则

+ 创建WebSecurityConfigurerAdapter 的子类
+ 重写config方法（**注意放行资源放在任何资源前面**）![image-20220228213242652](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228213242652.png)

### 自定义登录

+ 放行请求

+ ```java
  @Override
  public void configure(WebSecurity web) throws Exception {
      web.ignoring().antMatchers("/login");
  }
  ```

+ 自定义默认登录页

  + ![image-20220228214448838](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228214448838.png)

    + 放行登录控制器（转发到登录视图）
    + 指定默认登录页面
    + 指定登录请求url

  + 登录页面![image-20220228214058387](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228214058387.png)

    + 必须post请求
    + 参数名必须为username password
      + 也可以自定义![image-20220228214621152](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228214621152.png)
    + 请求地址必须为之前配置的
    + 关闭跨站请求保护![image-20220228214239095](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228214239095.png)

  + 成功跳转

    + ![image-20220228214726418](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228214726418.png)总是跳转至index

    + ![image-20220228214755086](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228214755086.png) 默认访问认证前试图访问的页面，也可以修改第二个参数**强制跳转**

    + 前后端分离模式登录成功跳转

      + 实现接口![image-20220228215251058](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228215251058.png)
      + 实现方法，返回json![image-20220228215428695](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228215428695.png) 
      + ![image-20220228215440569](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220228215440569.png)绑定回调


  + 失败跳转

    + forward存request域中，redirect存session中，默认redirect

    + 传统web![image-20220301090731155](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301090731155.png) 

    + 在前端拿到失败信息：从session或request中以![image-20220301091102040](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301091102040.png)为key

    + 前后端分离实现

      +  实现接口![image-20220301091309197](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301091309197.png)

      + 实现方法 返回json

        ![image-20220301091442324](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301091442324.png)

      + 绑定回调![image-20220301091426740](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301091426740.png)

+ 注销登录

  +  ![image-20220301094133230](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301094133230.png)
  + 设置多个登出请求![image-20220301094440871](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301094440871.png)
  + 前后端分离实现
    + 实现接口![image-20220301094815619](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301094815619.png)
    + 实现方法 返回json略
    + 绑定![image-20220301094850464](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301094850464.png)
  
+ 未登录不要重定向而是直接返回错误结果(用来替代.loginPage("/login"))

+ ```java
  .exceptionHandling().authenticationEntryPoint((httpServletRequest, httpServletResponse, e) -> {
      httpServletResponse.setContentType("application/json;charset=utf-8");
      PrintWriter writer = httpServletResponse.getWriter();
      RespBean res = RespBean.error("请求失败");
      String s = new ObjectMapper().writeValueAsString(res);
      writer.write(s);
    
      writer.flush();
      writer.close();
  });
  ```

### 登录数据获取

+ SecurityContextHolder ThreadLocal
+ 包含关系![image-20220301100007468](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301100007468.png)
+ 获取SecurityContext：存放策略
  + ![image-20220301100152373](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301100152373.png)只能在单个线程中使用，子线程无法获取数据
  + ![image-20220301100229296](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301100229296.png)多线程环境，可以在子线程中访问
  + ![image-20220301100257519](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301100257519.png)放在全局静态变量中，基本不适用
+ 在代码中获取![image-20220301100522548](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301100522548.png)
  + 可以将Authentication强转成User类然后getusername
  + 无法在子线程中获取
  + 修改系统参数，改变存放策略便可以在子线程中使用![image-20220301100938647](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301100938647.png)
+ 在页面中获取
  + 引入依赖![image-20220301101147207](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301101147207.png)
  + 命名空间![image-20220301101157817](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301101157817.png)
  + 获取认证信息![image-20220301101254254](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301101254254.png)

### 自定义认证数据源

+ 认证流程![image-20220301101557459](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301101557459.png)

+ 认证原理 ![image-20220301103849919](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301103849919.png)
  + 有全局的AuthenticationManager（实现类ProviderManager）和局部的，局部的共用一个全局的parent作为其备用资源
  + 每一个ProviderManager都有一个List<AuthenticationProvider>
  + 首先调用局部的，若失败再调用全局的
  + 全局ProviderManager中默认AuthenticationProvider实现为DaoAuthenticationProvider，通过UserDetailService实现认证
  + ![image-20220301171757856](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301171757856.png)
  + 结论：自定义UserDetailService

+ 配置全局AuthenticationManager
  + 配置**默认**的全局AuthenticationManager
    + ![image-20220301172751868](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301172751868.png)
    + 在springsecurity配置类中使用@Autowired绑定一个initialize方法
    + 参数中传入一个![image-20220301171213947](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301171213947.png)
  + 配置**自定义**的全局AuthenticationManager
    + 重写WebSecurityConfirgurerAdaptor的configure方法
    + 也传入了一个AuthenticationManagerBuilder
    + 使用了自定义的会覆盖默认的
    + ![image-20220301173211726](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301173211726.png)
      + 如果想对外暴露，则![image-20220301173453904](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301173453904.png)
    + 推荐使用自定义的
  + AuthenticationManagerBuilder 方法
    + ![image-20220301171655819](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301171655819.png)设置自己的UserDetailService
      + 手动创建一个基于内存的UserDetailService![image-20220301172042912](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301172042912.png)
    + 添加authenticationProvider![image-20220301172434388](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301172434388.png)
  + 如果只要覆盖UserDetailService，可以直接@Bean放一个自己的UserDetailService
    + 如果使用自定义的后就没有这个功能了

+ 自定义数据源实现

  + 创建表：

    + 创建用户表和角色表
    + 创建用户角色关联表，用户与角色为多对多关系

  + 创建实体类

    + 角色

      ```java
      public class Role {
          private Integer id;
          private String name;
          private String nameZh;
        	//get set..
      }
      ```

    + 用户类继承UserDetails，实现方法

      ```java
      public class User  implements UserDetails {
          private Integer id;
          private String username;
          private String password;
          private Boolean enabled;
          private Boolean accountNonExpired;
          private Boolean accountNonLocked;
          private Boolean credentialsNonExpired;
          private List<Role> roles = new ArrayList<>();
      
          @Override
          public Collection<? extends GrantedAuthority> getAuthorities() {
              List<GrantedAuthority> grantedAuthorities = new ArrayList<>();
              roles.forEach(role->grantedAuthorities.add(new SimpleGrantedAuthority(role.getName())));
              return grantedAuthorities;
          }
          
          get....
          set....
      }
      ```

      + 其他方法照常返回get
      + getAuthorities需要将自己的roles对象转化成GrantedAuthority的集合返回出去

  + 编写dao及mapper

  + 编写自己的UserDetailService实现类，实现方法

    ```java
        @Override
        public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
            User user = userDao.loadUserByUsername(username);
            if(ObjectUtils.isEmpty(user))throw new RuntimeException("用户不存在");
            user.setRoles(userDao.getRolesByUid(user.getId()));
            return user;
        }
    ```

    + 先查用户信息，再根据用户查询角色信息
    + 可以抛出UsernameNotFoundException

### 前后端分离案例

+ 需要创建![image-20220301204918694](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301204918694.png)的实现类，覆盖其attemptAuthentication方法

+ 改写其获取参数相关的代码

  ![image-20220301210014691](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301210014691.png)

+ 将fiter放入容器并配置相关（其中指定认证管理器比较繁琐，自定义认证管理器，指定userdetailservice, 暴露认证管理器）

  ![image-20220301210602314](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301210602314.png)。。。

+ 用自己写的filter替换系统的

  ![image-20220301205149856](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301205149856.png)

+ 未认证返回json![image-20220301211102911](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301211102911.png)

### 添加验证码

+ 传统web开发

  + 添加依赖![image-20220302105332368](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302105332368.png)（弹幕说使用hotool)

  + 容器中放一个对象![image-20220302105431535](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302105431535.png)

  + 新建一个controller获取验证码图片并放行该controller

    ![image-20220302105715600](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302105715600.png)

  + 新建自己的![image-20220301204918694](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220301204918694.png)![image-20220302110509302](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302110509302.png)

    + 自定义一个验证码不匹配的异常

  + 创建自定义的filter实例并配置其相关请求参数并放入容器

    ![image-20220302111021361](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302111021361.png)

  + 替换原有的filter![image-20220302110929814](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302110929814.png)

+ 前后端分离验证码

  + 返回验证码需要转化为base64编码之后以json返回

    ![image-20220302112102644](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302112102644.png)

## 密码加密

+ PasswordEncoder![image-20220302114714514](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302114714514.png)

  ![image-20220302114536975](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302114536975.png)

+ 使用

  + 灵活方式，不用配置
    + 使用![image-20220302115127695](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302115127695.png)将密码加密
    + 数据库中存储![image-20220302115158090](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302115158090.png)
  + 整个项目使用一种加密方式
    + 在容器中放一个![image-20220302115525645](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220302115525645.png)
    + 数据库中存储就不需要加`{加密方式}`
  
+ 密码自动更新

  + 自定义的UserDetailService 同时实现UserDetailPasswordService

## RememberMe

+ 回顾：注册基于内存的![image-20220329200718102](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329200718102.png)

+ 开启：
  + ![image-20220329201313971](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329201313971.png)
  + 使用.rememberMe()
  
+ 可选配置![image-20220329213222580](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329213222580.png)

+ 原理：会返回一个cookie，内容是

  + ![image-20220329213328604](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329213328604.png)
  + 用户名：过期时间：md5加密（用户名 密码 过期时间）
  + 后段校验的时候从数据库取出密码之后加密后与客户端发来的请求做对比

+ 提高安全性

  + token会自动更新

  + 内容只包含两个字段

  + 使用:

    + 自定义RememberMeService,使用特定的实现类,放入容器

      ![image-20220329221020141](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329221020141.png)

    + 在config中指定自定义的

      ![image-20220329220355686](/Users/xingyijin/Library/Application%20Support/typora-user-images/image-20220329220355686.png)

  + 指定记住我对应的页面

    ![image-20220329220606400](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329220606400.png)

  + 持久化令牌

    + 在自定义RememberMeService时指定自定义的数据源

    + ![image-20220329221126482](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329221126482.png)

      这种方法没法在启动时创建表结构,翻车v

    + 另一种方法,创建一个数据源

      ![image-20220329221425853](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329221425853.png)

      指定![image-20220329221453876](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329221453876.png)

       
