import requests
from bs4 import BeautifulSoup

def status(username, password, host) :
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
				k = zimbra.get(host+'/m/zmain')
				soup = BeautifulSoup(k.text, "html.parser")
				entradas = soup.find_all('span',{'class':'quota-span'})
				return str(entradas).replace('[<span class="quota-span">','').replace("</span>]","").replace("                                              de ","/").replace("Espacio de almacenamiento: ","").replace(" de ","/")				
#TTTTTTEEEEEECCCCCH          H
#     TT     E            C           H         H
#     TT     EEEE     C           HHHHH
#     TT     E            C           H         H
#     TT     EEEEEECCCCCH         H