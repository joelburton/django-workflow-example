Django Workflow
===============

An experiment to use PostgreSQL schemas to enforce Django workflow.

It creates views for the data and search tables in a public-user schema that obscure the real
table, so when Django goes to select/insert/update/delete on these, it is actually using the
views that filter down to published items.

This has the nice advantage that Django doesn't need to know what's going on -- the public server
will only ever see or be able to act on published items, while the admin server can see/edit
everything.

Searching: includes django.watson for searching only published item; the admin server searches
over everything.

Caching: the public server has aggressive 10 minute caching on everything; the admin server does
not cache anything.

This requires: Django 1.7, django-watson, and PostgreSQL 9.4 (since we used the JSONB type).

To use, create our two users and our database::

  $ createuser workflowpublic
  $ createuser workflowadmin
  $ createdb workflow

Then, you will run the admin server::

  $ python manage.py runserver

And the public server::

  $ DJANGO_SETTINGS_MODULE=workflow.settings.public python manage.py runserver 8001
