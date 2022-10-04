import requests
from bs4 import BeautifulSoup
from pyrogram import Client,filters
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)

def deleted(username,password,host,id):
	zimbra = requests.session()
	k = zimbra.get(host, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"},allow_redirects=True,stream=True)
	if "503" in str(k):
		return "Servidor caído";
	elif "404" in str(k):
		return "Servidor no encontrado";
	elif "403" in str(k):
		return "Acceso denegado"
	else:
		soup = BeautifulSoup(k.text, "html.parser")
		token = soup.find("input", attrs={"name": "login_csrf"})["value"]
		params = {'loginOp':'login','login_csrf':token,'username':username, 'password':password,'zrememberme':'1','client':'standard'}
		s = zimbra.post(host, params,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"},allow_redirects=True,stream=True)
		cook = s.cookies.get_dict()
		url = zimbra.get("https://correo.uclv.edu.cu/h/search?st=briefcase")
		soup = BeautifulSoup(url.text, "html.parser")	
		getID = str(soup.find("input", attrs={"id": "C"+str(id),"type":"checkbox"})["value"])
		crumb = str(soup.find("input", attrs={"name":"crumb"})["value"])
		url = str(soup.find("form", attrs={"name":"zform"})["action"])
		data={"actionDelete":"Eliminar","id":getID,"doBriefcaseAction":1,"view":"","selectedRow":0,"crumb":crumb}
		post = zimbra.post(host+url,data=data,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"},allow_redirects=True,stream=True)
		if getID in post.text:
			return "No se pudo borrar"
		else:
			return "Borrado con exito!!"
def deletedall(username, password, host):
	zimbra = requests.session()
	k = zimbra.get(host)
	soup = BeautifulSoup(k.text, "html.parser")
	token = soup.find("input", attrs={"name": "login_csrf"})["value"]
	params = {'loginOp':'login','login_csrf':token,'username':username, 'password':password,'zrememberme':'1','client':'standard'}
	s = zimbra.post(host, params)
	cook = s.cookies.get_dict()
	s = zimbra.get(host)
	if "404" in str(s):
		return "Página no encontrada"
	else:
		if "403" in str(s):
			return "Sin permiso de acceso, use un proxy"
		else:
			if "login_csrf" in s.text:
				return "Usuario incorrecto"
			else :
				k = zimbra.get(host+'/h/search;jsessionid=node019vkd4gg512591izv0d8gywbj77552.node0?st=briefcase')
				soup = BeautifulSoup(k.text, "html.parser")
				entradas = soup.find_all('a',{'onclick':'return false;'})
				resultvar = '\n' + str(entradas).replace("[","").replace("]","").replace(",","\n ").replace('                                            ' , '').replace('onclick="return false;"','').replace('" >','">').replace('"  >','">').replace('/home',host+'/home')
				resultvar = resultvar.split('\n ')
				total = int(len(resultvar)) - 1
				current = -1
				while current != total:
					current = current + 1
					
					deleted(username, password, host, 0)