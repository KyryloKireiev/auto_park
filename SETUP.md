# auto-park rest api

Clone project from https://github.com/KyryloKireiev/auto_park

For use auto-park rest api you need install Python 3.9 or higher.

Install all requirements:
+ use command: "pip install -r requirements.txt" in the root directory of the project

Create a database:
+ use command: "python manage.py migrate"
+ you need to enter the commands in the directory auto_park, where manage.py is


To start server:
+ use command: "python manage.py runserver"
+ server starts on the local host: "http://127.0.0.1:8000/"

You can see all endpoints of project in README.md in the root directory of the project

You can use api with admin panel:
+ go to "http://127.0.0.1:8000/admin"
+ to use admin panel you need to create superuser  
+ you can create new super user with command "python manage.py createsuperuser"
  or in admin panel, if you already have superuser.
  
To use endpoit "POST /vehicles/set_driver/<vehicle_id>/" you need:
+ make post request with driver_id in json format
+ example: {"driver_id": 1} to set driver 1 in "/<vehicle_id>/"
+ again {"driver_id": 1} to remove driver 1 from "/<vehicle_id>/"

If you want to include Django Rest Framework forms:
+ remove from settings.py "REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}"
