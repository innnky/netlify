+ Emmet

  + ! tab生成网页框架
  + lorem lorem3 lorem*3
  + 类选择器.container
  + id选择器#btn
  + 标签选择a 
  + 复合a.test
  + 嵌套.test>a.test

+ 加载js文件

  + 放在head中加上defer属性（延迟加载）
  + 放在body的最下方

+ navbar模板

  ```html
  <nav class="navbar navbar-expand-md bg-dark navbar-dark">
      <div class="container">
          <a href="#" class="navbar-brand">我在b站玩编程</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navmenu">
              <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navmenu">
              <ul class="navbar-nav">
                  <li class="nav-item">
                      <div class="nav-link">前端认知</div>
                  </li>
                  <li class="nav-item">
                      <div class="nav-link">后端认知</div>
                  </li>
                  <li class="nav-item">
                      <div class="nav-link">数据库</div>
                  </li>
              </ul>
          </div>
      </div>
  </nav>
  ```

+ 不同的大块之间使用section+div.container包裹

+ my-4 等同于margin top bottom 4

+ 黑底白字bg-dark text-light

+ 小屏不显示 大屏显示 d-none d-md-block

+ 小屏居中 大屏靠左text-center text-md-start

+ card模板

  ```html
  <div class="card bg-secondary text-light">
      <div class="card-body text-center">
          <div class="card-title">前端知识</div>
          <div class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci aspernatur
              excepturi officia possimus quo sequi. Cum illum itaque
          </div>
          <a href="#" class="btn btn-primary mt-2">学习前端</a>
      </div>
  </div>
  ```

+ img-fluid 宽度100% 高度auto

+ 手风琴组件模板

  ```html
  <div class="accordion accordion-flush" id="accordionFlushExample">
      <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingOne">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                      data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                  Accordion Item #1
              </button>
          </h2>
          <!--默认展开第一项 show-
          <div id="flush-collapseOne" class="accordion-collapse collapse show" aria-labelledby="flush-headingOne"
               data-bs-parent="#accordionFlushExample">
              <div class="accordion-body">Placeholder content for this accordion</div>
          </div>
      </div>
      <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingTwo">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                      data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                  Accordion Item #2
              </button>
          </h2>
          <div id="flush-collapseTwo" class="accordion-collapse collapse" aria-labelledby="flush-headingTwo"
               data-bs-parent="#accordionFlushExample">
              <div class="accordion-body">Placeholder content for this accordion</div>
          </div>
      </div>
  </div>
  ```

+ p标签.lead

+ 