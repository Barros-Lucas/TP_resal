# -*- coding: utf-8 -*
import sys
from socket import *
import datetime
from time import gmtime, strftime



if len(sys.argv) != 2:
	print(f"Usage: {sys.argv[0]} <port>",file=sys.stderr)
	sys.exit(1)

TAILLE_TAMPON = 256

sock = socket(AF_INET, SOCK_DGRAM)

sock.bind(('', int(sys.argv[1])))
print("Serveur en attente sur le port "+ sys.argv[1], file=sys.stderr)

def getPaques():
	now = datetime.datetime.now()
	return "paques aujourd'hui"


def retour(mess):
	now = datetime.datetime.now()
	messs = mess.lower()
	if mess.lower() == "help".lower():
		return f"Commandes possibles: date, heure, jour, mois, annee, paques, ascension"
	else:
		if mess == "date":
			return f"{now}"
		if mess == "heure":
			return f"{now.hour}"
		if mess == "jour":
			return f"{now.day}"
		if mess == "mois":
			return f"{now.month}"
		if mess == "annee":
			return f"{now.year}"
		if mess == "paques":
			return getPaques()
		if mess == "ascension":
			return "ascension aujourdhui"
	return "Requéte incorrecte : " + mess


with open("serveurDate.log", "a") as fd:
	now = strftime("%Y/%m/%d %H:%M:%S", gmtime())
	fd.write(f"{now}"+" Serveur started\n")
	



while True:
	try:
		requete = sock.recvfrom(TAILLE_TAMPON)
		(mess, adr_client) = requete
		ip_client, port_client = adr_client
		print(f"Requete provenant de {ip_client}. Longueur = {len(mess)}", file=sys.stderr)
		with open("serveurDate.log", "a") as fd:
			now = strftime("%Y/%m/%d %H:%M:%S", gmtime())
			fd.write(f"{now}"+" Received "+mess.decode() +" from "+f"{ip_client}"+":"+f"{port_client}"+"\n")
		reponse = retour(mess.decode())

		sock.sendto(reponse.encode(), adr_client)

	except KeyboardInterrupt: break

sock.close()
print("Arret du serveur", file=sys.stderr)
with open("serveurDate.log", "a") as fd:
	now = strftime("%Y/%m/%d %H:%M:%S", gmtime())
	fd.write(f"{now}"+" Serveur stopped...\n")
sys.exit(0)
