Ce dossier contient un client TCP et un serveur TCP en python conformément à l'exercice "TP Réseau n°2".
cf. sujet pdf "tp_réseau_2.pdf", 
proposé par Mr Jacoboni L3 Miashs, Université Jean Jaurès Toulouse.


note: Le client devra être lancé avec python 2.7 et le serveur devra être lancés avec python3.7 pour être sûr de leur bon fonctionnement. J'ai obligé le client à utiliser "GET" en uperCase sinon le serveur ne comprendra pas la requete.

Le client est à "usage unique". Vous devrez le relancer à chaque requetes. Une boucle While(true) aurait pu être faite (comme dans les tp précedent mais j'ai préféré rendre un client qui n'accompli qu'une requete). 

Seule la version avec le module "socket" est présent. En effet socketserveur n'est qu'une version allégé de socket nous dispensant de code. Quant à la version Java n'étant la que pour appuyer le propo de Mr Jacoboni concernant la lourdeur de ce langage, j'ai décidé de passer au tp suivant.

Les fichiers tt tt.txt et error.txt ne sont la que pour tester les requetes GET.
