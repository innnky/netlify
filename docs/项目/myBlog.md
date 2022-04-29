# MyBlog

## [VO、DTO、DO、PO的概念、区别和用处](https://blog.csdn.net/zjrbiancheng/article/details/6253232)

![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203132049029.png)

+ pojo：纯的java对象，不包含业务逻辑，不实现接口
+ do与dto
  + 两者有时候并不是一对一的关系，因此需要进行转换
  + DO有时候具有业务逻辑，DTO为纯的POJO不具有业务逻辑
    + DO为业务层内的对象，如果直接返回给展示层，则可能会在展示层越过业务层调用业务方法
    + 也会使得事务难以控制（事务默认都在业务层）
+ 这篇文章说DTO尽量是二维的，如果一个DTO对象包含了多个其他对象（变成树形结构）会使得性能变慢
+ DO与PO
  + PO为与数据库一一对应的POJO，也就是最底层的
  + 大部分情况两者一样
  + 也有不同的：
    + 有某些DO没有对应的PO
    + 有PO没有对应的DO如某些多对多的关联表，可能没有实际的意义，则其有PO而无DO
      + 不是所有的多对多都无实际意义，比如两者的联系影响到业务
  + 操作
    + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203132119217.png)

## 使用

+ 方法一BeanUtils.copyProperties(admin,adminDTO)
+ 方法二
  + ![image-20220331153514869](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220331153514869.png)
  + 定义映射
  +  
    + ![image-20220331153659742](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220331153659742.png)

## vue渲染Md页面

https://blog.csdn.net/qq_34691227/article/details/105845460

## 路由传参数

https://www.jianshu.com/p/d276dcde6656

## SpringSecurity貌似默认会拦截所有未登录的post请求

## 部署项目相关

vue部署

根目录新建vue.config.js

```js
module.exports={
    publicPath:'./'
}
```