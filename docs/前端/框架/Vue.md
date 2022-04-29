# Vue

+ CSS预处理器
+ 行为层
+ webpack打包
+ vue同时支持了模块化和虚拟DOM 

## 环境搭建

+ IDEA添加VUE插件
+ 引入vue.js文件

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2.5.16/dist/vue.js"></script>
or
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>

```

+ Hello Vue样例

```html
<div id="app">
  {{ message }}
</div>
<script>
    var app = new Vue({
      el: '#app',
      data: {
        message: 'Hello Vue!'
      }
    })
</script>

```

+ MVVM的优点

![image-20220119095659990](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119095659990.png)

+ 以下为通过v-bind指令，将span标签的title属性，与vue实例的message属性，进行绑定

```html
<div id="app-2">
  <span v-bind:title="message">
    鼠标悬停几秒钟查看此处动态绑定的提示信息！
  </span>
</div>
<a v-bind:href="dt.href"></a>
```

+ 只加载一次后不改变

  ```html
  <span v-once>这个将不会改变: {{ msg }}</span>
  ```

## 判断循环

+  单分支判断，if内部为表达式

```html
  <p v-if="seen">现在你看到我了</p>
```

+ 多分支

```html
  <p v-if="seen==='A'">a</p>
  <p v-else-if="seen==='B'">b</p>
  <p v-else>other</p>
```

+ 循环

```html
<div id="app-4">
  <ol>
    <li v-for="todo in todos">
      {{ todo.text }}
    </li>
  </ol>
</div>
```



## 事件

+ 定义实例中的方法：在构造函数method下定义

```javascript
var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'Hello Vue.js!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
```

+ 为组件绑定事件方法

```html
<button v-on:click="reverseMessage">反转消息</button>
```

## 数据双向绑定

+ v-model 将input对象的value值与Vue实例中的message属性进行双向绑定，同步相互更新

```html
<div id="app-6">
  <p>{{ message }}</p>
  <input v-model="message">
</div>
```

+ 单选框对象的绑定

![image-20220119101434406](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119101434406.png)

+ 下拉框对象的绑定

![image-20220119101630141](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119101630141.png)

## 组件

+ 定义组件

```javascript
Vue.component('todo-item', {
  template: '<li>这是个待办项</li>'
})
//之后便可以使用<todo-item></todo-item>来显示该组件
```

+ 组件的数据传递

```javascript
Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})
//接受一个todo参数，在使用组件时使用v-bind:todu="parameter"传入parameter参数
//调用时还需传入			      v-bind:key="item.id"

```



![image-20220119102139544](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119102139544.png)

## 异步通信

+ vue推荐使用axios进行网络通信

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

+ 可以直接在方法中this.xxx修改data中的数据以达到与页面交互

```html

<div id="app">{{message}}</div>
<script>
    var vm = new Vue({
        el: "#app",
        data: {
            message: "hello, vue!"
        },
        mounted: function(){
            axios.get("../data.json").then(response=>{
                this.message = response.data.netmessage;
            })
        }
    });
</script>
```

+ js知识点：箭头函数并没有 `this`
+ 解决加载闪烁问题

<img src="https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119103423852.png" alt="image-20220119103423852" style="zoom:33%;" />

## 计算属性

+ 将计算结果缓存在**属性**中，但一旦其中的参数变化也会刷新
+ **计算属性**定义：在构造函数computed下定义

![image-20220119110317621](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119110317621.png)

## 内容分发

slot（插槽）

![image-20220119110836707](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119110836707.png)

![image-20220119111319851](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119111319851.png)

获取循环中的index 

![image-20220119111429864](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119111429864.png)

## Vue-cli

+ 环境搭建
  + npm安装淘宝镜像 `npm install cnpm -g`
  + 安装vue-cli `npm install vue-cli -g`
  + 使用`vue list`查看可创建的模板
  + 使用`vue init webpack projectname`
  + 进入项目文件夹后`npm install`安装依赖
  + 使用`npm run dev`启动
+ 通过export暴露接口导出  使用import导入

## WebPack

+ 环境搭建

  + `npm install webpack -g`
  + `npm install webpack-cli -g`

+ 暴露一个方法

  ![image-20220119213237072](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119213237072.png)

+  引入并调用方法

  ![image-20220119213348512](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119213348512.png)

+ 打包模块配置文件

  ![image-20220119213538231](https://cdn.jsdelivr.net/gh/innnky/images@master/uPic/image-20220119213538231.png)

+ 打包将整个项目编译成一个js，使用只需引入一个js即可

## Vue-Router

+ 安装`npm install vue-router --save-dev`
+ 引入`importy VueRouter from 'vue-router'`
+ 显示声明使用`Vue.use(VueRouter)`
