# Quiz Start


**Note: ** after each change on code, restart server for apply changes

## Make model
Availabel fields:

* IntegerField
* CharField


on minidjango/models.py

```python
from minidjango.db import models


class User(models.Model):
    name = models.CharField(max_length=50, default='Ali')
    age = models.IntegerField()

    def __str__(self):
        return self.name
```

## Make function view

on minidjango/views.py


```python
from minidjango.templates.template import render
from .models import User


def home(request):
    p = User(name='adel', age=22)
    print(p.age)
    context = {
        'title': 'new site'
    }
    return render(request, 'index.html', context)

```

## Set template folder:
**Note:** you can add many folders for templates

on minidjango/settings.py

```python
TEMPLATES = {
    'DIRS': [os.path.join(BASE_DIR, 'templates'), ]
}
```

## Use data of view on html template:

on your template:

```html
<p> {{ title }} </p>
```

## Add url
on minidjango/urls.py


```python
from .views import home

routes = {
    '': home,
    # add another views
}

```


## Run server

run server on default ip and port: 127.0.0.1:8000

```bash
python manage.py runserver
```

to set ip and prot:

replace 127.0.0.1:8002 to your ip and port

```bash
python manage.py runserver 127.0.0.1:8002
```