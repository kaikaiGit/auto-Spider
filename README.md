# auto-Spider

## 使用步骤
### 1. 安装selenium、openpyxl库
```
pip install selenium openpyxl
```

### 2. 查看chrome、edge或其他浏览器版本（自动化脚本运行的环境）
此处以Chrome为例：  
打开浏览器设置 -> 关于chrome -> 看到版本号：126.0.6478.127，  
因此需要下载一个与版本号 126.0.6478.127 接近的浏览器驱动driver，用于控制浏览器。

### 3. 下载对应版本和内核的浏览器驱动
下载链接： https://googlechromelabs.github.io/chrome-for-testing/#stable

### 4. 使用chromedriver驱动
将下载的压缩包中的chromedriver.exe文件存放到python解释器的目录文件夹下

### 5. 在python编辑器中使用selenium模块
本脚本用于爬取 https://www.diandian.com/ 某些appID的 标题、副标题、评分、评分数、排名。  
使用步骤：  
1. 在dataParse文件中修改appIDList的值（该列表为所需爬取的appID）
2. 运行程序mySpider
3. 在12秒内扫码完成登录操作
4. 程序自动爬取内容（期间可切换其他程序窗口做其他的事情）


## selenium教程： 

新版本： https://blog.csdn.net/kobepaul123/article/details/128796839?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172128378816800188598793%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=172128378816800188598793&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-128796839-null-null.142^v100^pc_search_result_base4&utm_term=selenium&spm=1018.2226.3001.

旧版本： https://blog.csdn.net/qq_43965708/article/details/120658713?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172128378816800188598793%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=172128378816800188598793&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-120658713-null-null.142^v100^pc_search_result_base4&utm_term=selenium&spm=1018.2226.3001.4187

