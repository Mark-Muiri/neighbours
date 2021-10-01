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
    business = Business.objects.all()
   

    return render(
        request,
        "index.html",
        {"title": title, "business": business,},
    )

@login_required(login_url="/accounts/login/")
def post_business(request):
    """
    Enables a User to post a business
    """
    if request.method == "POST":
        form = AddBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = request.user
            business.save()

        return redirect("index")
    else:
        form = AddbusinessForm()

    return render(request, "post_business.html", {"form": form})

def business_details(request, id):
    """
    Show business details
    """
    business = Business.objects.get(pk=id)
   

    return render(request, "business_details.html", {"business": business, })


def business_search(request):
    """
    Display search results
    """
    if "business" in request.GET and request.GET["business"]:
        searched_business = request.GET.get("business")
        business = Business.search_business(searched_business)
        message = f"{searched_business}"

        return render(
            request, "search.html", {"business": business, "message": message}
        )
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message": message})
    


def profile(request):
    """
    Displays User's profile page
    """
    title = "Profile"
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    business = Business.get_user_business(current_user)

    return render(request, "profile.html", {"profile": profile, "business": business})



def edit_profile(request):
    """
    Edits profile
    """
    current_user = request.user

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            bio = form.cleaned_data["bio"]
            picture = form.cleaned_data["picture"]
            email = form.cleaned_data["email"]
            

            updated_profile = Profile.objects.get(user=current_user)
            updated_profile.bio = bio
            updated_profile.picture = picture
            updated_profile.email = email
            
            updated_profile.save()
        return redirect("profile")
    else:
        form = EditProfileForm()
    return render(request, "edit_profile.html", {"form": form})


