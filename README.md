# auto-park rest api

Autopark REST API allows you to create and edit a car and driver models. 
All data is transmitted in json format. The app is written in Python using 
Django and Django Rest Framework.

## Features

| Feature                      | Supported                |
|:-----------------------------|:-------------------------|
| CRUD for Driver model        | :white_check_mark:       |
| Get driver detail info       | :white_check_mark:       |
| CRUD for Vehicle model       | :white_check_mark:       |
| Get vehicle detail info      | :white_check_mark:       |
| Date filter for drivers      | :white_check_mark:       |
| Get/Get out driver from a car| :white_check_mark:       |
| Tested Python version        | 3.9                      |
| Tested Django version        | 3.2.9                    |
| Tested DRF version           | 3.12.4                   |

## The app supports operations

Driver:
+ GET /drivers/driver/ - get drivers list
+ GET /drivers/driver/?created_at__gte=10-11-2021 - get drivers list created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - get drivers list created before 16-11-2021

+ GET /drivers/driver/<driver_id>/ - get driver info
+ POST /drivers/driver/ - create new driver
+ UPDATE /drivers/driver/<driver_id>/ - update driver
+ DELETE /drivers/driver/<driver_id>/ - delete driver

Vehicle:
+ GET /vehicles/vehicle/ - get vehicles list
+ GET /vehicles/vehicle/?with_drivers=yes - get vehicles list with drivers
+ GET /vehicles/vehicle/?with_drivers=no - get vehicles list without drivers

+ GET /vehicles/vehicle/<vehicle_id> - get vehicle info
+ POST /vehicles/vehicle/ - create new car
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - update car
+ POST /vehicles/set_driver/<vehicle_id>/ - get/get out driver from a car  
+ DELETE /vehicles/vehicle/<vehicle_id>/ - delete car


