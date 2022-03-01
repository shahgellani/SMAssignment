## Online BookReader & REST API Using DRF
## Setup Project

1. Clone the project using following command
```
git clone git@github.com:enmassenergy/Waste2X-Platform-Source.git
```
2. Make sure you have python 3 installed in your system
-  Open terminal and run command 
```
python3 --version
```
-  If there is not python3 version in your system, please visit https://www.python.org/downloads/

3. Check if you have pip in you OS
-  pip --version or python3 -m pip --version
-  If it says no module named pip please visit https://pip.pypa.io/en/stable/installation/#get-pip-py

4. For mac: 
- Install & Update brew
- Install, Run & Connect Postgres Service
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
brew install postgresql
brew services start postgresql
psql postgres
```

4. For Ubuntu: 
- Update package installer
- Install, Run & Connect Postgres Service
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo apt install postgresql postgresql-contrib pgadmin4
sudo su - postgres
```


5. Setup postgresql database user using postgre shell, postgres is default user, you can create your own or update default user password using following
-  Write this command in terminal to make sure postgres installed properly 
```
postgres --version
```
-  Configuring postgres 
```
psql postgres
```
-  Now see the users you have installed
```
\du
```
-  If you have no user, follow the following commands
```
CREATE ROLE username WITH LOGIN PASSWORD 'quoted password' [OPTIONS]
CREATE ROLE patrick WITH LOGIN PASSWORD 'Getting started';
ALTER ROLE patrick CREATEDB;
createuser patrick --createdb
```
-  If you want to create super user
```
createuser --interactive --pwprompt
```
-  If you have user use the following commands
```
ALTER USER postgres PASSWORD 'newpassword';
CREATE DATABASE cache_db;
```

6. Update Database connection credentials in `cacheproject/settings/development.py`


7. Create Virtual Environment
```
python -m venv {{virtual_env}}
```

8. Activate Environment
```
source {{virtual_env}}/bin/activate
```

9. Install Required Dependencies
For mac: `pycrypto` requires openssl and libffi:
```
xcode-select --install
brew install openssl
brew install libffi
```

Then (for all platforms):
```
pip install -r requirements.txt
```

10. Run following command to migrate django models to database
```
python manage.py makemigrations
python manage.py migrate
```
-   If you are facing issue in python manage.py makemigrations
```
python3 manage.py makemigrations waste2x_web
python manage.py makemigrations
python manage.py migrate
```

11. Run following commands to populate following:
- Locations
- Commodities
- User roles
```
python manage.py runscript populate_locations
python manage.py runscript import_us_commodities
python manage.py runscript import_waste_types
python manage.py sync_roles
```

12. Run following command to create superuser
```
python manage.py createsuperuser
```

13. Run following command to run server
```
python manage.py runserver
```

## Run Test Cases
- For All Apps
- For Single App
- Using Specific pattern
```
python manage.py test
python manage.py test {{app_name}}
python manage.py test --pattern=test_*.py"
```

## Git Branching Structure
- Default latest branch is **Staging**
- Dev branching naming structure is based on **Jira Ticket No**.
- Every task branch finally merged in Staging upon completion/review.
- **Hot Fix** branches are merged directly in staging upon lead approval.

## Overview of Platforms
- Admin: https://app.enmassenergy.com/
- Customer: https://app.enmassenergy.com/customers/
- Supplier: https://app.enmassenergy.com/suppliers/
- Transporter: https://app.enmassenergy.com/carriers/
- REST API Docs: https://app.enmassenergy.com/docs/

## How to deploy new changes
- Create a new branch from **Staging** branch
- Update the codebase according to the change-set required
- Create a **Pull Request** with **Staging** branch
- Review & Merge that PR
