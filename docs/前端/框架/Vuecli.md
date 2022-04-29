# VueCli

## 目录结构

![image-20220211151612451](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220211151612451.png)

+ 局部注册

  ```html
  <div id="app-2">
      <Child></Child>
  </div>
  
  <script>
      //局部注册
      var child={
          template:'<div>这是一个局部注册组件</div>'
      }
      new Vue({
          el:"#app-2",
          components:{child}
      })
      
  </script>
  ```

+ 路由：可以使用redirect进行重定向

  ```javascript
  export default new Router({
    routes: [
      {path: '/', redirect: '/HelloWorld'},
      {path: '/HelloWorld', component: HelloWorld},
      {path: '/User', component: User}
    ]
  })
  ```

+ 组件：必须有一个根容器，否则无法识别组件

+ axios

  + npm install axios --save-dev
  + main.js 中import axios from "axios"
  + Vue.prototype.$http = axios
  + Vue.prototype.$http.defaults.baseURL = ''
  + this.$http.get() ......

+ 子路由![image-20220211172414997](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220211172414997.png)

+ xxxx.log   -> console.log(xxxx)

+ 切换路由

  ![image-20220211172859101](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220211172859101.png)

+ 监听路由

  ![image-20220211173009626](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220211173009626.png)

## 部署

+ 打包 vue run build
+  