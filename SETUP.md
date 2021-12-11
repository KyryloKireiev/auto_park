# auto-park rest api

Clone project from https://github.com/KyryloKireiev/auto_park

For use auto-park rest api you need install Python 3.9 or higher.

Install all requirements:
+ use command: "pip install -r requirements.txt" in the root directory of the project

For start server:
+ use command: "python manage.py runserver"
+ server start on the local host: "http://127.0.0.1:8000/"

You can see all endpoints of project in README.md in the root directory of the project

You can use api with admin panel:
+ go to "http://127.0.0.1:8000/admin" 
+ name: "admin"
+ password: "password"
+ you can create new super user in admin panel 
  or with command "python manage.py createsuperuser".