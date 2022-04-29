# Java 并发编程

## 引入

+ 线程状态

```java
public enum State {
  
    NEW,

    RUNNABLE,

    BLOCKED,

    WAITING,

    TIMED_WAITING,

    TERMINATED;
}
```

+ wait与sleep
  + wait是Object类方法 会释放锁
  + sleep是Thread类静态方法 不会释放锁
+ 管程
  + 管程封装了PV操作，实现了对临街资源的互斥访问，对外提供同步方法入口，同一时间只能有一个线程访间
+ 用户线程与守护线程
  + 用户线程：自定义线程
  + 守护线程：运行在后台，如垃圾回收
    + ![image-20220422102323181](https://home.innky.xyz:25566/images/image-20220422102323181.png)是否为守护线程；.setDaemon(true)
    + 当没有用户线程只剩守护线程则jvm结束

## Lock接口

+ synchronized 关键字

+ 多线程编程步骤

   ![image-20220422110250099](https://home.innky.xyz:25566/images/image-20220422110250099.png)

+ 创建线程的多种方式

  ![image-20220422103221244](https://home.innky.xyz:25566/images/image-20220422103221244.png) 

+ lock接口

  + 为接口，有诸多实现类

    ![image-20220422103525154](https://home.innky.xyz:25566/images/image-20220422103525154.png)

  + 可重入锁ReentrantLock

    + 创建![image-20220422103800476](https://home.innky.xyz:25566/images/image-20220422103800476.png)
    + 上锁lock.lock();
    + 临界操作放在try中
    + 解锁lock.unlock();
    + 解锁放在finally代码块中

  + 区别![image-20220422104206323](https://home.innky.xyz:25566/images/image-20220422104206323.png)

  + 竞争资源激烈时Lock接口比synchronized高效

## 线程通讯

+ 线程通讯synchronized配合wait和notify

  + 个人理解
    + this.wait()以this对象为锁,中断调用线程转入this对象的等待队列(会释放锁)
    + this.notifyAll()将this对象所有正在等待队列的线程释放
  + wait方法应该写在while循环中,否则会有虚假唤醒
    + ![image-20220422105943724](https://home.innky.xyz:25566/images/image-20220422105943724.png) 

+ 使用Lock接口实现通讯

  + ![image-20220422110514422](https://home.innky.xyz:25566/images/image-20220422110514422.png)
  + 方法体![image-20220422110557955](https://home.innky.xyz:25566/images/image-20220422110557955.png)
  + 区别
    + wait换成await()
    + notifyAll()换成signalAll()

+ 线程定制化通讯:使用标志位![image-20220422111056267](https://home.innky.xyz:25566/images/image-20220422111056267.png)

   + 关键代码

      while(flag ==1 ){

       ![image-20220422155016624](https://home.innky.xyz:25566/images/image-20220422155016624.png)

   + 据弹幕所言,似乎有flag的情况是不需要多个condition的 存疑

## 集合线程安全

+ 并发修改问题

  + 在集合的存于取时会出现并发修改异常

+ ArrayList解决方案

  + 使用Vector

  + Collections![image-20220422160145382](https://home.innky.xyz:25566/images/image-20220422160145382.png)

  + CopyOnWriteArrayList![image-20220422160256288](https://home.innky.xyz:25566/images/image-20220422160256288.png)

    + 原理:写时复制

      ![image-20220422160429232](https://home.innky.xyz:25566/images/image-20220422160429232.png)

    + 与Vector区别: **写互斥,但写时仍可以读,Vector读写也互斥**

+ Set

  + 使用![image-20220422161330112](https://home.innky.xyz:25566/images/image-20220422161330112.png)

+ Map

  + 使用![image-20220422161516635](https://home.innky.xyz:25566/images/image-20220422161516635.png)

## 多线程锁

+ 公平锁和非公平锁

  + ![image-20220422162246155](https://home.innky.xyz:25566/images/image-20220422162246155.png)
  + 默认是非公平锁false:效率高,可能出现饿死现象(饥饿)
  + 公平锁效率低

+ 可冲入锁(递归锁)![image-20220422162535745](https://home.innky.xyz:25566/images/image-20220422162535745.png)

  + ![image-20220422162906375](https://home.innky.xyz:25566/images/image-20220422162906375.png)
  + 即在持有锁的时候可以大开使用同一把锁的任意其他地方
  + lock方式实现时候同一把锁**也需要释放多次**(并不是说释放一次就行)

+ 死锁检测

  ![image-20220422163907717](https://home.innky.xyz:25566/images/image-20220422163907717.png)

  +  jps -l 
  + jstack pid

## Callable接口

```java
@FunctionalInterface
public interface Callable<V> {
    /**
     * Computes a result, or throws an exception if unable to do so.
     *
     * @return computed result
     * @throws Exception if unable to compute a result
     */
    V call() throws Exception;
}
```

+ 创建线程方式:

  + Callable接口方式:可以有返回值
  + 线程池方式

+ 与Runable区别

  ![image-20220422164222647](https://home.innky.xyz:25566/images/image-20220422164222647.png)

+ 使用:适配器模式FutureTask

  + 持有Callable接口,实现Runnable

+ 举例![image-20220422165148227](https://home.innky.xyz:25566/images/image-20220422165148227.png)

+ 案例

  + 通过futureTask.get()获取返回值
  + <img src="https://home.innky.xyz:25566/images/image-20220422165358941.png" alt="image-20220422165358941" style="zoom:50%;" />
  + 通过isDone获取完成状态![image-20220422165502780](/Users/xingyijin/Library/Application%20Support/typora-user-images/image-20220422165502780.png)
  + get多次只会执行一次计算(未来任务完成后会将结果保存)

## JUC辅助类

+ 减少计数CountDownLatch

  + 构造方法设置初始值
  + countDown方法 减一
  + await方法 等待值变成0

+ CyclicBarrier

  ```
  CyclicBarrier 看英文单词可以看出大概就是循环阻塞的意思，在使用中
  CyclicBarrier的构造方法第一个参数是目标障碍数 ，每次执行 Cyclic Barrier
  次障碍数会加-
  ，如果达到了目标障碍数，才会执行 cyclic Barrier.await0之后
  的语句。可以将 CyclicBarrier 理解为加1操作。
  ```

  + 举例:集齐7颗龙珠就可以召唤神龙

  + ![image-20220422191354430](https://home.innky.xyz:25566/images/image-20220422191354430.png)

     ![image-20220422191411571](https://home.innky.xyz:25566/images/image-20220422191411571.png)

  + 等待线程到达阈值执行方法

+ 信号量Semaphore

  + pv操作acquire release 同操作系统

## 读写锁

+ 乐观与悲观锁

+ 表锁和行锁(行锁会发生死锁)

+ 读锁(共享锁)和写锁(独占锁)(都会发生死锁)

+ 案例

  + ![image-20220422194557708](https://home.innky.xyz:25566/images/image-20220422194557708.png)
  + 休眠时间            TimeUnit.MINUTES.sleep(0);

+ ReentrantReadWriteLock读写锁

  + 创建![image-20220422195931235](https://home.innky.xyz:25566/images/image-20220422195931235.png) 

  ![image-20220422195225447](https://home.innky.xyz:25566/images/image-20220422195225447.png)

  + 写锁创建 rwLock.writeLock().lock()

  + 释放![image-20220422195355135](https://home.innky.xyz:25566/images/image-20220422195355135.png)

  + 读写锁缺陷

     ![image-20220422200941937](https://home.innky.xyz:25566/images/image-20220422200941937.png)

  + 锁降级

    + ![image-20220422201745877](https://home.innky.xyz:25566/images/image-20220422201745877.png)
    + (写锁降级成写锁后可以让别人进来)
    + 获取写锁后同一个线程可以继续去获取读锁

## 阻塞队列

+ ![image-20220423075606824](https://home.innky.xyz:25566/images/image-20220423075606824.png)

  ```
  当队列是空的，从队列中获取元素的操作将会被阻塞。
  当队列是满的，从队列中添加元素的操作将会被阻塞。
  试图从空的队列中获取元素的线程将会被阻塞，直到其他线程往空的队列插入新的元素•
  试图向已满的队列中添加新元素的线程将会被阻塞，直到其他线程从队列中移除一个或多
  个元素或者完全清空，使队列变得空闲起来并后续新增。
  ```

+ 接口 BlockingQueue:类似于生产者消费者问题

  + 实现类ArrayBlockinqQueue基于定长数组, DelayQueue, LinkedBlockinqDeque, LinkedBlockingQueue, PriorityBlockingQueue,
    SynchronousQueue
  + 方法![image-20220423080315870](https://home.innky.xyz:25566/images/image-20220423080315870.png)

## 线程池

+ 线程池特点

  ```
  降低资源肖耗：通过重复利用己创建的线程降低线程创建和销毁造成的销耗。
  提高响应速度：当任务到达时 ，任务可以不需要等待线程创建就能立即执行。
  提高线程的可管理性：线程是稀缺资源，如果无限制的创建，不仅会销耗系统资
  源，还会降低系统的稳定性，使用线程池可以进行统
  -的分配，调优和监控。
  Java 中的线程池是通过 Executor-框架实现的，该框架中用到了 Executor , Executors
  ExecutorService, ThreadPoolExecutor这几个类
  ```

+ ![image-20220423081136585](https://home.innky.xyz:25566/images/image-20220423081136585.png)

+ 分类

  + 一池n线程ExecutorService threadPooll = Executors.newFixedThreadPool(int) --阿里不推荐
    + threadPool.execute(Runnable)
    + 最后要关闭线程池threadPooll.shutdown();
  + 一个任务一个任务执行，一池一线程Executors.newSingleThreadExecutor()
    + 代码同上
  + 线程池根据需求创建线程，可扩容，遇强则强Executors.newCachedThreadPool()

+ 原理

  +  ThreadPoolExecutor 构造参数![image-20220423082942838](https://home.innky.xyz:25566/images/image-20220423082942838.png)

  + 执行流程![image-20220423083332794](https://home.innky.xyz:25566/images/image-20220423083332794.png)

  + 内置拒绝策略

    + AbortPolicy默认 抛出异常
    + CallerRunsPolicy
    + DiscardOldestPoliy
    + DiscardPolicy

  + 规范:

    ```
    【强制】线程池不允许使用 Executors 去创建，而是通过 ThreadPoolExecutor 的方式
    这样的处理方式让写的同学更加明确线程池的运行规则，规避资源耗尽的风险。
    说明：Executors 返回的线程池对象的弊端如下：
    1) FixedThreadPool fl SingleThreadPool:
    允许的请求队列长度为 Integer.MAX_VALUE，可能会堆积大量的请求，从而导致 ooM。
    2) CachedThreadPool Al ScheduledThreadPool:
    允许的创建线程数量为 Integer.MAX_VALSE，可能会创建大量的线程，从而导致 OOM。
    ```

  + 自定义创建连接池![image-20220423084020964](https://home.innky.xyz:25566/images/image-20220423084020964.png)

## Fork/join

+ ![image-20220423085445296](https://home.innky.xyz:25566/images/image-20220423085445296.png)
+ ![image-20220423085511525](https://home.innky.xyz:25566/images/image-20220423085511525.png)
+ ![image-20220423085532119](https://home.innky.xyz:25566/images/image-20220423085532119.png)
+ ![image-20220423085642865](https://home.innky.xyz:25566/images/image-20220423085642865.png)

## 异步回调

+ ![image-20220423085819658](https://home.innky.xyz:25566/images/image-20220423085819658.png)
+ ![image-20220423085927373](https://home.innky.xyz:25566/images/image-20220423085927373.png)
+ ![image-20220423090041407](https://home.innky.xyz:25566/images/image-20220423090041407.png)
+ 

