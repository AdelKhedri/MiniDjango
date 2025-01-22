from minidjango.templates.template import render
from .models import User


def home(request):
    p = User(name='adel', age=1)
    print(p.age)
    return render(request, 'index.html', {})