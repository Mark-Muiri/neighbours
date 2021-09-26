from django.shortcuts import render

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