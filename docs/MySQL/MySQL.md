# MySQL

## 基础

分类

```
DQL：
				数据查询语言（凡是带有select关键字的都是查询语句）
				select...

			DML：
				数据操作语言（凡是对表当中的数据进行增删改的都是DML）
				insert delete update
				insert 增
				delete 删
				update 改

				这个主要是操作表中的数据data。

			DDL：
				数据定义语言
				凡是带有create、drop、alter的都是DDL。
				DDL主要操作的是表的结构。不是表中的数据。
				create：新建，等同于增
				drop：删除
				alter：修改
				这个增删改和DML不同，这个主要是对表结构进行操作。

			TCL：
				不是王牌电视。
				是事务控制语言
				包括：
					事务提交：commit;
					事务回滚：rollback;

			DCL：
				是数据控制语言。
				例如：授权grant、撤销权限revoke....
```



### 单表 

+ 数据处理函数

  + 单行:lower substr(下表从1开始) concat length trim	round(四舍五入) rand()
    + NULL只要参与运算，最终结果一定是NULL。为了避免这个现象，需要使用ifnull函数ifnull(comm, 0)
    + format(数字, '格式')
    + str_to_date：将字符串varchar类型转换成date类型
      + ​		`insert into t_user(id,name,birth) values(1, 'zhangsan', str_to_date('01-10-1990','%d-%m-%Y'));`
    + date_format：将date类型转换成具有一定格式的varchar字符串类型。

+ 分组函数（多行处理函数）聚合函数

  + count sum...

+ 分组相关

  + ```
    在一条select语句当中，如果有group by语句的话，
    			select后面只能跟：参加分组的字段，以及分组函数。
    			其它的一律不能跟。
    ```

+ 单表总结

  ```
  执行顺序？
  		1. from
  		2. where
  		3. group by
  		4. having
  		5. select
  		6. order by
  	
  	从某张表中查询数据，
  	先经过where条件筛选出有价值的数据。
  	对这些有价值的数据进行分组。
  	分组之后可以使用having继续筛选。
  	select查询出来。
  	最后排序输出！
  ```

+ distinct只能出现在所有字段的最前方。

### 多表

+ 连接

  + 关于各种连接的等价性
  + 内连接
    + 逗号
    + join
    + inner join
  + 外连接
    + left join
    + left outer join
    + right...
  + 非等值连接案例

  ```
  2.6、内连接之非等值连接
  
  案例：找出每个员工的薪资等级，要求显示员工名、薪资、薪资等级？
  mysql> select * from emp; e
  +-------+--------+-----------+------+------------+---------+---------+--------+
  | EMPNO | ENAME  | JOB       | MGR  | HIREDATE   | SAL     | COMM    | DEPTNO |
  +-------+--------+-----------+------+------------+---------+---------+--------+
  |  7369 | SMITH  | CLERK     | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
  |  7499 | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
  |  7521 | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 |  500.00 |     30 |
  |  7566 | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |    NULL |     20 |
  ....
  
  mysql> select * from salgrade; s
  +-------+-------+-------+
  | GRADE | LOSAL | HISAL |
  +-------+-------+-------+
  |     1 |   700 |  1200 |
  |     2 |  1201 |  1400 |
  |     3 |  1401 |  2000 |
  |     4 |  2001 |  3000 |
  |     5 |  3001 |  9999 |
  +-------+-------+-------+
  
  select 
  	e.ename, e.sal, s.grade
  from
  	emp e
  join
  	salgrade s
  on
  	e.sal between s.losal and s.hisal; // 条件不是一个等量关系，称为非等值连接。
  ```

+ 子查询

+ Limit下标(查询出来的行号)从0开始

##### 总结

+ 查询尽量走索引(主键, UNIQUE)
+ 少用"%"开头的模糊查询
+ 少用or
+ 索引列尽量不要数学运算
+ 

## DDL

### 基础

+ 建表:	表名：建议以t_ 或者 tbl_开始，可读性强。见名知意。

+ 复制表: create table emp2 as select * from emp;(连同数据一起复制)

+ 数据类型

  + Date datetime (与java不同 java只有Date jdk8后新增的带Local 的时间类则和mysql中的类似)

    + ``` 
      如果你提供的日期字符串是这个格式，str_to_date函数就不需要了！！！
      			%Y-%m-%d
      		insert into t_user(id,name,birth) values(2, 'lisi', '1990-10-01');
      
      	mysql短日期默认格式：%Y-%m-%d
      	mysql长日期默认格式：%Y-%m-%d %h:%i:%s
      
      ```

  + Binary类型: 可以用来存储uuid 插入数据需要unhex("16进制数据")

  + char - varchar - text - clob(字符大对象)  >>>binary - varbinary - blob (又分为TINYBLOB BLOB MEDIUMBLOB LONGBLOB) 

+ 将结果插入表中insert into dept_bak select * from dept;

+ truncate 快速删除表中的所有数据

  ```sql
  delete语句删除数据的原理？（delete属于DML语句！！！）
  		表中的数据被删除了，但是这个数据在硬盘上的真实存储空间不会被释放！！！
  		这种删除缺点是：删除效率比较低。
  		这种删除优点是：支持回滚，后悔了可以再恢复数据！！！
  	
  	truncate语句删除数据的原理？
  		这种删除效率比较高，表被一次截断，物理删除。
  		这种删除缺点：不支持回滚。
  		这种删除优点：快速。
  
  	用法：truncate table dept_bak; （这种操作属于DDL操作。）
  
  	大表非常大，上亿条记录？？？？
  		删除的时候，使用delete，也许需要执行1个小时才能删除完！效率较低。
  		可以选择使用truncate删除表中的数据。只需要不到1秒钟的时间就删除结束。效率较高。
  		但是使用truncate之前，必须仔细询问客户是否真的要删除，并警告删除之后不可恢复！
  
  		truncate是删除表中的数据，表还在！
  	
  	删除表操作？
  		drop table 表名; // 这不是删除表中的数据，这是把表删除。
  ```

### 约束

+ 五种约束

  ![image-20220430095107167](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430095107167.png)

  + 执行sql脚本source D:\course\03-MySQL\document\vip.sql

+ unique

  + ```sql
    create table t_vip(
    		id int,
    		name varchar(255) unique,
    		email varchar(255)
    	);
    ```

  + unique可以为空

  + 表级约束

    ```sql
    create table t_vip(
    				id int,
    				name varchar(255),
    				email varchar(255),
    				unique(name,email) // 约束没有添加在列的后面，这种约束被称为表级约束。
    			);
    ```

  + 在mysql当中，如果一个字段**同时被not null和unique约束**的话，该字段自动变成主键字段。（注意：oracle中不一样！）

  + 主键和unique会自动加上索引

+ 主键

  + 列级`id int primary key auto_increment,  //列级约束`
  + 表级`primary key(id,name) //复合主键比较复杂，不建议使用！！！`  
  + 主键一般使用数字等定长的字段,不建议使用varchar
  + 自然主键与业务主键
    + ![image-20220430095938274](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430095938274.png)

+ 外键

  + 被引用的这个字段不一定是主键，但至少具有unique约束。
  + `CONSTRAINT t_student_ibfk_1 FOREIGN KEY (cno) REFERENCES t_class (classno)`

+ 存储引擎
  + 建表时使用CREATE TABLE `t_student` (...) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8
  + MyISAM引擎 不支持事务机制，安全性低。
  + MEMORY引擎 存储在内存中

### 事务

+ 一个事务其实就是一个完整的业务逻辑。是一个最小的工作单元。不可再分。

+ 只有DML语句才会有事务这一说，其它语句和事务无关 增删改

+ ![image-20220430101951997](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430101951997.png)

+ 事务的结束:

  + ![image-20220430102215779](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430102215779.png)
  + 提交commit
  + 回滚rollback

+ mysql默认自动提交事务,回滚都是回滚到上次提交点,因此默认情况回滚不会有任何效果

+ 开启事务 start transaction

+ 事务的4个特性 ACID

  + ```
    A：原子性
    		说明事务是最小的工作单元。不可再分。
    
    	C：一致性
    		所有事务要求，在同一个事务当中，所有操作必须同时成功，或者同时失败，
    		以保证数据的一致性。
    
    	I：隔离性
    		A事务和B事务之间具有一定的隔离。
    		教室A和教室B之间有一道墙，这道墙就是隔离性。
    		A事务在操作一张表的时候，另一个事务B也操作这张表会那样？？？
    
    	D：持久性
    		事务最终结束的一个保障。事务提交，就相当于将没有保存到硬盘上的数据
    		保存到硬盘上！
    ```

+ 隔离性

  + 读未提交 read uncommited --->A可以读取B未提交的数据 脏读
  + 读已提交 read commited    ----> 不可重复读取问题 (oracle默认级别)
  + 可重复读 repeatable read    --->出现幻影读问题 (mysql默认级别) (永远读取的都是刚开启事务时的数据)
  + 序列化    serializable  串行   --->标级别上锁
  + 实验: 
    + RR下,两个事务同时操作同一个表的同一行会被阻塞,直到另一个事务提交
  + 隔离级别
    + 修改set global transation isolation level read uncommitted
    + 查看SELECT @@global.tx_isolation; 或者SELECT @@tx_isolation;
    + 查看新版本SELECT @@transaction_isolation;

### 索引

+ 索引可以单列也可以多字段联合

+ 索引需要排序

+ ![image-20220430151302602](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430151302602.png)

+ 加索引条件:
  + 数据量大
  + 经常出现在where后面
  + 字段较少进行DML语句(增删改)
  + 唯一性较弱的字段索引意义不大,越唯一意义越大
  + 索引太多会降低效率,建议通过主键和unique查询
  
+ 加索引条件:
  
  + 唯一性加索引
  + 频繁分组或排序的列,排序列多个可以建组合索引
  
+ 减少索引的条件:
  
  + 经常更新的表
  + 数据量小的表
  + 唯一性弱的列 如男/女
  +  where条件中用不到的字段
  + 参与计算的列
  
+ 创建索引![image-20220430152407854](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430152407854.png)

  + 创建表时创建索引

     ![image-20220501104223306](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220501104223306.png)

  + 已经存在表上创建

    + ![image-20220501104316684](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220501104316684.png)
    + ![image-20220501104335546](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220501104335546.png)

+ 删除索引![image-20220430152417824](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430152417824.png)

+ 分析是否SQL使用索引![image-20220430152507953](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430152507953.png)
  + 看结果的type字段:Ref/All possible_keys字段
  + ![image-20220501104750902](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220501104750902.png)

+ 索引失效
  + 以"%"开头的模糊查询不走索引,效率低
  + 使用or两边都要有索引才走索引,只有一遍有索引则失效,因此尽量少用or,(或许可以用union替代)
  + 复合索引没有使用最左侧列查找不走索引(最左原则)
  + 索引列参与了数学运算(或使用了函数)

### 视图

+ 创建![image-20220430154109058](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430154109058.png)
+ 删除 drop view xxxx
+ 对视图进行增删改会影响原表
+ 视图的作用![image-20220430154610559](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430154610559.png)
+ crud![image-20220430154750274](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430154750274.png)

## DBA

+ 数据库导出![image-20220430155228841](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430155228841.png)
+ 导入:在数据库连接中
  + create database xxx-->use xxx -->source xxx.sql

## 数据库设计

+ 三范式

  ```sql
  	第一范式：要求任何一张表必须有主键，每一个字段原子性不可再分。
  
  	第二范式：建立在第一范式的基础之上，要求所有非主键字段完全依赖主键，
  	不要产生部分依赖。
  
  	第三范式：建立在第二范式的基础之上，要求所有非主键字段直接依赖主键，
  	不要产生传递依赖。
  
  ```

+ 第一范式

  + ![image-20220430155817676](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430155817676.png)
    + 没有主键
    + 联系方式可再分

+ 第二范式

  + 多对多设计-->三张表+2外键-->多对多放在一张表上就会出现部分依赖

+ 第三范式

  + 一对多设计-->两张表+1外键-->一对多放在一张表上就会出现传递依赖

+ 一对一设计------->外键+UNIQUE![image-20220430161111724](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220430161111724.png)

+ 有的时候可能会存在冗余，但是为了减少表的连接次数，这样做也是合理的!

  + Docker+ mysql备份数据

    ```shell
    docker exec -it 9d12fdadc5bd8f9729a86aef3a4945ad47da8ecf252680c703f96f60143417c4 mysqldump -uroot -p000508 graduation_design > /Users/xingyijin/graduation.sql
    ```

    
