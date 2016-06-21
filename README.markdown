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

* Steps:


  - mkvirtualenv --no-site-packages distancia
  - git clone git@github.com:avarajar/distancia.git
  - cd distancia
  - pip install -r drequirements.txt
  - ./manage.py syncdb
  - ./manage.py migrate
  - ./manage.py runserver

Deploy to heroku
========

git push heroku master
