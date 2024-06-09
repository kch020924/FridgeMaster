# DIS fianl project: Fridge Master
## Summary
Fridge_Master is python & Django based recipe recommendating website. Unlike existing recipe sharing sites, Fridge_Master focuses more on users by gathering data about groceries. Each user can become both publisher and reader as registering the groceries they bought or uploading their own recipes on the website.

    git repository: https://github.com/goeunP/FridgeMaster


## Database init
1. set the database in fridge_master > settings.py > "DATABASES"
Example: 

    change into your name, user, password
   {
   'NAME':'name of your database',
   'USER':'user name of that database',
   'PASSWORD':'password of that database'
   }

2. run schema.sql, schema_ins.sql, schema_upd.sql in your database
3. run sql_ddl/ddl-customers-001-add.sql in your database.

Example: 

    psql -d{database} -U{user} -W -f schema.sql
   
#### notes
For Ubuntu add host (-h127.0.0.1) to psql: 

    psql -d{database} -U{user} -h127.0.0.1 -W -f schema.sql

## Running Server
#### 1.OSX: 

    python manage.py runserver


Create virtual environment in folder

    python3 -m venv .venv

Activate virtual environment in folder

    . .venv/bin/activate


#### 2.WINDOWS:

Create virtual environment in folder

    py -3 -m venv .venv

Activate virtual environment in folder

    .venv\Scripts\activate

### Install Django

    pip install django
    
    pip install psycopg2


