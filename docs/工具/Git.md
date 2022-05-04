# Git

+ 主要流程

  <img src="https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220322213824893.png" alt="image-20220322213824893" style="zoom:25%;" /><img src="https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220322214233810.png" alt="image-20220322214233810" style="zoom:25%;" />

## 常用命令

+ ![image-20220323102852643](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323102852643.png)
+ 设置用户名邮箱：全局设置后会在Home目录中生成.gitconfig文件
+ git init初始化本地库后会在当前目录生成.git目录(linux 查看隐藏文件 ll -a)
+ Git status 查看本地仓库状态
+ git add 添加到暂存区
  + 删除暂存区![image-20220323104203409](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323104203409.png)
+ git commit  -m "日志信息" 文件名称
+ git reflog 查看历史记录
+ 修改文件：
  + 即使被修改的文件之前已经在库中了，修改后仍然要先add 再commit
+ 版本穿梭
  + ![image-20220323104907245](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323104907245.png)
  + 首先查看版本历史找到版本序号
  + 通过 git reset --hard 版本号回到过去版本

## 分支

+ head文件指向分支名，分支文件指向版本号，两者共同决定当前的版本

+ 好处：![image-20220323105444720](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323105444720.png)
+ 命令![image-20220323105509148](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323105509148.png)
+ git branch -v 查看分支
+ git branch 分支名 创建分支
+ git checkout 分支名 切换分支
+ git merge 分支名 把制定分支合并到当前分支上
+ 冲突处理 
  + 当同一个文件被不同的分支修改时，合并会产生代码冲突
  + 有冲突时合并git会修改冲突文件，此时处于合并状态，需要手动去冲突文件解决冲突
  + ![image-20220323110334515](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323110334515.png)
    + 将该文件再add commit解决冲突
    + 此时commit不需要跟文件名

## 团队协作github

+ git remote -v 查看当前所有远程库别名
+ git remote add 别名 远程地址
  + 创建完成后查看会有两个
+ git push 别名 分支名称
  + 首次push的时候会跳出登陆选项，问你是使用浏览器授权还是使用令牌
+ git pull 别名 分支名称
+ git clone 会自动设置远程库的别名为origin
+ 添加仓库成员->复制邀请函->成员通过邀请函接受邀请![image-20220323112749725](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323112749725.png)
  + 成为项目成员之后就可以push 了
+ 跨团队协作
  + fork-> 修改->pull request ->同意
+ ssh登陆
  + 生成密钥![image-20220323113530720](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323113530720.png)
  + 进入~/.ssh 复制公钥
  + 在GitHub 用户头像->setting->SSH and GPGkeys里添加公钥

## idea集成

+ 配置忽略文件（这个应该创建的是全局的）

  + 创建.gitignore文件

  + 在~/.gitconfig中配置忽略文件

    ![image-20220323114312119](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323114312119.png)

+ 切换版本![image-20220323115056118](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323115056118.png)

+ 创建分支

  ![image-20220323115215744](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220323115215744.png)

## github+idea

+ 使用token登陆
  + 用户头像->setting->developersettings ->personal access token->generate

## github token 登陆

git remote add 别名 https://生成的token@仓库地址即可登陆

