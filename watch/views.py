from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Business,User

from django.urls import reverse
from django.http import HttpResponseRedirect



from django.contrib.auth.models import User
import statistics

# Create your views here.

def index(request):
    """
    Displays landing page
    """
    title = "T.N.W"
    business = business.display_all_business()
   

    return render(
        request,
        "index.html",
        {"title": title, "business": business,},
    )