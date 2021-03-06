Title: Metaprogramming(Methods)
Date: 2014-05-03 16:44:19 
Category: Ruby

Ruby是动态语言，没有静态类型检查，同时也提供了很多java等静态语言无法提
供的编程技巧。本章主要专注于消除重复代码的技巧，通过用两种不同的方式对一
段代码的重构来展示Ruby的强大功能，涉及的知识点比较少。
<br>
![methods](/images/methods.png)
<br>
* 注1: method_missing()是Kernel中的一个实例方法，当Ruby找不到调用的方
  法时，它最后就会调用这个名为method_missing()的方法。

* 注2: 移除一个对象中的所有方法，以便把它们转换成幽灵方法。

---

**重构例子**

``` ruby
# 原始代码
class Computer
  def initialize(computer_id, data_source)
    @id = computer_id
    @data_source = data_source
  end
  def mouse
    info = @data_source.get_mouse_info(@id)
    price = @data_source.get_mouse_price(@id)
    result = "Mouse: #{info} ($#{price})"
    return "* #{result}" if price >= 100
    result
  end
  def cpu
    info = @data_source.get_cpu_info(@id)
    price = @data_source.get_cpu_price(@id)
    result = "Cpu: #{info} ($#{price})"
    return "* #{result}" if price >= 100
    result
  end
  def keyboard
    info = @data_source.get_keyboard_info(@id)
    price = @data_source.get_keyboard_price(@id)
    result = "Keyboard: #{info} ($#{price})"
    return "* #{result}" if price >= 100
    result
  end
  # ...
end
```

``` ruby
# 使用动态方法重构
class Computer
  def initialize(computer_id, data_source)
    @id = computer_id
    @data_source = data_source
    # 使用内省方式提取所有组件的名字
    data_source.methods.grep(/^get_(.*)_info$/) { Computer.define_component $1 }
  end

  def self.define_component(name)
    # 使用define_method()动态定义方法
    define_method(name) do
      # 使用send()方法集中处理
      info = @data_source.send "get_#{name}_info", @id
      price = @data_source.send "get_#{name}_price", @id
      result = "#{name.capitalize}: #{info} ($#{price})"
      return "* #{result}" if price >= 100
      result
    end
  end
  
  define_component :mouse
  define_component :cpu
  define_component :keyboard
end
```

``` ruby
# 使用幽灵方法重构
class Computer
  # 创建白板， 以免方法命名冲突
  instance_methods.each do |m|
    undef_method m unless m.to_s =~ /^__|method_missing|respond_to?/
  end

  def initialize(computer_id, data_source)
    @id = computer_id
    @data_source = data_source
  end

  # 在method_missing()中创建方法
  def method_missing(name, *args)
    super if !respond_to?(name)
    info = @data_source.send("get_#{name}_info", @id)
    price = @data_source.send("get_#{name}_price", @id)
    result = "#{name.to_s.capitalize}: #{info} ($#{price})"
    return "* #{result}" if price >= 100
    result
  end

  # 覆写respond_to?()，保证查询方法时返回正确结果
  def respond_to?(method)
    @data_source.respond_to?("get_#{method}_info") || super
  end
end
```
