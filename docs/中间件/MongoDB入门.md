# MongoDB

## 引入

+ 使用场景：三高

  + 高并发high performance
  + 海量数据 high storage
  + 高拓展性、高可用性high scalability/availablity

+ 特点

  + 数据量大
  + 写操作频繁
  + 价值较低，对事务支持不高
  + 2000以上qps

+ 简介

  + 无模式 
  + 最像关系型数据库的
  + 可以嵌套js脚本实现存储过程

+ 安装

  + 关于版本号![image-20220226215724616](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226215724616.png)

  + 启动：默认端口：27017

    + 参数式![image-20220226215817010](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226215817010.png)

    + 配置文件![image-20220227090821299](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227090821299.png)

      ![image-20220226220249378](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226220249378.png)
    
  + linux安装

+ 连接

  + ![image-20220226220422967](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220226220422967.png)不带参数默认连接本地的
  + 图形化：compass

## 基本常用命令

+ _db为MongoDB的主键字段

### 库

+ 创建DB并使用： use <dbname>
+ 刚创建不会存到磁盘，当第一个set出现进行持久化
+ 显示所有库：show dbs
+ 默认库：admin local（数据永远不会被复制）config
+ 删除库![image-20220227112220280](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227112220280.png)

### 集合（类似于表）

+ 显式创建
  + 创建![image-20220227112336941](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227112336941.png)
  + show collections
+ 删除![image-20220227112410776](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227112410776.png)

#### 插入

+ 插入单个

```js
db.<setName>.insert(
	<document or array of documents>,
    {
        writeConcern: <document>,
        ordered: <boolean>
    }
)
```

+ 插入多条![image-20220227112831129](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227112831129.png)

#### 查询

+ 查询所有db.<setName>.find()
+ 条件查询![image-20220227113025009](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113025009.png)
+ 查询第一条![image-20220227113044695](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113044695.png)
+ 投影![image-20220227113155210](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113155210.png)
  + 第二个参数，1表示显示，0表示不显示
+ 可以直接使用js语法trycatch![image-20220227113323062](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113323062.png)

#### 更新

+ ![image-20220227113408392](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113408392.png)

+ 覆盖修改![image-20220227113454033](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113454033.png)

  + 默认是浮点数，因此存整数需要调函数

+ 局部修改![image-20220227113611122](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113611122.png)

+ 批量修改（默认只修改第一条数据）

  + 批量需要设置第三个参数multi=true![image-20220227113755951](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113755951.png)

+ 列值增长修改

  ![image-20220227113857786](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113857786.png)

+ 删除文档![image-20220227113918030](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227113918030.png)

  + 条件为{}表示删除全部
  + 弹幕说可以deleteOne 和deleteMany
  + 删除默认可以删多条数据![image-20220227114009452](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114009452.png)

#### 分页查询

+ 计数![image-20220227114207226](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114207226.png)
+ 使用limit限制条数![image-20220227114231285](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114231285.png)
+ 跳过前几条数据不显示skip![image-20220227114319821](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114319821.png)
+ 排序查询![image-20220227114337077](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114337077.png)
  + ![image-20220227114403402](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114403402.png)以userid升序
  + 1为升序 -1为降序
  + 支持多条件![image-20220227114502886](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114502886.png)

#### 复杂查询

+ 支持js的正则语法查询![image-20220227114619219](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114619219.png)
+ 比较查询![image-20220227114659169](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114659169.png)
+ 包含查询$in![image-20220227114740435](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114740435.png)
+ 复合条件查询`$and`  `$or`![image-20220227114910420](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227114910420.png)

#### 小结

```mongodb
选择切换数据库：use articledb
插入数据：db.comment.insert({bson数据})
查询所有数据：db.comment.find();
条件查询数据：db.comment.find({条件})
查询符合条件的第一条记录：db.comment.findOne({条件})
查询符合条件的前几条记录：db.comment.find({条件}).limit(条数)
查询符合条件的跳过的记录：db.comment.find({条件}).skip(条数)
修改数据：db.comment.update({条件},{修改后的数据}) 或db.comment.update({条件},{$set:{要修改部分的字段:数据})
修改数据并自增某字段值：db.comment.update({条件},{$inc:{自增的字段:步进值}})
删除数据：db.comment.remove({条件})
统计查询：db.comment.count({条件})
模糊查询：db.comment.find({字段名:/正则表达式/})
条件比较运算：db.comment.find({字段名:{$gt:值}})
包含查询：db.comment.find({字段名:{$in:[值1，值2]}})或db.comment.find({字段名:{$nin:[值1，值2]}})
条件连接查询：db.comment.find({$and:[{条件1},{条件2}]})或db.comment.find({$or:[{条件1},{条件2}]})

```

## 索引

+ 分类
  + 单字段索引
  + 复合索引
  + 其他索引

### 操作

+ 查看![image-20220227134718047](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227134718047.png)
+ 创建![image-20220227134842675](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227134842675.png)
  + keys：加索引的字段
  + options：常用的选项![image-20220227134931629](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227134931629.png)
  + 例：![image-20220227135048655](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227135048655.png)![image-20220227135105028](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227135105028.png)
    + 1表示升序-1降序
+ 移除![image-20220227135303437](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227135303437.png)
  + 通过条件删除![image-20220227135342319](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227135342319.png)
  + 通过名称删除![image-20220227135359245](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227135359245.png)
  + 删除多个（所有）![image-20220227135420800](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227135420800.png)
  + _id索引无法被删除

### 使用

+ 执行计划:分析查询性能
  + 加.explain![image-20220227135549330](C:\JavaLearning\JavaSe\Intermediate\image-20220227135549330.png)
  + 使用compass的explain plan 标签下
+ 涵盖的查询（mysql覆盖索引）（不用回表）

## 文章评论

+ java环境搭建

  + 引入starter

    ```xml
    <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
    </dependency>
    
    ```

  + 配置文件

    ![image-20220227170656252](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227170656252.png)

+ 使用

  + 实体类po创建

    ![image-20220227170951128](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227170951128.png)

    + @Id主键属性
    + @Field：类似于映射
    + @Index创建索引
    + @CompoundIndex复合索引

  + dao包编写

    + 创建接口（并继承）![image-20220227171449049](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227171449049.png)
    + 动态代理自动生成![image-20220227171644293](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227171644293.png)类
    + dao方法
      + .save() deleteById() findAll() findById()

  + 测试类命名规范（待测试类全称Test）![image-20220227171917762](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227171917762.png)

+ 分页查询

  + dao接口中编写方法![image-20220227180007432](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227180007432.png)
    + 注意语法格式必须这么写（弹幕说是jpa规范）
    + idea会有代码提示
  + 调用![image-20220227180115652](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227180115652.png)
  + 使用MongoTemplate实现对某一列的操作
    + 在业务层注入![image-20220227180445310](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227180445310.png)
    + 创建查询（条件好像也可使用.and()方法）![image-20220227180811735](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227180811735.png)
    + 创建更新条件![image-20220227180907444](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227180907444.png)
    + 调用template的更新方法![image-20220227180946908](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220227180946908.png)

