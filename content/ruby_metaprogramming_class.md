Title: Meta programming(Class)
Date: 2014-05-03 17:51:04
Category: Ruby

在Ruby中，使用class定义类时，实际上是在运行代码，这与java之类的静态语
言有很大的差别。    
另外，类只是一个增强的模块，因此，任何适用于类的东西也
适用于模块。
<br>
![Object Definitions](/images/ObjectDefinitions.png)
<br>
 * 注1:在类(或模块)定义时，类本身充当了当前对象self的角色。
 
``` ruby
result = class MyClass
  self
end

result     # =>  MyClass
```

 * 注2:Ruby中总是存在一个当前对象self，与此类似，也总是存在一个当前类
   （或模块）。每当通过class关键字来打开一个类时，这个类就成为当前类，
   但是使用class关键字需要一个类的名字。
   如果只有一个类的引用，需要用class_eval()方法打开这个类。
   
 * 注3：类实例变量仅仅是属于Class类对象的普通实例变量。它仅仅可以被类
   本身所访问，而不能被类的实例或之类所访问。
   
 * 注4：类方法的实质，它们只是一个类的单件方法。
 
 * 注5: 在类定义中使用一个类方法。
 
 * 注6: eigenclass是一个对象特有的隐藏类，它是单件方法存在的地方。Ruby中可以使用如下语法进入eigenclass的作用域。
 
``` ruby
class << an_object 
  # do something
end
```

 * 注7: 如果对象是eigenclass，那么Ruby不是从它所在的类开始，而是从这个
   eigenclass类中开始查找方法，如图。
   <br>
   ![Eigenclass](/images/eigenclassMethod.png)
   
 * 注8: 一个对象的eigenclass的超类是这个对象的类，一个类的eigenclass的
   超类是这个类的超类的eigenclass,如图。
   ![eigenclassInherit](/images/eigenclassInherit.png)
   
 * 注9: 通过向类的eigenclass中混入模块来定义类方法。
 
 * 注10: 通过给一个对象的eigenclass混入模块来定义单件方法。

* 注11: 1. 给方法定义一个别名；2.重新定义这个方法；3.在新的方法中调用老的方法。

* 注12: 1.环绕别名是一种猴子补丁，可能会破坏已有代码。2.你永远不该把一个环绕别名加载两次。
