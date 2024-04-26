from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    video = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title