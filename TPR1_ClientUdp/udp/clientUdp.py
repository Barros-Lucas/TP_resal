# -*- coding: utf-8 -*
import sys
from socket import *


if len(sys.argv) != 3:
	print(f"Usage: {sys.argv[0]} <ip> <port>", file=sys.stderr)
	sys.exit(1)

# la taille est arbitraire selon le type de réponses retournées par le serveur
TAILLE_TAMPON = 256

with socket(AF_INET, SOCK_DGRAM) as sock:
	while True:
		mess = input("Entrez une commande (help pour la liste, quit pour quitter)")
		if mess.lower() == "quit".lower():
			exit(0)
		sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))

		reponse, t = sock.recvfrom(TAILLE_TAMPON)
		print("Réponse = " + reponse.decode())




