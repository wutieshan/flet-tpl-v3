# Jmeter使用手册


## 参考
> - [官方文档]()


## FAQs
### 1. 控制吞吐量


### 2. jsr223实现: 用户参数化, 在不同线程组间共享
```groovy
// setup thread group
// ===============================================
// 初始化参数
import java.util.concurrent.atomic.AtomicInteger;

AtomicInteger paramsLine = new AtomicInteger(0);
props.put("paramsLine", paramsLine);


// login fragment
// ===============================================
import java.util.concurrent.atomic.AtomicInteger;
import org.apache.commons.io.FileUtils;

AtomicInteger paramsLine = null;
synchronized(props) {
    if (props.get("paramsLine") == null) {
        paramsLine = new AtomicInteger(0);
        props.put("paramsLine", paramsLine);
    } else {
        params = props.get("paramsLine") as AtomicInteger;
    }

    def csvFile = new File("c:/tieshan/jmeter/scripts/......./p_userinfo.csv");
    if (vars.getObject("users") == null) {
        def users = FileUtils.readLines(csvFile, "utf-8");
        vars.putObject("users", users);
    }
}

def line = paramsLine.getAndIncrement();
def users = vars.getObject("users");
def rowIndex = line % (users.size() - 1); // 每次取一行, 排除首行, 循环(一般来说会准备足够的用户数据, 不会循环)
def currentUser = users.get(rowIndex + 1).split(","); // 以","作为分隔符

// 将用户信息存到线程本地变量中
vars.put("username", currentUser[0]);
vars.put("password", currentUser[1]);
```


### 3. jsr223实现: 异步任务线程组结束后, 同步交易线程组随之结束
> 背景: 某混合场景中, 有M个异步任务需要执行, 同时要求同步交易作为背景压力, 由于无法预知异步任务的结束时间, 所以需要某种机制同步
```groovy
// setup thread group
// ===============================================
import java.util.concurrent.atomic.AtomicInteger;

// user defined variables: num_of_async_threads
AtomicInteger numOfAsyncThreads = new AtomicInteger(${num_of_async_threads});
props.put("numOfAsyncThreads", numOfAsyncThreads);


// async thread teardown
// ===============================================
import java.util.concurrent.atomic.AtomicInteger;

AtomicInteger numOfAsyncThreads = props.get("numOfAsyncThreads");
numOfAsyncThreads.getAndDecrement();


// sync thread
// ===============================================
import java.util.concurrent.atomic.AtomicInteger;

AtomicInteger numOfAsyncThreads = props.get("numOfAsyncThreads");
if (numOfAsyncThreads.get() == 0) {
    ctx.getThread.stop();
}
```


### 4. 