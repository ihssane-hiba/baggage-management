# baggage management
 
# to start
run the following command to install the dependencies
> pip install -r requirements.txt

# the data base

change the infromation in the .env file to use you data base
if you are using mysql data base change the db_type to mysql instead of postgresql

# the hierarchy of the applicaion

/baggage_management
│
├── /app
│   ├── /models
│   │   ├── user.py         # Models for the user table
│   │   ├── parcel.py       # Models for the baggage/parcel table
│   │   └── __init__.py     # Initialize SQLAlchemy models
│   │
│   ├── /services
│   │   ├── user_service.py # Business logic for users (admin)
│   │   ├── parcel_service.py # Business logic for parcels (workers)
│   │   └── __init__.py     # Import services
│   │
│   ├── /routes
│   │   ├── auth_routes.py   # Login, Logout, Session management
│   │   ├── user_routes.py   # User-related routes (Admin role)
│   │   ├── parcel_routes.py # Parcel-related routes (Worker role)
│   │   └── __init__.py      # Initialize routes
│   │
│   ├── /utils
│   │   ├── db_setup.py      # Class to manage DB connection and initialization
│   │   └── __init__.py      # Initialize utils
│   │
│   ├── /templates           # HTML templates for views (login, lists, forms, etc.)
│   │   └── login.html
│   │
│   ├── __init__.py          # Main app factory function to initialize the app
│
├── config.py                # Configurations for PostgreSQL and MySQL
├── requirements.txt         # Project dependencies
└── run.py                   # Entry point to run the Flask application
