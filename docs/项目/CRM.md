# crm

+ 技术架构![image-20220326171113389](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220326171113389.png)
+ 软件企业组织结构
  + 研发部（程序员，美工，DBA），测试部，实施部门，产品部，市场部
+ 软件开发生命周期
  + 招标投标
  + 可行性分析--可行性分析报告
  + 需求分析--需求文档
  + 分析与设计
    + 架构设计
    + 项目设计
  + 搭建开发环境
  + 编码
  + 测试
  + 试运行
  + 运维

## 核心业务

+ customerRelationshipManagement(crm)客户关系管理系统
  + 传统应用，企业级应用；对软件性能等要求较低
  + 给销售或贸易型公司
  + 市场、销售、服务等环节中维护客户关系
  + 项目宗旨：增加新客户，留住老客户，已有客户转化为中式客户
  
+ 该项目
  + 给一个大型进出口贸易公司使用的，大宗商品的进出口贸易
  
+ 核心业务
  + 系统管理功能：为了保证业务管理功能安全运行
  + 业务管理功能
    + 市场活动：市场部
    + 线索：初级销售
    + 客户和联系人：高级销售
    + 交易：高级销售
    + 售后回访：客服使用
    + 统计图标：管理层
  
+ 表结构
  + ![image-20220328183343497](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220328183343497.png)
  
  + 主键
  
    + 一般采用非业务的字段做主键
  
    + 主键生成
  
      + 自增：运行效率高
      + assigned：程序员手动制定
        + ![image-20220329081824153](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329081824153.png)
        + 还有一些其他算法，（弹幕说雪花算法）貌似可以和时间做关联
      + 共享主键：用一对一外键做主键（不常用）
      + 联合主键（不常用）
  
    + 外键
  
      + 一对多
  
        + 内外连接
  
        + 外键不能为空，则使用内连接
  
        + 若外键可以为空，则看情况
  
          ![image-20220329084040466](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329084040466.png)
  
      + 一对一
  
        + 共享主键
        + 唯一外键（不加唯一约束则从语法上可能会发生多对多）
  
      + 多对多
  
        + 拆分为两个一对多
        + 关联关系表中的外键一般都不能为空，一般直接使用内连接
        + 内连接join
  
    + 关于日期与时间
  
      + 数据库date time datetime
      + Java Date
      + 都按照字符串处理
        + ![image-20220329085626645](/Users/xingyijin/Library/Application%20Support/typora-user-images/image-20220329085626645.png)

## SSM环境搭建

+ WEB-INFO下 不能直接访问

+ tymeleaf设置根路径

  + ```html
    <base th:href="${#request.getContextPath()}+'/'">
    ```

## 登陆

+ 某些简单的一对多可以使用字符串存储，使用‘，’隔开，之后判断可以直接使用.contains()方法

+ jq获取属性值![image-20220329164507587](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329164507587.png)

+ 地址栏跳转

  ![image-20220329164814299](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220329164814299.png)

+ 