Code source de l'Oreille à gauche

Installation
============

Paquet Yunohost.

En une ligne de commande :

```
sudo yunohost app install https://github.com/Jojo144/oreille_a_gauche --debug -f -a "domain=DOMAINE&mastodon_access_token=XXXXXX&email=ADMINEMAIL"
```

--debug : pour avoir la trace

-f, --force           Do not ask confirmation if the app is not safe to use
                        (low quality, experimental or 3rd party)

-a : arguements Domaine, Email de l'admin et jeton d'accès mastodon


Jeton d'accès (access token)
------------------------------------

*NB: le **jeton d'accès** se génère en créant une application dans le profil du compte mastodon, section « développement » puis en le copiant-collant depuis le champ éponyme*.


Upgrade
---------

La mise à jour n'est pas supportée, désinstaller/réinstaller pour mettre à jour.
