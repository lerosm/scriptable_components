import requests
session = requests.session()
a = session.get("http://www.baidu.com")
#print("hello world")
print(a.content.decode('utf-8'))
print(a)