# Useful and common commands

- `python manage.py runserver` (Start local server, [here](http://127.0.0.1:8000/))
- `python manage.py makemigrations` (Create DB migrations)
- `python manage.py migrate` (Migrate data to DB, needs to be run every time the models change)
- `python manage.py startapp app_name .\apps\app_name` (Create new app - app are miniature but standalone web applications)
- `python manage.py createsuperuser` (Create admin user)
- `python manage.py collectstatic` (Preparation for deployment, collection all static files, e.g. css, js...)
