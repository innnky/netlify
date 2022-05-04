# JDK8

## lambda表达式

+ 使用

  + ![image-20220409102935375](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409102935375.png)

  + 简化匿名内部类的使用

  + 语法规则

    ![image-20220409103303906](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409103303906.png)

+ 具有单个方法的接口貌似可以直接使用lambda表达式代替匿名内部类

+ 注解:@FunctionalInterface

  + 只能声明一个抽象方法

+ 原理

  + 匿名内部类的实现原理![image-20220409104325448](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409104325448.png)
  + lambda表达式编译后不会形成新的类
    + 在类中新生成一个私有的静态方法
    +  **运行时**生成一个类,在这个类中调用了静态方法
  
+ 省略模式

  + ![image-20220409171911917](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409171911917.png)
  + ![image-20220409171926617](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409171926617.png)

+ 前提条件

  + ![image-20220409172045840](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409172045840.png)

  + 举例:(局部变量)

    ![image-20220409172239445](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409172239445.png)

+ 与匿名内部类的区别:

   ![image-20220409172636453](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409172636453.png)

### 接口默认方法与静态方法

+ 默认方法
  + 优势:方便了接口的拓展(添加默认方法实现类可以不用修改)
  + ![image-20220409172931340](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409172931340.png)
+ 静态方法
  + 加static关键字
  + **不可重写**
  + **实现类不可调用**
  + 只可以使用接口名调用

### 内置函数式接口

+ 常用内置接口

   ![image-20220409173546737](/Users/xingyijin/Library/Application%20Support/typora-user-images/image-20220409173546737.png)

+  Supplier:供给型 get()

+ Consumer: 消费型 accept()

  + 两个consumer顺序执行

     ![image-20220409185444268](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409185444268.png)

+ Function接口apply() 也可以andThen

+ Predicate接口 test() 

  + 多条件组合:(与或非)
    + ![image-20220409190652541](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409190652541.png) 
    + ![image-20220409190810114](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409190810114.png) 
    + 去取反![image-20220409190920421](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409190920421.png)

## 方法引用

+ ![image-20220409191301744](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409191301744.png)

+ 常见引用方式

   ![image-20220409191744206](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409191744206.png)

+ 对象::方法名

  + ```java
    Date now = new Date();
    Supplier<Long> supplier = () -> {
        return now.getTime();
    };
    //等效于
    Date now = new Date();
    Supplier<Long> supplier = now::getTime;
    ```

  + 引用方法的参数和返回值必须与接口中的一样

+ 类名::静态方法

+ 类名::实例方法

  + ![image-20220409193323596](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409193323596.png)
    + 引用无参方法
  + ![image-20220409193305132](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409193305132.png)
    + 引用单参数方法
  + 类名::new 
    + ![image-20220409193656691](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409193656691.png) 
      + 引用无参构造
    + ![image-20220409193811144](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409193811144.png) 
      + 引用有参构造
  + 数组::new ![image-20220409194121876](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409194121876.png)

## Stream流

+ ![image-20220409194504822](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409194504822.png)

### 获取Stream流

+ Collection接口默认方法:.stream()
+ Stream接口的静态方法of![image-20220409195533758](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409195533758.png)
  + ![image-20220409195611532](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409195611532.png)
  + 不能传基本数据类型数组

### 常用方法

+ 分类:终结方法和非终结方法

  ![image-20220409195916331](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409195916331.png)

+ 注意事项 

  + Stream只能操作一次
    + 终结方法调用完后就不能再操作了  
  + 非终结方法返回的是新的流(不是同一个对象)
  + Stream不调用终结方法，中间的操作不会执行

+  终结方法:

  + foreach: Consumer
  + count: 统计元素个数
  + allMatch: Predicate 流中所有元素是否都成功返回真
  + anyMatch: 任意一个满足返回真
  + noneMatch: 所有元素都不满足
  + 返回Optional
    + findAny() findFirst() :找一个元素(first保证找第一个 any不保证)
    + max min: Comparator 返回最大/最小
    + reduce: 
      ![image-20220409203115676](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409203115676.png)

+ 非终结:

  + filter: Predicate
  + limit: 获取前几个数据
  + skip: 跳过前几个数据
  + map: Function将一种流转成另一类型的流![image-20220409201246285](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409201246285.png)
    + ![image-20220409201406262](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409201406262.png)
  + sorted() sorted(Comparator)
  + distinct(): 去重(自定义对象要重写equals和hashcode)
  + mapToInt: 减少自动装箱与拆箱,转化为IntStream(没有包装类了)

+ 静态方法

  + concat()合并两个流![image-20220409205319807](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409205319807.png)
    + 合成后不能操作之前的流

### 实例

+ map与reduce组合使用
  + ![image-20220409204425965](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409204425965.png)
  + ![image-20220409204437022](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409204437022.png)
  + ![image-20220409204746521](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409204746521.png)

### 结果收集

+ 收集

  + .collect(参数)
    + Collectors.toList/toSet
    + Collectors.toCollection(ArrayList::new/Hashset::new)
  + 收集到数组![image-20220409210250707](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220409210250707.png)

+ 聚合

  + ![image-20220410110144500](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410110144500.png)
  + ![image-20220410111729441](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410111729441.png)

+ 分组

  + ![image-20220410112333799](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410112333799.png)

  + map的遍历

     ![image-20220410112235689](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410112235689.png)

  + 以条件分组

    ![image-20220410112410460](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410112410460.png)

+ 多级分组

  + ![image-20220410112539955](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410112539955.png)

+ 分区![image-20220410112725748](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410112725748.png)

+ 拼接![image-20220410112821100](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410112821100.png)

  + ![image-20220410112919884](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410112919884.png)

### 并行数据流

+ 获取方式

  + list转![image-20220410115709029](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410115709029.png)
  + 串行流转![image-20220410115737049](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410115737049.png)

+ 解决线程安全

  + 加锁,使用同步代码块
  + 使用线程安全的Vector
  + 将List转为线程安全的![image-20220410120745773](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410120745773.png)
  + 使用collect![image-20220410120836708](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410120836708.png)

+ 原理:fork/join

  + 构成

     ![image-20220410121105483](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410121105483.png)

  + 原理

    + 分治法:将大问题拆分成小任务

      ![image-20220410121157564](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410121157564.png)

    + 工作窃取算法:有空闲时窃取其他线程的任务执行

## Optional类

+ 创建对象
  + of方法(不能传空值)
  + ofNullable(可以传空值)
  + empty()创建空对象
+ 方法
  + isPresent()有值返回true
  + get()获取值(如果没有值会报错)
  + orElse(value)有值取值,没值取出传入的value默认值
  + ifPresent(consumer)有值就调用表达式
  + ifPresentOrElse(consumer, emptyConsumer)(jdk1.9)
  + map()继续返回一个Optional
+ 实例
  + ![image-20220410123841239](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410123841239.png)
    + 如果不使用optional则需要多次判空,多层嵌套
    + 使用optional 是先定义一系列操作不执行,最后执行时候中途返回空则调用orElse

## 新日期与时间api

+ 旧api的问题

  + 设计不合理(如年份从1900年开始算)
  + 时间解析和格式化是线程不安全的
  + 处理时区麻烦

+ 相关类

  + LocalDate
    + static now()获取当前时间
    + static of(year, month, dayOfMonth)
    + getYear() getMonth()(返回枚举) getMonthValue()

  + LocalTime
    + static of(h, m, s)
    + static now()
    + getMinute()....

  + LocalDateTime
    + static of() now()
    + get....

+ 修改时间

  + 设值withYear() withMonth()....
    + 修改后产生新的时间对象(不修改原有的时间对象)

  + 增减时间.plusYears() .minusYears()
  + 比较时间 isAfter(other) isBefore() isEqual() 返回布尔

+ 时间格式化与解析DateTimeFormatter

  + 常量:![image-20220410170535744](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410170535744.png)
  + static ofParttern("yyyy-MM-dd HH-mm-ss")
    + localDateTime.format(dtf)
    + DateTimeFormatter.parse(字符串, dtf)
    + 线程安全

+ 时间戳 Instant

  + static now()
  + plusSeconds() 
  + getEpochSecond() getNano()

+ 计算日期与时间差

  + Duration 计算时间差
    + static between(t1, t2)
    + toDays() toHours() toMinutes() (有正负)

  + Period 计算日期差
    + static between(d1, d2)
    + toYears() ....

+ 时间矫正器

  + ![image-20220410171852517](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410171852517.png)

  + 自带的:

    ![image-20220410171928886](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410171928886.png)

+ 带时区的日期

  + ![image-20220410172059234](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410172059234.png)
  + ![image-20220410172145869](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410172145869.png)不带参数使用计算机默认时区
  + 创建指定时区的![image-20220410172254143](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410172254143.png)
  + 修改时区![image-20220410172334978](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410172334978.png)
    + 不改时间![image-20220410172439890](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410172439890.png)

+ 总结

  + ![image-20220410172614801](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410172614801.png)


## 重复注解

+ 需要先创建一个容器,之后![image-20220410173000819](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410173000819.png)
+ 类型注解->![image-20220410173211004](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220410173211004.png)

## JDK7

+ try-with-resource

  + ```java
    Scanner scanner = null;
    try {
        scanner = new Scanner(new File("test.txt"));
        while (scanner.hasNext()) {
            System.out.println(scanner.nextLine());
        }
    } catch (FileNotFoundException e) {
        e.printStackTrace();
    } finally {
        if (scanner != null) {
            scanner.close();
        }
    }
    
    //替换为
    
    try (Scanner scanner = new Scanner(new File("test.txt"))) {
        while (scanner.hasNext()) {
            System.out.println(scanner.nextLine());
        }
    } catch (FileNotFoundException fnfe) {
        fnfe.printStackTrace();
    }
    ```

  + 
