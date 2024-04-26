from rest_framework import serializers
from .models import ( Users, Video_Darslar, Client, Payment, Team, Web_sites, Web_images
)

class  UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class Video_DarslarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_Darslar
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class Web_sitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web_sites
        fields = '__all__'


class Web_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web_images
        fields = '__all__'


