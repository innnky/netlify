# Cache

使用注解的方式操作缓存

+ 类似jdbc，是一种标准，可以兼容各种不同的（包含redis）
+ 主要注解![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131845020.png)

## 注解

+ @EnableCaching注解：作用在配置类上方，用于开启SpringBoot Cache自动装配

  ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131846195.png)

+ @Cacheable  ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131848049.png)

+ @CacheEvict方法执行后删除缓存![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131852958.png)

+ @CachePut![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131853365.png)

+ @Caching

  ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131853724.png)

+ @CacheConfig

  ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131854089.png)

## 使用

+ 配置类：
  + 类上方启用Cache![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131856722.png)
  +  向容器中放一个bean![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131857497.png)
    + RedisCacheManager是该接口的一个实现
    + 配置方法
    + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131952606.png)
    + ![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203131953144.png)
    +  
+ 使用
  + @Cacheable注解：
    + 在Controller上方加![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203132001985.png)
      制定Cache前缀
    + 在控制器方法上方添加该注解![](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/202203132003372.png)
      + 推测原理：应该是通过控制器方法的传入的值，将返回值进行缓存；下一次访问到该方法时先通过方法入参到缓存中去取值，取到了就不用执行控制器方法了

SPEL表达式