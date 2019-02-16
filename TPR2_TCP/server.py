from socket import *
import sys, threading, os, os.path, re
import datetime

if len(sys.argv) != 3:
    print("Usage: {} <port> <répertoire>".format(sys.argv[0]))
    sys.exit(1)
DOC_ROOT = os.path.realpath(sys.argv[2])

sock_server = socket(AF_INET, SOCK_STREAM)
sock_server.bind(("localhost", int(sys.argv[1])))
sock_server.listen(4)
print("le serveur écoute sur le port " + sys.argv[1], file=sys.stderr)
print("Son répertoire de base est " + DOC_ROOT, file=sys.stderr)

BUFFER = 1024

def traiter_client(client):
    
    """ test if contenu client it's ok"""
    requete = client.recv(1024)
    requete = requete.decode()
    req = re.compile(r"^GET(?P<nbLigne> [1-9]+)? (?P<nameFile>(?P<nom>[a-zA-Z][a-zA-Z0-9_]{0,7})(\.(?P<ext>[a-zA-Z0-9]{1,3}))?)")
    result = re.match(req, requete)
    """ send contenu file"""
    if (result is not None) :
        monFile = str(result.group("nameFile"))
        if result.group("nbLigne") is None:
            nbLigne = -1
        else:
            nbLigne = int(result.group("nbLigne"))
        contenu = getFile(monFile,nbLigne)
        client.send(contenu.encode())
    else:
        if requete == "DATE":
            now = datetime.datetime.now()
            client.send(str(now).encode())
        else:
            client.send("404 Not Found".encode())
   
    
    client.close()

def getFile(monFichier, nbLigne):
    if not os.path.isfile(monFichier):
            retour = "666 Not Found"
    else:
        if nbLigne == -1:
            with open(monFichier, 'r') as content_file:
                retour = content_file.read()
        else:
            contenuFichier = open(monFichier)
            retour = ""
            for ligne in range(0,nbLigne):
                retour += contenuFichier.readline()
            

    return retour


def requete_invalide(client):
    client.send("erreur de requete")

while True:
    try:
        client, adresseClient = sock_server.accept()
        print("Connexion de " + adresseClient[0])
        threading.Thread(target=traiter_client, args=(client,)).start()
    except KeyboardInterrupt:
        break

sock_server.shutdown(SHUT_RDWR)
print("Arrêt du serveur")
for t in threading.enumerate():
    if t != threading.main_thread(): t.join
sys.exit(0)