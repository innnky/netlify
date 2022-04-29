# Bootstrap

> 官网https://getbootstrap.com/

+ 引入 bootstrap.min.css bootstrap.min.js
+ Flex快速入门

  + display:flex;

  + justify-content:center;

  + align-items:center;
+ Sass编程
  + 后缀名是scss
  + 面向css的编程语言，编译后生成css文件
  + 概念：
    + 变量 $定义
    + 嵌套 在css块内再写css块
    + 模块use引入模块
    + mixins @mixin @include 类似函数？
    + 继承和拓展 %定义 @exdend使用
    + 运算：可以带单位px等进行运算
  + 定制bs：可以翻阅文档，最后一般有定制方法，修改scss源码
    + 例：修改primary颜色，修改_variables.scss文件后在主模块重新编译

## Utilities

+ mt margin top
+ px- padding
+ float-start float-end :左右浮动
+ ms margin start（左）
+ bg-dark background dark
+ w-100 宽度100%
+ css基础知识
  + clearfix清除浮动

## 布局

+ 概念：

  + viewport：视口不包含右侧滚动条

    ![image-20220209111538971](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220209111538971.png)

  + brakepoint

    ![image-20220209111631354](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220209111631354.png)

+ container：

  ![image-20220209113032318](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220209113032318.png)

  + 注：fluid是永远100%

+ holder

  + 先引入，之后![image-20220209114454989](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220209114454989.png)

  + 常用功能

    ![image-20220209114559455](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220209114559455.png)

+ 栅格系统

  + col默认自动均分row
  
  + 当存在多个时候，如col-3 col-lg-12 以覆盖范围小的优先
  
    + col覆盖所有，col-lg覆盖960px以上
    + 即960以上时占12格，以下占3格
  
  + 没有指定情况下默认占满一行
  
    + 只指定了col-lg-3则在小于960时候没有指定，则占12格一行
  
  + auto: col-lg-auto 即当达到960px的时候 宽度自动设为内层元素的宽度
  
  + 行列：用在row元素后，用于子元素col为均分的情况
  
    + row-cols-n：每行n个col
  
    + row-cols-auto:按内容自适应行列
  
    + 理解：当指定了行列数后会自动计算默认宽度以及自动宽度，之后如果自行指定了覆盖范围更小的则在其作用域上覆盖
  
      ![image-20220209154709210](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220209154709210.png)
  
      ```html
      <div class="container">
        <div class="row row-cols-4">
          <div class="col">Column</div>
          <div class="col">Column</div>
          <div class="col-6">Column</div>
          <div class="col">Column</div>
        </div>
      </div>
      ```
  
      指定4列，计算出默认占3个，因此未指定的占3格，而指定的占6个
  
    + 也可以用断点区分列数（关联行列） row row-cols-1 row-cols-sm-2 row-cols-md-4
  
  + 栅格系统可以嵌套，当col中再出现row时，新的row便细分出较小的12格
  
+ Columns

  + 垂直
    + align-items-start(end center)使用在**父元素**上，使子元素排布居左，居右，中央
    + align-self-start(end center)使用在**子元素**上，决定自己的位置
  + 水平
    + justify-content-start(end center around between evenly)用在**父元素**上
  + 强制换行`<div class="w-100"></div>`
    + 在md时候换行`<div class="w-100 d-none d-md-block"></div>`
  + 列排序 order-
    + 取值由1-6
    + -first -last
    + 支持断点-md-1
  + 偏移offset-
    + -n  偏移n个栅格
    + 原理是增加margin
    + 支持断点offset-md-1
  + margin utilities
    + ms- me- mt- mb-
    + 支持断点-md-
    + -auto 貌似就是自动将左（右）边的空间填满（与左（右）边的元素互斥）
    + -n 
  + 独立使用占一整行
  + float-
    + -end -start

+ Gutturs

  + gx-n用在row上，改变col的水平padding
  + gy-n用在row上，改变换行时的行间距
  + g-n水平垂直均算上
  + 当n取0时无间距
  + -md-支持断点

+ z-index

  + bs中的z值都很大1000以上
  + 参见helpers-position进行定位

## Content

+ 修改了各种原生标签的默认样式
+ 新标签<code><pre><var><ktd>
+ 不推荐使用原生hidden 使用d-none d-block visible
+ 图片居中
  + 法1：父级设置text-center
  + 法2：img class="d-block mx-auto"