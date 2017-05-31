# mySweetCompany
Site de e-commerce réalisé en Django

Dans un onlgte :
$ docker-compose up --build

Dans un autre onglet :
$ docker-compose exec web bash
$ python manage.py loaddata dump.json
$ python manage.py makemigrations

Puis relancer serveur.
