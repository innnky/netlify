# Mockito

## 引入

+ maven依赖

```xml
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-core</artifactId>
    <version>4.5.1</version>
    <scope>test</scope>
</dependency>

import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

```

+ 作用

  + 模拟出一个对象,替换掉真实的对象

    ![image-20220502154707589](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502154707589.png) 

+ 生成测试类:generate->test

+ mock方法

  ![image-20220502155034720](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502155034720.png) 

  + 产生一个模拟的对象,传入一个class![image-20220502155425546](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502155425546.png)
  + 使用vervify验证一个方法是否被调用了多少次(次数不对**会报错**)![image-20220502155500506](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502155500506.png)
  + 如果不对模拟对象的行为进行定义(称之为打桩)则会返回默认值(如int 返回0,Object 返回null)

+ 打桩

  + thenReturn()一直返回同一个值
    +  ![image-20220502155817906](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502155817906.png)
  + thenThrow()调用时抛出异常
  + thenCallRealMethod()调用真实的方法![image-20220502164836629](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502164836629.png)
  + 

+ 断言Assertions类静态方法

  + 断言![image-20220502160037483](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502160037483.png)
  + assertTrue()

+ Mock注解

  + 与Mock方法一样,创建Mock对象![image-20220502160224304](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502160224304.png)

  + 使用注解方式需要先启用
    ```java
        @BeforeEach
        void beforeEach() {
            MockitoAnnotations.openMocks(this);
        }
    ```

+ Spy与@Spy

  ![image-20220502160604393](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502160604393.png) 

  + 没有打桩则调用真实的方法
  + 若打桩则调用打桩方法![image-20220502160810164](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502160810164.png)

+ Mock静态方法

  + 使用这个**替换**原来的依赖

     ![image-20220502165119208](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502165119208.png)

  + 有参静态方法Mock![image-20220502165225202](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502165225202.png)

  + 无参静态方法Mock

    ![image-20220502165452105](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502165452105.png)

+ @InjectMocks注解:依赖注入?

  ![image-20220502170426514](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220502170426514.png) 

+ RunWithCoverage计算覆盖率

## 单元测试生成

+ Jcode5  https://www.jianshu.com/p/33f9fc37403b
+ TestMe
+ JunitGenerate
+ Squaretest

