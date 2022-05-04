# SpringSecurity

## 授权管理

> 一个用户可以有多个角色，而每个角色又可以有多个权限
>
> 有关权限与角色https://blog.csdn.net/NDKHBWH/article/details/100074764

+ hasAuthority方法：制定单个权限
  + 在配置类中配置
  + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141008526.png)
    + permitAll()允许所有 authenticated()认证了就可以访问 hasAuthority()具有制定权限才可以访问
    + 此处举例不恰当，权限信息应该是类似DELETE_USER INSERT_USER之类的
  + 在返回的UserDetail中需要设置权限
    + 通过![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141022711.png)方法获取权限信息（一般是重写的时候遍历角色列表设置权限)
+ hasAnyAuthority方法：多个权限满足任意一条就可以
  + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141013453.png)
  + 语法：使用","分隔开多个权限
  + 语法：也可以传入多个String
+ hasRole：单个角色
  + 使用的时候会自动在传入的参数前面加上ROLE_前缀
  + 为对象声明角色信息（此处为另一种写法，自定义的用户对象并没有实现UserDettail，而是通过User（）构造方法得到UserDetail对象）![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141029880.png)
  + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141030152.png)
+ hasAnyRole：多个角色
+ 自定义403页面：![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141033476.png)

## 注解使用

+ 开启注解（在启动类上）![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141035370.png)
+ 注解
  + @Secured
    + 启用securedEnabled=true
    + 在Controller方法上方![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141037106.png)
    + 需要添加ROLR前缀
  + @PreAuthorize
    + 启用prePostEnabled=true
    + 既可以以权限来判定，也可以以角色
    + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141054546.png)
    + 弹幕说：该注解内填的是Access表达式，适用的范围更广
  +  @PostAuthorize
    + 启用prePostEnabled=true
    + 方法执行之后进行权限判断
  + @PostFilter
    + 对返回值做过滤（返回List）
    + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141101133.png)
  + @PreFilter
    + 对传入参数做过滤
    + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203141101558.png)
    + 