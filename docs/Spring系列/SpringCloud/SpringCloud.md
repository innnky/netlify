# SpringCloud

## 引入

+ 架构演变

  ![image-20220410184448441](https://home.innky.xyz:25566/images/image-20220410184448441.png)

  + 单体架构orm-垂直架构mvc-分布式架构rpc-面向服务体系架构SOA

+ 微服务解决方案

  + 阿里系springboot + dubbo + zookeepr
  + SpringCloud技术栈

+ 定义

  + ![image-20220410204440029](https://home.innky.xyz:25566/images/image-20220410204440029.png)
  + 各种组件![image-20220410205927042](https://home.innky.xyz:25566/images/image-20220410205927042.png)

+ 命名与版本选择

  + 早期:按伦敦地铁站名A-H

    ![image-20220410210336161](https://home.innky.xyz:25566/images/image-20220410210336161.png)

  + 最新命名 :2020.2 年份命名

  + 版本对应关系不能改

    ![image-20220410210554839](https://home.innky.xyz:25566/images/image-20220410210554839.png)

## 环境搭建

+ 创建父项目

  ```xml
  <properties>
      <spring.cloud-version>Hoxton.SR8</spring.cloud-version>
  </properties>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-parent</artifactId>
    <version>2.2.6.RELEASE</version>
  </parent>
  <dependencyManagement>
      <dependencies>
          <dependency>
              <groupId>org.springframework.cloud</groupId>
              <artifactId>spring-cloud-dependencies</artifactId>
              <version>${spring.cloud-version}</version>
              <type>pom</type>
              <scope>import</scope>
          </dependency>
      </dependencies>
  </dependencyManagement>
  ```

+ 继承springboot父项目

  ![image-20220410212430806](https://home.innky.xyz:25566/images/image-20220410212430806.png)

## 服务注册中心

+ 定义

  ![image-20220410212659826](https://home.innky.xyz:25566/images/image-20220410212659826.png)

+ 常用组件:

  + eureka zookeepr consul nacos
  + eureka
    + 包含 Eureka Server /Client

### Server

+ 创建子模块,引入springweb

+ 引入eureka server

  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
  </dependency>
  ```

+ 配置文件

  ![image-20220410213455494](https://home.innky.xyz:25566/images/image-20220410213455494.png)

  + 必须有服务名,不能重名,不能出现下划线,不区分大小写,最好全大写

    ![image-20220410214233589](https://home.innky.xyz:25566/images/image-20220410214233589.png) 
    
  + 关闭立即注册 fetch-registry: false

  + 关闭自己注册自己register-with-eureka: false

  + ```yaml
    server:
      port: 8761
    
    spring:
      application:
        name: EUREKASERVER
    
    eureka:
      client:
        service-url:
          defaultZone: http://localhost:8761/eureka/
        fetch-registry: false
        register-with-eureka: false
    ```

+ 入口类加注解![image-20220410213555766](https://home.innky.xyz:25566/images/image-20220410213555766.png)

### Client

+ 引入依赖
  + spring web
  + eureka client
    + ![image-20220411095122539](https://home.innky.xyz:25566/images/image-20220411095122539.png)
+ 配置文件
  + ![image-20220411095012432](https://home.innky.xyz:25566/images/image-20220411095012432.png) 
  + ![image-20220411095207905](https://home.innky.xyz:25566/images/image-20220411095207905.png)
+ 入口类加注解![image-20220411095241407](https://home.innky.xyz:25566/images/image-20220411095241407.png)

### 自我保护机制

+ ![image-20220411095901211](https://home.innky.xyz:25566/images/image-20220411095901211.png)

+ 触发机制

  + ![image-20220411100611202](https://home.innky.xyz:25566/images/image-20220411100611202.png)

  + 关闭方法服务端

    ![image-20220411100645828](https://home.innky.xyz:25566/images/image-20220411100645828.png)

  + 客户端![image-20220411100903642](https://home.innky.xyz:25566/images/image-20220411100903642.png)

  + 官方不推荐关闭

### eureka server集群

+ 完全集群
  + 创建多个springboot项目,配置不同的端口与依赖
  + 配置文件配置副本集,配置另外的节点![image-20220411101426959](https://home.innky.xyz:25566/images/image-20220411101426959.png)
  + 客户端只需要像其中一个进行注册,其他会自动同步(但客户端也应该写全部节点)(与上面一样)
+ 集群同一个服务需要用同一个名字
+ 

