# VBlog

+ SpringSecurity配置跨域https://www.cnblogs.com/kenx/p/15201283.html
  + 两步：开启配置，放一个bean
  
+ nodejs似乎可以代理解决跨域问题

+ 通过这个计算start![image-20220303145756701](https://home.innky.xyz:25566/images/image-20220303145756701.png)![image-20220303145850272](https://home.innky.xyz:25566/images/image-20220303145850272.png)

+ 如文章对tag的1对多关系中tag可能为空，则连接需要使用左连接

+ 使用

+ ```xml
  <resultMap id="BaseResultMap" type="xyz.innky.web.bean.Article">
      <id column="id" property="id"/>
      <result column="title" property="title"/>
      <result column="cid" property="cid"/>
      <result column="uid" property="uid"/>
      <result column="publishDate" property="publishDate"/>
      <result column="editTime" property="editTime"/>
      <result column="state" property="state"/>
      <result column="pageView" property="pageView"/>
      <result column="mdContent" property="mdContent"/>
      <result column="htmlContent" property="htmlContent"/>
      <result column="summary" property="summary"/>
      <result column="nickname" property="nickname"/>
      <result column="cateName" property="cateName"/>
      <collection property="tags" ofType="xyz.innky.web.bean.Tags" column="tagName">
          <id property="id" column="tid"/>
          <result property="tagName" column="tagName"/>
      </collection>
  </resultMap>
  ```

  将多条数据封装到一个对象中，关键点collection

+ 检查权限是否包含xxx

  ```java
  @RequestMapping("/isAdmin")
  public Boolean isAdmin() {
      Collection<? extends GrantedAuthority> authorities = Util.getCurrentUser().getAuthorities();
      for (GrantedAuthority authority : authorities) {
          if (authority.getAuthority().contains("超级管理员")) {
              return true;
          }
      }
      return false;
  }
  ```

+ 同时更新多条文章：mybatis传入一个数组然后使用

+ ```xml
   WHERE id IN <foreach collection="aids" item="aid" separator="," open="(" close=")">
      #{aid}
  </foreach>
  ```

+ 进行遍历修改或删除

+ 删除多条的时候判是否删除成功需要比较返回的数量与待删除数据的数量是否相等

+ 定时任务

   + 启动类加入@EnableScheduling
   + 组件方法加入@Scheduled(cron = "* * * * * ?")
      + 填写cron表达式https://www.cnblogs.com/yanghj010/p/10875151.html
   + 