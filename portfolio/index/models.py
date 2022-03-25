from django.db import models

class about(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=1000,blank=False)
    image = models.ImageField(upload_to="about/", blank=False, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title


class slider(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=1000,blank=False)
    image = models.ImageField(upload_to="slider/", blank=False, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title


class client(models.Model):
    name = models.CharField(max_length=100,blank=False)
    link = models.CharField(max_length=400,blank=False)
    image = models.ImageField(upload_to="client/", blank=False, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name
    
class location(models.Model):
    address = models.CharField(max_length=400,blank=False)
    email = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=15,blank=False)

    def __str__(self):
        return self.address    


class external_contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.CharField(max_length=100,blank=False)
    subject = models.CharField(max_length=400,blank=False)
    message = models.CharField(max_length=1000,blank=False)

    def __str__(self):
        return self.name  