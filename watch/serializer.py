from rest_framework import serializers
from .models import Neighbourhood, User, Business

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta :
        model = Neighbourhood
        fields = ('title', 'description','image','profile', 'pubdate')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user', 'bio', 'picture', 'email', 'github_link')


class BusinessSerializer(serializers.ModelSerializer):
    class Meta :
        model = Business
        fields = ('name', 'image', 'location', 'admin','pubdate','occupants')