# Django Rest Framework Group Based Permission
This example will illustrate how to set permission in drf based on user group.
### Clone the project and run the command as shown in the order inside the virtual environment of project
1. Install all the requirements
    ```python
    pip install -r requirements.txt
2. Make migrattions
    ```python
     python manage.py makemigrations
3. Migrate the migrations
    ```python
    python manage.py migrate
4. Run **group.py**
    ```python
    python group.py
5. Create **superuser** provide **groups.id: 1** (group id of admin)
    ```python
    python manage.py createsuperuser
6. Run server
    ```python
    python manage.py runserver

#### Two groups
1. Admin
2. Anonymous

**Admin** group user can 
1. Login
2. Add a new user
3. List all users
4. View individual user
5. Delete users
6. Update all users


**Anonymous** group user can
1. Login
2. List all users
3. View and Update own detail

Without login, no user can get access to the system.
