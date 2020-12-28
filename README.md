# Virtual Classroom Platform


## Steps to setup
Follow the following commands in your terminal to checkout this primitive auth system for single users 
```
$ trydjango\Scripts\activate
```
```
$ pip install -r requirements.txt 
```
```
$ pip install django-crispy-forms
```

Here please change your directory to the one which has the manage.py file in your system
```
$ python manage.py migrate 
```
```
$ python manage.py runserver
```

For admin access run:
```
$ python manage.py createsuperuser
```

Django version 3.1.4,settings 'mysite.settings'
Default development server at http://127.0.0.1:8000/
