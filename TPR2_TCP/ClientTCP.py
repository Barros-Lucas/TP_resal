import socket
import sys

if len(sys.argv) != 3:
	print "Usage: "+{sys.argv[0]}+" <ip> <port>"
	sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print 'Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.'

message = raw_input("Requete : ")
message = str(message)
print 'Envoi de :' + str(message)
n = client.send(message)
if (n != len(message)):
        print 'Erreur envoi.'
else:
        print 'Envoi ok.'

print 'Reception...'
donnees = client.recv(1024)
print 'Recu :', donnees

print 'Deconnexion.'
client.close()
