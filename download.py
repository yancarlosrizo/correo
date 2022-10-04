import urllib3
import requests
from os.path import exists
import os

def download(url):
	if not exists("downloads/"):
		os.mkdir("downloads")
	http = urllib3.PoolManager()
	name = str(requests.get(url).headers["Content-Disposition"]).replace('attachment; ','')
	name = name.replace('filename=','').replace('"','').replace("inline;","").replace("[","").replace("]","")
	ul = http.request('GET', url)
	save = open("downloads/"+name, "wb")
	save.write(ul.data)
	save.close()
	return name