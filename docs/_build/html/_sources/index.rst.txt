.. MyProject documentation master file, created by
   sphinx-quickstart on Wed Dec 27 14:22:28 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MyProject's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


* Setup your virtual environment:

::

	virtualenv venv
	source venv/Scripts/activate
	pip install django


* After setting up environment:

::

	django-admin startproject --template=https://github.com/russell310/myproject/archive/master.zip project_name
	cd project_name


* Add .env with the following:

::

	SECRET_KEY=
	DEBUG=True
	ALLOWED_HOSTS=.localhost,127.0.0.1
	DATABASE_URL=sqlite:///db.sqlite3
	EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
	EMAIL_HOST=
	EMAIL_HOST_USER=
	EMAIL_HOST_PASSWORD=
	SOCIAL_AUTH_FACEBOOK_KEY=
	SOCIAL_AUTH_FACEBOOK_SECRET=
	SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
	SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=


* Finally:

::

	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver

