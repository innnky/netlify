# Vue项目

## 环境搭建

+ 安装cnpm

  ![image-20220212155043036](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212155043036.png)

+ 安装yarn

  ![image-20220212155115432](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212155115432.png)

+ 安装vue-cli

  ![image-20220212155140314](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212155140314.png)

  + vue -V 测试是否安装成功

+ 创建项目

  + vue create my-project  (不能有大写)
  + npm run serve (运行)

+ elementui

  + cdn引入

  + npm方式

    + 安装![image-20220212160041306](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212160041306.png)

    + 全局引入

      ![image-20220212160143587](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212160143587.png)

    + 按需引入

      + （可选）![image-20220212160435009](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212160435009.png)
      + 引入![image-20220212160642148](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212160642148.png)
      + 配置babel.config.js![image-20220212160550423](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212160550423.png)

  + 基础使用

    + 按钮添加点击事件

      ![image-20220212155823456](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212155823456.png)

      ![image-20220212155925933](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212155925933.png)

    + 弹出框绑定vue属性

      ![image-20220212160001462](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212160001462.png)

+ vuerouter安装![image-20220212160825452](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212160825452.png)

  + 引入![image-20220212160919874](C:/JavaLearning/%E5%89%8D%E7%AB%AF/%E6%A1%86%E6%9E%B6/image-20220212160919874.png)

  + 创建/router/index.js

    ![image-20220212161222150](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212161222150.png)

  + 使用按钮切换路由

    ![image-20220212161417488](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212161417488.png)

+ 安装less

  + ![image-20220212161743553](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212161743553.png)
  + ![image-20220212161753325](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212161753325.png)

## 网页搭建

+ 整体布局![image-20220212161653805](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212161653805.png)

+ 使用v-for 最好指定:key 可以提升渲染性能

+ :key是v-bind:key的简写

+ :class="此处是js的表达式，可以写运算比如连接字符串"

+ 去除自带的一堆html样式在app.vue中

  ```html
  <style>
  html,body{
    margin: 0;
    padding: 0;
  }
  #app {
    height: 100vh;
  }
  </style>
  ```

+ 使用@click绑定点击事件

  ```html
  <el-menu-item  @click="clickMenu(item)"  v-for="item in noChildren" :index="item.path" :key="item.path">
  ```

+ 使用this.$router.push(item.name)进行跳转

+ 使用嵌套路由

  + 在父页面的路由中加入children

    ```javascript
    const routes = [
        {
            path:'/',
            name:'Main',
            component: Main,
            children:[
                {
                    path: '/home',
                    name: 'home',
                    component: home
                },
                {
                    path: '/user',
                    name: 'user',
                    component: user
                }
            ]
        }
    ]
    ```

  + 在父页面中加入<router-view/>标签

  + 父页面中`this.$router.push(子页面路由如'home')`

+ 在main.js中引入样式文件

  ![image-20220212211554175](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220212211554175.png)

+ 使用图片

  + ```html
    <img :src="userImg">
    <script>
    export default {
      name: "CommonHeader",
      data(){
        return{
          userImg: require("../assets/logo.png")
        }
      }
    }
    </script>
    ```

  + 图片圆形

    ```less
    img{
      height: 40px;
      width: 40px;
      border-radius: 50%;
    }
    ```

+ flex布局居中：

  ```less
  header{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  ```

+ 组件间事件传递：vuex

  + cnpm i vuex 

    ```js
    Vue.use(Vuex)
    
    const store = new Vuex.Store({
      state: {
        count: 0
      },
      mutations: {
        increment (state) {
          state.count++
        }
      }
    })
    
    
    new Vue({
      store,
      router,
      render: h => h(App),
    }).$mount('#app')
    
    ```

  + 版本使用3.6.2

  + 使用this.$store.state.模块名.属性名  访问属性

  + 使用this.$store.commit('方法名', ...[参数列表]) 访问方法

  + map注入属性

    ```js
    import {mapState} from 'vuex'
    。。。
    computed: {
        ...mapState({
            tag: state => state.tab.tabList
        })
    }
    ```

  + 使用map注入方法

    ```js
     import {mapMutations} from 'vuex'
    methods:{
        ...mapMutations({
          deleteMenu:'deleteMenu'
        })
      }
    ```

+ <el-card shadow="hover" ></el-card>

+ table

  ```html
  <el-table :data="tableData">
    <el-table-column v-for="(val, key) in tableLabel" :key="key"
                     :prop="key" :label="val"></el-table-column>
  </el-table>
  ```
  
+ el-card

  ```html
  <div class="num">
    <el-card v-for="item in countData" :key="item.name" :body-style="{display:'flex', padding:0}">
      <i :class="'el-icon-'+item.icon" :style="{background:item.color}"></i>
      <div class="detail">
        <p class="num">{{ item.value }}</p>
        <p class="txt">{{ item.name }}</p>
      </div>
    </el-card>
  </div>
  ```

  + 注意body-style属性写法
  + 以及:style属性写法

+ 修改i图标大小

  ```html
  <i style="font-size: 60px" :class="'el-icon-'+item.icon" :style="{background:item.color}"></i>
  ```

+ 设置图标居中

  ```scss
  i {
    font-size: 30px;
    width: 80px;
    height: 80px;
    text-align: center;//****水平
    line-height: 80px;//****垂直
    color: #fff;
  }
  ```

+ axios使用

  + 坑：baseURL大小写

+ echarts

  + 获取html dom元素<div style="height: 280px" ref="ech"></div>

    ```javascript
    import * as echarts from 'echarts'
    const option = {
        xAxis:{
            data:sData
        },
        yAxis:{},
        legend:{
            data:['苹果','vivo','oppo','魅族',"三星", "小米"]
        },
        series:order.data
    }
    const E = echarts.init(this.$refs.ech)
    E.setOption(option)
    ```

+ vue 构造方法中watch属性监听值的变化

  ```js
  export default {
    name: "MyEchart",
    watch: {
      seriesData: {
        handler: function () {
          
        },
        deep: true
      }
    },
    data() {
      return {
        seriesData: []
      }
    }
  }
  ```

+ 修改面包屑导航的颜色

  ```less
  .el-breadcrumb ::v-deep .el-breadcrumb__inner {
    color: #d9bb95 !important;
  }
  ```

+ 使得鼠标放上去的时候是一个小手

  ```css
  cursor: pointer;
  ```

+ 获取当前路由

  ```js
  $route.name
  ```

+ 组件传递参数

  ```js
  export default {
    props:{
      formLabel:Array,
      form:Object,
      inline:Boolean
    },
    name: "CommonForm"
  }
  ```

+ 使用slot

  + 现在组件中写入<slot></slot>
  + 之后调用组件的时候插入组件中央<common-table>待插入的内容</common-table>

+ 事件

  + 在下层组件中向上抛出事件

  ```js
  this.$emit('changePage', page)
  ```

  + 在上层组件使用时指定处理的函数

    ```js
    @changePage="change"
    ```

+ Notice

  + 如果是全局引入，则已自动注册了诸如`$message $alert $confirm `等方法

  + 按需引入需要手动注册

    ```js
    Vue.prototype.$confirm = MessageBox.confirm
    ```

+ 路由相关操作（）

  ```js
  router.beforeEach((to, from, next)=>{
    store.commit('getToken')
    const token = store.state.user.token
    if(!token && to.name !== "login"){
      next('login');
    }else{
      next()
    }
  })
  new Vue({
    store,
    router,
    render: h => h(App),
  }).$mount('#app')
  ```

+ 关于绑定点击事件相关

  +  @click默认是指绑定的组件内部定义的click方法 如果组件没有定义click方法且需要绑定原生的点击事件，则需要使用@click.native