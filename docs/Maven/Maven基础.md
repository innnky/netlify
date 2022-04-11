

# Maven

> BV1dp4y1Q7Hf

+ maven功能

  + 管理jar文件
  + 自动下载jar，源代码，文档
  + 管理jar依赖
  + 管理jar版本
  + 编译程序
  + 测试代码
  + 打包文件
  + 部署项目

+ 构建：面向过程

  + 清理
  + 编译（批量）
  + 测试（批量）
  + 报告
  + 打包
  + 部署

+ 核心概念

  + pom：项目对象模型，控制maven项目
  + 约定的目录结构
  + 坐标：用来表示资源
  + 依赖管理
  + 仓库管理
  + 生命周期
  + 插件和目标
  + 继承
  + 聚合

+ 安装：下载->解压->配环境变量（M2_HOME+Path）

+ 约定的目录结构

  ![image-20220127101808534](https://home.innky.xyz:25566/images/image-20220127101808534.png)

  + mvn -compile: 编译src/main中所有java文件
    + 项目根目录编译后生成target目录
  + 默认仓库：user/.m2/repository/
    + 修改位置：配置文件conf/settings.xml->    <localRepository>本地仓库</localRepository>

+ 仓库:存放jar和插件

  + 本地仓库
  + 远程仓库：中央仓库、中央仓库的镜像、私服
  + 使用：
    + 本地仓库->私服->中央仓库

+ Pom文件

  + 坐标：互联网中唯一标识一个项目
    + <groupId>
    + <artifactId>
    + <version>
    + [通过**坐标**搜索项目](https://mvnrepository.com/)
  + packaging打包拓展名
  + dependences
  + properties
  + build:配置maven构建相关的参数，指定jdk，配置插件
    + plugins配置编译插件**想再稍微详细的了解一下**

+ Maven命令 ---通过插件完成实际功能

  + mvn clean
  + mvn compile
    + 编译main/java下的所有文件至target/classes中
    + 将main/resources复制到classes中 
  + mvn test-compile~p17~
  + mvn test
  + mvn packge
  + mvn install
    + 将项目安装到本地仓库，可以在别的项目中引用
  + 当执行生命周期后面的步骤时会把前面的步骤也执行一遍

+ 单元测试junit

  + 添加maven依赖
  + ![image-20220127110633517](https://home.innky.xyz:25566/images/image-20220127110633517.png)
  
+ 再IDEA中使用Maven

  + settings配置当前工程 other settings 为以后新建工程配置（new project setup）

  + 添加该选项后不会自动下载模板![image-20220127155218665](https://home.innky.xyz:25566/images/image-20220127155218665.png)

    -Darchtype.....

  + 使用模板创建项目

    + 最普通的java项目模板![image-20220127155835130](https://home.innky.xyz:25566/images/image-20220127155835130.png)、

  + 右键目录-> Make directory as
  
+ 依赖范围scope

  + compile 默认项 所有阶段（编译 测试 打包 部署）
  + test 仅测试时使用
  + provide 打包时不放入（编译 测试）

+ maven 属性设置

+ maven全局变量

  + 在<properties>中使用<>定义变量，使用${}访问

+ maven资源插件

  ![image-20220127195919966](https://home.innky.xyz:25566/images/image-20220127195919966.png)

  