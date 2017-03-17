# 推送p12转换pem脚本

## 功能
将推送的p12文件转换为pem文件，提供给服务器使用。

## 使用前准备工作

推送证书公钥，如：push_public.p12
推送证书私钥，如：push_private.p12

并放到当前文件夹下

## 注意事项
里面有两个方法，分别是带密码的pem和不带密码的pem，默认是执行不带密码的pem的方法。


#### 中间需要输入文件密码,无密码直接回车

```
Enter Import Password:
MAC verified OK
```

#### 中间有个移除私有密码的方法

随便写一个4位以上的密码即可，下一步移除再重新输入一遍。

如果是带密码的方法，没有移除密码命令

```
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:

移除密码pem命令：
openssl rsa -in push_private.pem -out push_private.pem
Enter pass phrase for push_private.pem:
```

## 使用方式

> cd xxx
> python pushCreatePem.py

#### 手动修改文件名到脚本

修改py脚本：

```
PushCerPublicP12Name = "push_public" # 推送证书公钥p12文件名
PushCerPrivateP12Name = "push_private" # 推送证书私钥p12文件名
PushCerPemResultName = "push_pem" # 推送证书最终pem文件名
```

> 需要输入证书p12文件名（Y/N）:N 

#### 命令输入文件名

> 需要输入证书p12文件名（Y/N）:Y
> 请输入推送证书公钥p12文件名:xxx
> 请输入推送证书私钥p12文件名:xxx
> 请输入最终pem文件名:xxx


