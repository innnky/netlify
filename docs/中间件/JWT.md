# JWT

## 简介

![image-20220307200218447](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307200218447.png)

+ 功能	
  + 授权
  + 信息交换
+ 流程![image-20220307201512011](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307201512011.png)
  + ![image-20220307201734233](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307201734233.png)
+ 优势![image-20220307201800733](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307201800733.png)

## 组成

+ ![image-20220307201834886](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307201834886.png)
+ 头部header
  + 内容
    + 类型
    + 签名算法
  + 使用base64编码
  + 示例![image-20220307202049188](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307202049188.png) 
+ 有效负载payload
  + 也是通过base64编码
  + 主要存放用户的自定义信息
  + 示例![image-20220307202219214](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307202219214.png) 
  + 负载不应该放敏感信息
  + jwt不保证安全性，安全性由https保障
+ 签名signature
  + 生成原理![image-20220307202829132](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307202829132.png)
  + ![image-20220307202840291](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307202840291.png)
+ 总结
  + ![image-20220307203049433](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307203049433.png) 

## Java使用

+ 引入依赖![image-20220307203251928](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307203251928.png)
+ 生成签名![image-20220307203609214](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307203609214.png)
  +  header可以不写使用默认值
+ 验证签名并取出值
  + ![image-20220307204335110](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307204335110.png)
  + 获取过期时间![image-20220307204605119](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307204605119.png)
    + 注意：如果存的是Int却使用asString()来取会返回空
  + 可能会抛出的异常![image-20220307204654872](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220307204654872.png)

