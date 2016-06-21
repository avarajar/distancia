Ejemplo de Disatncias
========

Ejemplo para calcular distancia entre ciudades dadas las coordenadas.

Setup Development
========

##How to Install?

* Pre:
  - virtualenvwrapper
  - python (dev)
  - postgres

1) mkvirtualenv --no-site-packages domicilios
2) git clone git@github.com:avarajar/distance.git
3) cd distancia
4) pip install -r drequirements.txt
6) ./manage.py syncdb
7) ./manage.py migrate
8) 7) ./manage.py runserver

Deploy to heroku
========

git push heroku master
