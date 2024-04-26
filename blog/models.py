from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=212)
    last_name = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()
    image = models.ImageField(upload_to='images')
    password = models.CharField(max_length=212)
    region = models.CharField(max_length=212)

    def __str__(self):
        return self.first_name


class Video_Darslar(models.Model):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='video')
    video = models.FileField(upload_to='video')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.TimeField(auto_now=False)

    def __str__(self):
        return self.name


class Client(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video_Darslar, on_delete=models.CASCADE)
    is_pay = models.BooleanField(default=False)




class Payment(models.Model):
    price = models.CharField(max_length=212)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.price



class Team(models.Model):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='team')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.TimeField(auto_now=False)

    def __str__(self):
        return self.name


class Web_sites(models.Model):
    name = models.CharField(max_length=212)
    link = models.CharField(max_length=212)
    price = models.CharField(max_length=212)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.TimeField(auto_now=False)

    def __str__(self):
        return self.name

class Web_images(models.Model):
    website_id = models.ForeignKey(Web_sites, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='website')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.TimeField(auto_now=False)

    def __str__(self):
        return self.website_id.name