from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    '''
    Class that defines the project objects
    '''
    name = models.CharField(max_length = 30)
    image = CloudinaryField('image')
    location = models.TextField()    
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    pubdate = models.DateTimeField(auto_now_add=True, null = True)
    occupants = models.ManyToManyField(User, related_name="occupants")
    


    def __str__(self):
        return self.title


    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhod(self):
        self.delete()

    def occupants_count(self):
        return self.occupants.count()




    @classmethod
    def display_all_neighbourhoods(cls):
        return cls.objects.all()

    @classmethod 
    def search_neighbourhood(cls,name):
        return Neighbourhood.objects.filter(title__icontains = name)

    @classmethod
    def get_user_neighbourhood(cls,neighbourhood):
        return cls.objects.filter(neighbourhood=neighbourhood)


