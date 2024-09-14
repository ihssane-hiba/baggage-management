@echo off

:: Create the main directories
mkdir .\app
mkdir .\app\models
mkdir .\app\services
mkdir .\app\routes
mkdir .\app\utils
mkdir .\app\templates

:: Create the main files
echo > .\app\__init__.py
echo > .\app\models\user.py
echo > .\app\models\parcel.py
echo > .\app\models\__init__.py
echo > .\app\services\user_service.py
echo > .\app\services\parcel_service.py
echo > .\app\services\__init__.py
echo > .\app\routes\auth_routes.py
echo > .\app\routes\user_routes.py
echo > .\app\routes\parcel_routes.py
echo > .\app\routes\__init__.py
echo > .\app\utils\db_setup.py
echo > .\app\utils\__init__.py
echo > .\app\templates\login.html
echo > .\config.py
echo > .\requirements.txt
echo > .\run.py

echo Project structure created successfully!
