Title: Front End Questions
Date: 2016-06-06 21:16:16
Category: Note

* 行内元素有哪些？块级元素有哪些？空(void)元素有哪些？

    1. 行内元素有：a b span img input select strong
    2. 块级元素有：div ul ol li dl dt dd h1 h2 h3...p
    3. 常见空元素；br hr img input link meta

* 浏览器内多个标签页之间通信方式
    WebSocket, ShareWorker, 也可以调用localstorage，cookies等本地存储方式；

* this对象
    * this总是指向函数的直接调用者
    * 如果有new关键字，this指向new生成的那个对象
    * 在事件中，this指向触发这个事件的对象
