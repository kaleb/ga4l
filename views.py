from django.http import HttpResponse

def home(request):
    return HttpResponse('''<a href="/admin">Coming soon.</a>''')
