Title: Apache开启8080端口 
Date: 2015-12-31 11:10:40
Category: Apache

环境: 阿里云Centos+Apache+wordpress

### 1.Apache启用8080端口 ###

**添加8080监听**
```
# vim /usr/local/apache2/conf/httpd.confconf
```
在`Listen 80`后加入`Listen 8080`
```
...
Listen 80

# add here
Listen 8080
```

**配置服务器**
```
# vim /usr/local/apache2/conf/extra/httpd-vhosts.conf 
```
添加网站:
```
...
<VirtualHost *:8080>
    # ServerAdmin webmaster@dummy-host2.example.com
    DocumentRoot "/var/web2"
    ServerName example.com
    ErrorLog "logs/example.com-error_log"
    CustomLog "logs/example.com-access_log" common
</VirtualHost>

```

###2. 重启Apache###
```
# service httpd restart
```

###3. 检查8080端口###
```
# netstat -an | grep 8080
tcp        0      0 0.0.0.0:8080                0.0.0.0:*                   LISTEN
```

