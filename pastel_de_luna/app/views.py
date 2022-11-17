from django.shortcuts import render
from .models import Users


# Create your views here.
def profile(request):
    # inner join with id where user id =1
    obj = Users.objects.select_related("role_id").filter(id=1)
    context = {"object": obj}
    return render(request, "home.html", context)