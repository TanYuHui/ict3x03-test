from django.shortcuts import render, redirect

from django.views.decorators.debug import sensitive_post_parameters
from django.utils.html import escape



@sensitive_post_parameters()
# Create your views here.
def home(request):
    if request.method == 'POST':
        obj = escape(request.POST.get('searchterm'))
        if obj == "":
            return render(request, "home.html")
        else:
            print(obj)
            context = {
                'search': obj,
            }
            print(context)
        return render(request, "displaySearchResult.html", context)
    else:
        return render(request, "home.html")


def displaySearchResult():
    return redirect("/")
