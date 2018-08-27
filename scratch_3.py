ZZfrom threading import Thread
from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(("",4444))

s.listen(5)

s1,info = s.accept()
print("已接入")

print(s1.recv(1024).decode("gb2312"))
s1.send("哈哈".encode("gb2312"))

s1.close()
s.close()