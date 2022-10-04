from pyrogram import Client,filters
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
import asyncio
import os
from os.path import exists
from files_client import files
from deleted_client import deleted, deletedall
from upload_client import upload
from download import download
import urllib.parse
         
app = Client('name',api_id=12165603,api_hash='a217938354240f45f2a509b043723ac4',bot_token='5771350123:AAFualjqc1r3v8VVMlRiLJdrXbPLpqJYSRI')
@app.on_message(filters.private & filters.text)
async def home(client, message):
	text = message.text
	user_id = message.from_user.id
	user_name = message.chat.username
	msg_id = message.id
	if user_id in [ 1630373589]:
		if '/start' in text:
			await app.delete_messages(user_id,msg_id)
			if not exists(str(user_id)):
				os.mkdir(str(user_id))
			if not exists(str(user_id)+"/username"):
				start = "**UCLV New** \nSet your account first"
			else:
				if not exists(str(user_id)+"/proxy"):
					username = open(str(user_id)+"/username","r")
					password = open(str(user_id)+"/password","r")
					start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()
				else:
					username = open(str(user_id)+"/username","r")
					password = open(str(user_id)+"/password","r")
					start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()+"\n Proxy: ON"
			await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ACCOUNT",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("FILES",callback_data="files:"+str(user_id)+":"+str(msg_id))]#,[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
		elif 'http://' in text or 'https://' in text:
			await app.send_message(user_id, "Downloading")
			filename = download(text)
			await app.delete_messages(user_id, msg_id + 1)
			await app.send_message(user_id,"Uploading "+ filename)
			username = open(str(user_id)+"/username","r")
			password = open(str(user_id)+"/password","r")
			proxy = None
			
			if exists(str(user_id)+"/proxy"):
				proxy = open(str(user_id)+"/proxy","r")
				#si proxy
				uploadin = upload(username.read(), password.read(), "https://correo.uclv.edu.cu", filename,proxy=proxy.read())
			else:
				#no proxy
				uploadin = upload(username.read(), password.read(), "https://correo.uclv.edu.cu", filename,proxy="")
			if "ERROR" in uploadin:
				await app.delete_messages(user_id, int(msg_id) + 1)
				await app.send_message(user_id,uploadin)
			else:
				txt = open(filename.split(".")[0]+".txt", "w")
				txt.write(uploadin.replace(" ","%20"))
				txt.close()
				await app.delete_messages(user_id, int(msg_id) + 2)
				await app.send_message(user_id,filename, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("DOWNLOAD",url=uploadin.replace(" ","%20"))]]))
				await app.send_document(user_id, filename.split(".")[0]+".txt")
		elif '/menu' in text:
			await app.delete_messages(user_id,msg_id)
			if not exists(str(user_id)):
				os.mkdir(str(user_id))
			if not exists(str(user_id)+"/username"):
				start = "**UCLV New** \nSet your account first"
			else:
				if not exists(str(user_id)+"/proxy"):
					username = open(str(user_id)+"/username","r")
					password = open(str(user_id)+"/password","r")
					start = "**UCLV New** \nUser: "+username.read()+" \nPass: "+password.read()
				else:
					username = open(str(user_id)+"/username","r")
					password = open(str(user_id)+"/password","r")
					start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()+"\n Proxy: ON"
			await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ACCOUNT",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("FILES",callback_data="files:"+str(user_id)+":"+str(msg_id))]#,[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
		elif "socks5://" in text:
        			log = open(str(user_id)+"log","r")
        			logr = log.read()
        			proxy = open(str(user_id)+"/proxy", "w")
        			proxy.write(text)
        			if "socks5://none" in text:
        				os.remove(str(user_id)+"/proxy")
        			else:
        				print(1)
        			if not exists(str(user_id)+"/username"):
        				start = "**UCLV New** \nSet your account first"
        			else:
        				if not exists(str(user_id)+"/proxy"):
        					username = open(str(user_id)+"/username","r")
        					password = open(str(user_id)+"/password","r")
        					start = "**UCLV New** \n User: "+username.read()+" \n Password: "+password.read()
        				else:
        					username = open(str(user_id)+"/username","r")
        					password = open(str(user_id)+"/password","r")
        					start = "**UCLV New** \n User: "+username.read()+" \n Password: "+password.read()+"\n Proxy: ON"
        			await app.delete_messages(user_id, int(msg_id) - 1)
        			await app.delete_messages(user_id, msg_id)
        			await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ACCOUNT",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("FILES",callback_data="files:"+str(user_id)+":"+str(msg_id))]#,[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
		elif ":" in text:
		      	log = open(str(user_id)+"log","r")
		      	logr = log.read()
		      	if "files" in logr:
		      		data = text.split(":")
		      		if data[0] == "rm":
		      			username = open(str(user_id)+"/username", "r")
		      			password = open(str(user_id)+"/password", "r")
		      			if data[1] == "all":
		      				await app.delete_messages(user_id, msg_id - 1)
		      				await app.send_message(user_id, "This may take a while")
		      				deletedall(username.read(), password.read(), "https://correo.uclv.edu.cu")
		      			else:
		      				await app.delete_messages(user_id, msg_id - 1)
		      				await app.send_message(user_id, "This may take a while")
		      				await app.delete_messages(user_id, msg_id)
		      				deleted(username.read(),password.read(), "https://correo.uclv.edu.cu", data[1])
		      			if not exists(str(user_id)+"/username"):
		      				start = "**UCLV New** \nSet your account first"
		      			else:
		      					if not exists(str(user_id)+"/proxy"):
		      						username = open(str(user_id)+"/username","r")
		      						password = open(str(user_id)+"/password","r")
		      						start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()
		      					else:
		      						username = open(str(user_id)+"/username","r")
		      						password = open(str(user_id)+"/password","r")
		      						start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()+"\n Proxy: ON"
		      			await app.delete_messages(user_id, int(msg_id) - 1)
		      			await app.delete_messages(user_id, msg_id)
		      			await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ACCOUNT",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("FILES",callback_data="files:"+str(user_id)+":"+str(msg_id))]#,[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
		      	if "account" in logr:
		      		username = open(str(user_id)+"/username", "w")
		      		password = open(str(user_id)+"/password", "w")
		      		data = text.split(":")
		      		username.write(data[0])
		      		password.write(data[1])
		      		log = open(str(data[1])+"log","w")
		      		log.write("")
		      		if not exists(str(user_id)+"/username"):
		      			start = "**UCLV New** \nSet your account first"
		      		else:
		      			if not exists(str(user_id)+"/proxy"):
		      				username = open(str(user_id)+"/username","r")
		      				password = open(str(user_id)+"/password","r")
		      				start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()
		      			else:
		      				username = open(str(user_id)+"/username","r")
		      				password = open(str(user_id)+"/password","r")
		      				start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()+"\n Proxy: ON"
		      		await app.delete_messages(user_id, msg_id)
		      		await app.delete_messages(user_id, int(msg_id) - 1)
		      		await app.send_message(user_id, start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ACCOUNT",callback_data="account:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("FILES",callback_data="files:"+str(user_id)+":"+str(msg_id))]#,[InlineKeyboardButton("AYUDA",callback_data="help:"+str(user_id)+":"+str(msg_id))],[InlineKeyboardButton("Studio Kanami", url="https://t.me/studiokanami")]
        ]))
	else:
		await app.send_message(user_id, 'Access dennied')
@app.on_callback_query()
async def answer(client, callback_query):
	data = callback_query.data
	if 'help' in data:
		data = data.split(":")
		await app.delete_messages(data[1], int(data[2]) + 1)
		await app.send_message(data[1],"__Desarrollo de **Kanami Studios**__ \n\n **¿Usted tiene un correo de la uclv?** \n __Parecido a__ `kanami@uclv.cu` __, bueno..., si lo tiene felicidades con este bot puede hacer de ese correo su nube personal de descargas gratis en Cuba. \n Envíe un enlace para empezar la descarga de este en el bot para ser subido a su correo, el tamaño de las partes de los zips es automaticamente 48 MB.__ \n\n__El usuario y contraseña se editan en **CAMBIAR USUARIO** del menú, el formato del usuario es kanami@uclv.cu y el de la contraseña @Kanami0__\n\n__En **VER ARCHIVOS** usted puede ver y eliminar sus archivos en el correo para conservar el almacenamiento que debería ser de 1.95 GB__\n\n **__Para subir archivos use las hora de 11:00 pm : 11:00 am__**\n\n **Es hora de descargar gratis!!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCELAR",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]))
	if 'account' in data:
		data = data.split(":")
		log = open(str(data[1])+"log","w")
		log.write("account")
		await app.delete_messages(data[1], int(data[2]) + 1)
		await app.send_message(data[1],"**TURN ON:** \n `username:password`", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCEL",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]))
	if 'proxy' in data:
		data = data.split(":")
		log = open(str(data[1])+"log","w")
		log.write("proxy")
		await app.delete_messages(data[1], int(data[2]) + 1)
		await app.send_message(data[1],"**TURN ON:** \n `socks5://100.100.10.1:1000` \n **TURN OFF:** \n `socks5://none`", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCEL",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]))
	if 'files' in data:
		data = data.split(":")
		log = open(str(data[1])+"log","w")
		log.write("files")
		if exists(data[1]+"/username"):
			username = open(str(data[1])+"/username","r")
			password = open(str(data[1])+"/password","r")
			filesk = files(username.read(),password.read(),"https://correo.uclv.edu.cu")
			if '<a' not in filesk:
				await app.delete_messages(data[1], int(data[2]) + 1)
				await app.send_message(data[1],"Nothing to see here", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCEL",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]),disable_web_page_preview=True)
			else:
				await app.delete_messages(data[1],int(data[2]) + 1)
				await app.send_message(data[1], filesk, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCEL",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]),disable_web_page_preview=True)
		else:
			await app.delete_messages(data[1], int(data[2]) + 1)
			await app.send_message(data[1], "Set your account first", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCEL",callback_data="cancel:"+str(data[1])+":"+str(data[2]))]]))
	if 'cancel' in data:
		data = data.split(":")
		log = open("log", "w")
		log.write("")
		log.close()
		if not exists(str(data[1])+"/username"):
				start = "**UCLV New** \nSet your account first"
		else:
				if not exists(str(data[1])+"/proxy"):
					username = open(str(data[1])+"/username","r")
					password = open(str(data[1])+"/password","r")
					start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()
				else:
					username = open(str(data[1])+"/username","r")
					password = open(str(data[1])+"/password","r")
					start = "**UCLV New** \nUser: "+username.read()+" \nPassword: "+password.read()+"\nProxy: ON"
		await app.delete_messages(data[1],int(data[2]) + 2)
		await app.send_message(data[1] ,start, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ACCOUNT",callback_data="account:"+str(data[1])+":"+str(int(data[2])))],[InlineKeyboardButton("PROXY",callback_data="proxy:"+str(data[1])+":"+str(int(data[2])))],[InlineKeyboardButton("FILES",callback_data="files:"+str(data[1])+":"+str(int(data[2])))]#,[InlineKeyboardButton("HELP",callback_data="help:"+str(data[1])+":"+str(int(data[2])))]
        ]))
 
print("Iniciado")
app.run()
