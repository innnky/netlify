若依

## 验证码

+ ![image-20220308100647854](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308100647854.png)

+ vue初始化方法![image-20220308100952075](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308100952075.png)

+ 设置验证码图片![image-20220308101220104](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308101220104.png)

+ 配置![image-20220308101501712](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308101501712.png)

  该变量定义在![image-20220308101515122](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308101515122.png)文件

+ 反向代理![image-20220308101839333](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308101839333.png)保存在![image-20220308101809344](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308101809344.png)中

## 登录

+ es6 Promise()异步处理
+ ![image-20220308102945176](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308102945176.png)
+ 异步记录日志![image-20220308103229577](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308103229577.png)
+ 验证验证失败直接抛出异常
+ 使用jwt：自己验证一下具体实现![image-20220308104318544](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308104318544.png)

+ parentid参照menuid，为0则为顶级![image-20220308105627506](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308105627506.png)

## 用户管理

+ 页面加载转圈效果![image-20220308160146980](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308160146980.png)

+ springsecurity验证权限![image-20220308160323962](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308160323962.png)

+ 分页![image-20220308160854497](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308160854497.png)

+ 查询

  + 加载service方法上方，给查询数据库起别名![image-20220308161015645](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308161015645.png)

    弹幕说做权限的

+ 加载树状图

  + 可以利用断点配合日志查看SQL
  + 将与数据库匹配的类型转换为前端需要的类型（删除一些不需要的属性）未学过的知识![image-20220308162120771](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308162120771.png)

+ 添加

  + ![image-20220308163247401](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308163247401.png)
  
  + 前端进行校验
  
  + 多对多修改：先删再加
  
    ![image-20220308170014043](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308170014043.png)
  
    + 因为有事务所以操作失败也会直接回滚
  
  + 删除数据
  
    + 先删除关联表再删除用户
  
      ![image-20220308191233208](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308191233208.png)
  
    + 删除用户的时候是逻辑删除，即将用户的del状态置1而不真正的删除用户
  
  + 异步任务管理器![image-20220308191615471](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308191615471.png)
  
    + 单例模式
  
      ![image-20220308191600729](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308191600729.png)
  
    + ![image-20220308192204776](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220308192204776.png)

## 代码自动生成

+ 系统工具-》代码生成