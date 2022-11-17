from django.shortcuts import render, redirect
from .models import Users


# Create your views here.
def home(request):
    # inner join with id where user id =1
    if request.method == 'POST':
        obj = request.POST.get('searchterm')
        print(obj)
        context = {
            'search': obj,
        }
        print(context)
        return render(request, "displaySearchResult.html", context)
    else:
        return render(request, "home.html")


def displaySearchResult(request):
    return redirect("/")