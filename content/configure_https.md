Title: Configure Https
Date: 2015-10-10 16:35:59
Category: Https

Https just means "http with ssl". In order to enable SSL, we need a
certificate which is either self-signed or signed by an external
Cerificate Authority. A self-signed certificate need to be imported
when browsing. For easy-to-use purposes, use an external cerificate
here. [http://www.startssl.com/](http://www.startssl.com/) and
[https://buy.wosign.com/](https://buy.wosign.com/) are two sites for
buying cerificate. I use
[https://buy.wosign.com/](https://buy.wosign.com/) here.

For e-commerce websites, use OV(Organization Verified) SSL. For
financial websites, use EV(Extended Verified) SSL.

##### Enable in Nginx #####

```
server {
    listen 443 ssl;

    server_name example.com;    
    ssl_certificate /etc/ssl/private/example.com_bundle.crt;
    ssl_certificate_key /etc/ssl/private/example.com.key;

    ...
}
```

