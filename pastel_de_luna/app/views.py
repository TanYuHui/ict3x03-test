from django.shortcuts import render
from .models import Users


# Create your views here.
def home(request):
    # inner join with id where user id =1
    obj = request.POST.get('searchterm')
    print(obj)
    return render(request, "home.html")