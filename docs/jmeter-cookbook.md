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


### 4. jsr223实现: 各线程组执行次数配比
```groovy
// setup thread group
// ===============================================
int[] ratios_real = [0, 0, 0];
props.put("ratios_real", ratios_real.join(","));


// task alloc jsr223 sampler
// ===============================================
import java.util.Arrays;


int[] ratios_ideal = [2, 3, 4];
int ratios_ideal_total = Arrays.stream(ratios_ideal).sum();

// 核心算法
// 通过当前比例和目标比例做差, 找到差值最小的那一个, 下一个任务就分配给它
synchronized(props) {
	// int[] ratios_real = Arrays.stream(props.get("ratios_real").split(",")).map(x -> Integer.parseInt(x)).toArray(); // 如果jmeter版本不支持->写法, 可以使用闭包collect{}
    int[] ratios_real = Arrays.stream(props.get("ratios_real").split(",")).collect{Integer.parseInt(it)};
	int ratios_real_total = Arrays.stream(ratios_real).sum();

	int index;
	if (ratios_real_total == 0) {
		ratios_real[0]++;
		index = 0;
	} else {
		float minimum = 1;
		float diff;
		for (int i = 0; i < ratios_ideal.length; i++) {
			diff = (float)ratios_real[i] / ratios_real_total - (float)ratios_ideal[i] / ratios_ideal_total;
			if (diff < minimum) {
				minimum = diff;
				index = i;
			}
		}
	}
	ratios_real[index]++;
	vars.put("task_index", "${index}")
	
	String ratios_real_str = ratios_real.join(",");
	props.put("ratios_real", ratios_real_str);
	log.info("==================== ratios_real=${ratios_real_str}")
}


// if-controller
// ===============================================
// 通过if-controller判断task_index决定执行哪个任务
${__jexl3("${task_index}" == "0")}
${__jexl3("${task_index}" == "2")}
...
```