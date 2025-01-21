from minidjango.templates.template import render


def home(request):
    return render(request, 'index.html', {})