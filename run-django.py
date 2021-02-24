import os

comands = [
    'cd /code',
    'python manage.py migrate',
    'python manage.py collectstatic --no-input',
    #'python manage.py runserver 0.0.0.0:8000',
    'gunicorn proj.wsgi:application --env DJANGO_SETTINGS_MODULE=proj.settings_production --limit-request-line 0 --timeout 600 -w 4 -b :8000'
]

for command in comands:
    os.system(command)
