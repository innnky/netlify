# MyBatis

## 三层架构

+ 界面层（controller包）---springmvc
+ 业务逻辑层（service包）---sping
+ 数据访问层（dao包）---mybatis

## mybatis概述

+ 两大功能
  + sql映射sql mapper：将表中的1行数据映射成java对象
  + 数据访问data access objects(DAOs)：
+ 使开发人员专注于sql的编写，是一个增强的jdbc

## mybatis入门

+ 基本步骤

  1. 新建表
  2. maven加入--mybatis与mysql坐标
  3. 创建实体类--set-get-tostring
  4. 创建dao接口
  5. 创建sql映射文件
  6. 创建主配置文件
  7. 使用mybatis访问数据库

+ mapper文件

  + 放在与接口同一级目录

  + 模板

    ```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE mapper
      PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <mapper namespace="dao接口的全限定名称">
      <select id="dao接口中查询方法的名称" resultType="实体类名称">
        select * from Blog where id = #{id}
      </select>
    </mapper>
    ```

+ mybatis主配置文件

  + 模板

    ```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE configuration
      PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
      "http://mybatis.org/dtd/mybatis-3-config.dtd">
    <configuration>
      <environments default="development">
        <environment id="development">
          <transactionManager type="JDBC"/>
          <dataSource type="POOLED">
            <property name="driver" value="com.mysql.jdbc.Driver"/>
            <property name="url" value="${url}"/>
            <property name="username" value="${username}"/>
            <property name="password" value="${password}"/>
          </dataSource>
        </environment>
      </environments>
      <mappers>
        <mapper resource="org/mybatis/example/BlogMapper.xml"/>
      </mappers>
    </configuration>
    ```

  + evionment可以有多个，需要在default=指定使用的evironment
  
  + 需要在pom中加resource插件使得java下的xml也复制到class中
  
    ```xml
     <build>
        <resources>
          <resource>
            <directory>src/main/java</directory>
            <includes>
              <include>**/*.properties</include>
              <include>**/*.xml</include>
            </includes>
          </resource>
    
          <resource>
            <directory>src/main/resources</directory>
            <includes>
              <include>**/*.xml</include>
            </includes>
          </resource>
        </resources>
      </build>
    ```
  
  + mapper为从target/class/开始的路径
  
+ 使用mybatis访问数据库

  ![image-20220128105453056](https://home.innky.xyz:25566/images/image-20220128105453056.png)

+ IDEA出bug解决方案

  + maven clean compile
  + build rebuild project
  +  file invalidatecaches
  + 手动复制资源文件

+ 插入操作

  + 接口方法参数为插入对象，返回值为int影响行数
  + 在映射文件中使用#{属性名}访问
  + sqlSession.insert()方法进行查询
  + 默认情况下不会自动提交事务，需要sqlSession.commit()

+ 配置日志--在<configuration>中加入

  ![image-20220128110403069](https://home.innky.xyz:25566/images/image-20220128110403069.png)

## 第二章

+ 主要类

  + Resources 读取主配置文件
  + SqlSessionFactoryBuilder 创建SqlSessionFactory
  + SqlSessionFactory 重量级对象 一个项目中只用创建一个
    + 是接口 其实现类DefaultSqlSessionFactory 
    + openSession(boolean) ---获取SqlSession （是否自动提交事务）
  + SqlSession
    + 是接口：定义了各种操作数据库的方法
    + 实现类DefaultSqlSession
    + 该对象不是线程安全的，须在方法内部使用，执行sql完成后要关闭

+ 封装工具类

  + 在静态代码块中创建工厂，定义静态方法获取session

+ 使用idea创建模板

  ![image-20220128112523481](https://home.innky.xyz:25566/images/image-20220128112523481.png)

## 第三章

+ 通过**动态代理**创建dao的实现类
  + SqlSession.getMapper(DaoInterface.class)返回DaoInterface对象

### 参数传递

+ 传递参数：从接口方法传入xml mapper中
  + 使用**#{参数名}**在mapper中访问参数
    + 传入**一个**简单类型的值时，参数名可以随便写
    + 多个参数
      1. 接口中参数前加@Param("myname") mapper中使用myname做参数名
      2. 使用**java对象的属性值**做参数的值
      
           + #{属性名, javaType=,jdbcType=}完整写法
      
           + **#{属性名}**属性名直接做参数名，简化写法
      
      3. 位置传参 3.3前#{0} #{1} 3.4后#{arg0} #{arg1}
      4. map方式 #{key} 代码可读性差
    
  + 在`<select>`等标签中指定parameterType="参数类的全限定名称"
    + 此处该项可以省略，因为mybatis可以通过反射机制获取到
    + 对于java基本数据类型，mybatis提供了更为简短的别名
    
  + $ 和 # 

    + #使用的是PreparedStatement ?占位的方式，可以防止sql注入的风险，效率高
    + $使用的是Statement 是字符串的替换安全性低
      + 替换列名和表名时使用，能确保数据是安全的

  + 中文乱码-DarchetypeCatalog=internal -Dfile.encoding=gdk

### 输出结果

+ resultType属性:结果类型

  + 值为全限定名称或别名(如int)
  + mybatis执行sql语句调用结果类型的无参构造,并使用set方法进行赋值
    + 简单类型直接赋值
  + 结果类型可以为任何有同名列的类,没有的参数会被忽略
  + 类型也可以为map(HashMap)
    + 列名放key中,列值放value中
    + 只能取一个数据,多个数据要包裹在List中

+ 定义别名

  + 在configuration中使用typeAliases标签定义别名

    + 方式一:单独定义

      ![image-20220128193651291](https://home.innky.xyz:25566/images/image-20220128193651291.png)

    + 方式二:指定包

      ![image-20220128193914005](https://home.innky.xyz:25566/images/image-20220128193914005.png)

  + 使用别名可能导致名称不确定,因此推荐不使用别名

+  resultMap

  + 当实体类与列名不同时,使用resultmap指定其对应关系
  
  + 使用步骤
  
    ![image-20220128200315490](https://home.innky.xyz:25566/images/image-20220128200315490.png)
    
    定义
    
    ![image-20220128200351432](https://home.innky.xyz:25566/images/image-20220128200351432.png)
    
    引用 resultMap="studentMap"
    
  + resultMap和resultType不能一起用
  
  + resultMap替代方案：在sql语句中起别名
  
+ 模糊查询

  + 实现方法
    1. java代码中指定模糊查询内容（最普通的方式）
       + like #{name}
    2. 在mapper中拼接
       + like "%" #{name} "%"

## 动态sql

+ 根据条件不同执行不同的sql，使用标签实现

+ 使用动态sql需要使用java对象作为参数

+ 常用标签

  + `<if>`标签

    + `<if test="使用java对象的属性值作为判断条件 此处为sql语法不是java">条件成立则添加此处内容至sql中</if>`

  + `<where>`标签

    + 多个if的情况用where标签包裹起来,自动解决or and 等无效字符,解决语法问题

  + `<foreach>`标签

    + 循环遍历java中的数组,list 组装到sql中

    + 循环基本类型

      ![image-20220128203956980](https://home.innky.xyz:25566/images/image-20220128203956980.png)

    + 循环对象

      ![image-20220128204033990](https://home.innky.xyz:25566/images/image-20220128204033990.png)

    + collection取list或者array

+ sql代码片段

  + 先定义`<sql id="xxxxx">复用代码片段</sql>`
  + 后使用`<include refid="xxxxx">`![image-20220128204610152](https://home.innky.xyz:25566/images/image-20220128204610152.png)

## 配置文件

+ evironment配置项目

  + ![image-20220128205519526](https://home.innky.xyz:25566/images/image-20220128205519526.png)

  + ![image-20220128205801532](https://home.innky.xyz:25566/images/image-20220128205801532.png)

    ![image-20220128205822682](https://home.innky.xyz:25566/images/image-20220128205822682.png)

+ 属性配置文件

  + 将连接信息等单独放在一个文件中与主配置文件分开

  + 一般为jdbc.properters,使用.定义层级结构

    ```properties
    jdbc.driver=com.mysql.jdbc.driver
    jdbc.user=root
    .....
    ```

  + 使用

    + ![image-20220128210155727](https://home.innky.xyz:25566/images/image-20220128210155727.png)
    + ![image-20220128210257846](https://home.innky.xyz:25566/images/image-20220128210257846.png)

+ 指定mapper文件

  + 方式一:单独指定

  + 方式二:指定包名

    ![image-20220128210818954](https://home.innky.xyz:25566/images/image-20220128210818954.png)

    + 要求mapper文件与类同名(含大小写)
    + mapper文件要和接口在同一个包下

## Pagehelper数据分页

+ maven引入

  ![image-20220128211409270](https://home.innky.xyz:25566/images/image-20220128211409270.png)

+ mybatis添加插件(加在evionment前面)

  ![image-20220128211500378](https://home.innky.xyz:25566/images/image-20220128211500378.png)

+ 查询前使用![image-20220128211757178](https://home.innky.xyz:25566/images/image-20220128211757178.png)

## 高级

+ ![image-20220330153245105](https://home.innky.xyz:25566/images/image-20220330153245105.png)

+ 

+ ```xml
  <resultMap id="BaseResultMap" type="xyz.innky.vhr.model.Menu">
    <id column="id" jdbcType="INTEGER" property="id" />
    <result column="url" jdbcType="VARCHAR" property="url" />
    <result column="path" jdbcType="VARCHAR" property="path" />
    <result column="component" jdbcType="VARCHAR" property="component" />
    <result column="name" jdbcType="VARCHAR" property="name" />
    <result column="iconCls" jdbcType="VARCHAR" property="iconCls" />
    <result column="parentId" jdbcType="INTEGER" property="parentId" />
    <result column="enabled" jdbcType="BIT" property="enabled" />
    <association property="meta" javaType="xyz.innky.vhr.model.Meta">
      <result column="keepAlive" jdbcType="BIT" property="keepAlive" />
      <result column="requireAuth" jdbcType="BIT" property="requireAuth" />
    </association>
  </resultMap>
  <resultMap id="Menu2" type="xyz.innky.vhr.model.Menu" extends="BaseResultMap">
    <collection property="children" ofType="xyz.innky.vhr.model.Menu">
      <id column="id" jdbcType="INTEGER" property="id" />
      <result column="url2" jdbcType="VARCHAR" property="url" />
      <result column="path2" jdbcType="VARCHAR" property="path" />
      <result column="component2" jdbcType="VARCHAR" property="component" />
      <result column="name2" jdbcType="VARCHAR" property="name" />
      <result column="iconCls2" jdbcType="VARCHAR" property="iconCls" />
      <result column="parentId2" jdbcType="INTEGER" property="parentId" />
      <result column="enabled2" jdbcType="BIT" property="enabled" />
      <association property="meta" javaType="xyz.innky.vhr.model.Meta">
        <result column="keepAlive2" jdbcType="BIT" property="keepAlive" />
        <result column="requireAuth2" jdbcType="BIT" property="requireAuth" />
      </association>
    </collection>
  </resultMap>
  
  
  
  
  <select id="getMenuById" resultMap="Menu2">
  
      select distinct m1.*,
                      m2.id id2,m2.url url2, m2.path path2,
                      m2.component component2, m2.name name2,
                      m2.iconCls iconCls2, m2.keepAlive keepAlive2,
                      m2.requireAuth requireAuth2, m2.enabled enabled2
  
      from menu m1, menu m2, menu_role mr, role r, hr_role hrr
      where m1.id=m2.parentId and
        m2.id=mr.mid and
        mr.rid=r.id and
        r.id=hrr.rid and
        hrr.hrid=#{hrid} and
        m2.enabled=true
      order by m1.id,m2.id;
    </select>
  ```

+ resultMap继承

+ 