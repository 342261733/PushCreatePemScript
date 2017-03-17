#coding: utf-8
import os
import sys

PushCerPublicP12Name = "push_public" # 推送证书公钥p12文件名
PushCerPrivateP12Name = "push_private" # 推送证书私钥p12文件名
PushCerPemResultName = "push_pem" # 推送证书最终pem文件名

def inputCerName():
    is_need_input = raw_input("需要输入证书p12文件名（Y/N）:")
    if is_need_input == "N":
        return
    
    global PushCerPublicP12Name
    global PushCerPrivateP12Name
    global PushCerPemResultName
    
    PushCerPublicP12Name = raw_input("请输入推送证书公钥p12文件名:")
    print(PushCerPublicP12Name)
    PushCerPrivateP12Name = raw_input("请输入推送证书私钥p12文件名:")
    PushCerPemResultName = raw_input("请输入最终pem文件名:")

def checkFailure(ret):
    if ret != 0:
        print("\n\n*******\n 生成pem【%s.pem】失败, 请检查p12文件名是否正确 \n ********" % (PushCerPemResultName));
        os._exit(0)

# 推送证书p12->pem,带密码
def changePushCerP12ToPemWithPassword():
    
    inputCerName()
    
    change_public_string = "openssl pkcs12 -clcerts -nokeys -out %s.pem -in %s.p12" % (PushCerPublicP12Name, PushCerPublicP12Name)
    print("\n推送证书公钥转换pem命令：\n%s" %(change_public_string));
    ret = os.system(change_public_string)
    checkFailure(ret)
    
    change_private_string = "openssl pkcs12 -nocerts -out %s.pem -in %s.p12" % (PushCerPrivateP12Name, PushCerPrivateP12Name)
    print("\n推送证书私有转换pem命令：\n%s" %(change_public_string));
    ret = os.system(change_private_string)
    checkFailure(ret)
    
    cat_private_public_string = "cat %s.pem %s.pem > %s.pem" % (PushCerPublicP12Name, PushCerPrivateP12Name, PushCerPemResultName)
    print("\n合并pem命令：\n%s" % (cat_private_public_string));
    ret = os.system(cat_private_public_string)
    checkFailure(ret)
    
    print("\n\n*******\n 生成pem【%s.pem】成功 \n ********" % (PushCerPemResultName));

# 推送证书p12->pem,不带密码
def changePushCerP12ToPemWithoutPassword():
    
    inputCerName()

    change_public_string = "openssl pkcs12 -clcerts -nokeys -out %s.pem -in %s.p12" % (PushCerPublicP12Name, PushCerPublicP12Name)
    print("\n推送证书公钥转换pem命令：\n%s" %(change_public_string));
    ret = os.system(change_public_string)
    checkFailure(ret)

    change_private_string = "openssl pkcs12 -nocerts -out %s.pem -in %s.p12" % (PushCerPrivateP12Name, PushCerPrivateP12Name)
    print("\n推送证书私有转换pem命令：\n%s" %(change_public_string));
    ret = os.system(change_private_string)
    checkFailure(ret)
    
    remove_password_string = "openssl rsa -in %s.pem -out %s.pem" % (PushCerPrivateP12Name, PushCerPrivateP12Name)
    print("\n移除密码pem命令：\n%s" % (remove_password_string));
    ret = os.system(remove_password_string)
    checkFailure(ret)
    
    cat_private_public_string = "cat %s.pem %s.pem > %s.pem" % (PushCerPublicP12Name, PushCerPrivateP12Name, PushCerPemResultName)
    print("\n合并pem命令：\n%s" % (cat_private_public_string));
    ret = os.system(cat_private_public_string)
    checkFailure(ret)
    
    print("\n\n*******\n 生成pem【%s.pem】成功 \n ********" % (PushCerPemResultName));

if __name__ == '__main__':
    
    changePushCerP12ToPemWithoutPassword()



