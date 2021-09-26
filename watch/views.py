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

@login_required(login_url="/accounts/login/")
def post_business(request):
    """
    Enables a User to post a project
    """
    if request.method == "POST":
        form = AddBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = request.user
            business.save()

        return redirect("index")
    else:
        form = AddProjectForm()

    return render(request, "post_business.html", {"form": form})

def business_details(request, id):
    """
    Show business details
    """
    business = Business.objects.get(pk=id)
    voted = False
    if project.voters.filter(id=request.user.id).exists():
        voted = True

    return render(request, "business_details.html", {"business": business, })


