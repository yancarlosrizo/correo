import requests
from bs4 import BeautifulSoup
from status_client import status

def files(username, password, host) :
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
				tovar = "**"+status(username,password,host) + "**" + '\n'
				while current != total:
					current = int(current) + 1
					if current == 0:
						tovar += str(resultvar[current]).replace('<a',' '+str(current)+' <a').replace('\n','').replace('</a>','</a>\n\n').replace("%20"," ").replace("%5B","[").replace("%5D", "]").replace("%C3%BA","ú").replace("%E2%80%93","-")
					else:
						tovar += str(resultvar[current]).replace('<a',''+str(current)+' <a').replace('\n','').replace('</a>','</a>\n\n').replace("%20"," ").replace("%5B","[").replace("%5D", "]").replace("%C3%BA","ú").replace("%E2%80%93","-")
				tovar += "\n \n **Para eliminar un archivo envie** `rm:#` o `rm:all` **para eliminar todo**"
				return tovar.replace('1,95 GB', '1,95 GB \n')