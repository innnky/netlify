# ElasticSearch

## 入门

+ 数据格式![image-20220306165059275](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165059275.png)

+ type概念淡化，最新版本已经删除

+ 倒排索引

  + 通过关键字查询

    ![image-20220306165345411](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165345411.png)

### 操作

+ 创建索引

  + ![image-20220306165448965](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165448965.png)
  + post不具有幂等性

+ 获取索引

  + ![image-20220306165553284](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165553284.png)
  + 获取全部索引![image-20220306165619498](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165619498.png)

+ 删除![image-20220306165701854](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165701854.png)

+ 添加文档

  + 自动id![image-20220306165818876](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165818876.png)
  + 手动指定id![image-20220306165923607](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165923607.png)
  + 当确定是幂等性操作可以使用put方法，且可以使用_create![image-20220306165957021](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306165957021.png)

+ 查询文档![image-20220306170039474](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170039474.png)

  + 查询所有数据![image-20220306170107849](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170107849.png)

+ 修改文档

  + 完全覆盖，全量数据更新

    ![image-20220306170217627](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170217627.png)

  + 局部修改![image-20220306170345882](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170345882.png)

+ 删除文档![image-20220306170418756](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170418756.png)


### 查询

+ 通过url携带![image-20220306170446293](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170446293.png)

+ 通过body携带

  ![image-20220306170551923](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170551923.png)

  + 查询所有![image-20220306170612534](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170612534.png)
  
  + （根级参数）类似limit![image-20220306170646157](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170646157.png)
  
  + （根级参数）投影![image-20220306170735871](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170735871.png)
  
  + 排序![image-20220306170912395](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306170912395.png)
  
  + 多条件![image-20220306171032953](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306171032953.png)
  
    + must should 。。。
  
  + 比较![image-20220306171219327](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306171219327.png)
  
  + 高亮显示![image-20220306195206778](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306195206778.png)
  
  + 默认情况下文本数据会自动生成倒排索引存储
  
    + 使用match查询时会自动进行分词匹配，即全文检索，词中的任意一部分匹配上都会返回在结果中
    + 整体匹配的查询需要将match换成match_phrase
  
  + 聚合操作
  
    + ![image-20220306195259965](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306195259965.png)
  
    + 不要原始数据，只查统计结果![image-20220306195417603](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306195417603.png)
  
    + 求平均值
  
      ![image-20220306195454940](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306195454940.png)

### 映射

+ 创建![image-20220306195706067](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306195706067.png)

  ![image-20220306195654098](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306195654098.png)

  + keyword不会分词
  + index为false就不能作为查询条件

+ 查询 ：使用get

### javaapi

+ 依赖

  ```xml
  <dependencies>
      <dependency>
          <groupId>org.elasticsearch</groupId>
          <artifactId>elasticsearch</artifactId>
          <version>7.8.0</version>
      </dependency>
      <!-- elasticsearch 的客户端 -->
      <dependency>
          <groupId>org.elasticsearch.client</groupId>
          <artifactId>elasticsearch-rest-high-level-client</artifactId>
          <version>7.8.0</version>
      </dependency>
      <!-- elasticsearch 依赖 2.x 的 log4j -->
      <dependency>
          <groupId>org.apache.logging.log4j</groupId>
          <artifactId>log4j-api</artifactId>
          <version>2.8.2</version>
      </dependency>
      <dependency>
          <groupId>org.apache.logging.log4j</groupId>
          <artifactId>log4j-core</artifactId>
          <version>2.8.2</version>
      </dependency>
      <dependency>
          <groupId>com.fasterxml.jackson.core</groupId>
          <artifactId>jackson-databind</artifactId>
          <version>2.9.9</version>
      </dependency>
      <!-- junit 单元测试 -->
      <dependency>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
          <version>4.12</version>
      </dependency>
  </dependencies>
  ```

+ 使用

  + 创建客户端![image-20220306200245668](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306200245668.png)
  + 创建索引，，获取相应状态![image-20220306200542357](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306200542357.png)
  + 关闭连接![image-20220306200312364](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306200312364.png)

+ 查询索引![image-20220306200735953](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306200735953.png)

+ 删除索引![image-20220306200902156](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306200902156.png)

+ 添加数据

  + 新建bean类
  + 创建添加请求![image-20220306201045504](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306201045504.png)
  + 将bean转为json并关联请求![image-20220306201157648](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306201157648.png)
  + 发送请求

+ 更新数据

+ 修改数据![image-20220306201323012](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306201323012.png)

+ 获取数据![image-20220306201440499](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306201440499.png)

+ 删除数据![image-20220306201507848](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306201507848.png)

+ 批量处理（包装多个请求）

  ![image-20220306201718897](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306201718897.png)

+ 查询（搜索）数据

  ![image-20220306202011691](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202011691.png)

  + 查询结果转字符串![image-20220306202109449](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202109449.png)

    ![image-20220306202121485](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202121485.png)

+ 条件

  + ![image-20220306202207378](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202207378.png)

  + 分页![image-20220306202313376](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202313376.png)

  + 排序![image-20220306202422225](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202422225.png)

  + 投影操作（排除和包含）

  + ![image-20220306202519084](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202519084.png)

  + 组合条件

    ![image-20220306202724733](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202724733.png)

  + 范围查询![image-20220306202840075](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202840075.png)

  + 模糊查询

    ![image-20220306202937979](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306202937979.png)

    即与条件查（n）个字符也可以显示出来

  + 高亮查询![image-20220306203039688](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306203039688.png)

  + 聚合查询

    + 最大值

      ![image-20220306203236443](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306203236443.png)

    + 分组![image-20220306203319799](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220306203319799.png)

    + 