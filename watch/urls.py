from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),

    path("post/<int:id>", views.business_details, name="business_details"),
    path("post/business", views.post_business, name="post_business"),
    path('search/', views.business_search, name = "business_search"),
    path('profile/',views.profile, name = "profile"),
   
   
    path('profile/edit/', views.edit_profile,name= 'edit_profile'),
    # path('api/businesses/', views.businessList.as_view()),
    # path('api/profiles/', views.ProfileList.as_view()), 
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
