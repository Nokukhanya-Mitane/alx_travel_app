# alx_travel_app

mkdir alx_travel_app && cd alx_travel_app
python3 -m venv venv
source venv/bin/activate


pip install django djangorestframework django-cors-headers drf-yasg django-environ mysqlclient celery


django-admin startproject alx_travel_app .
python manage.py startapp listings
