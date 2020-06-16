from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    
    
    # class Meta:
    #     ordering = (name)
        
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    linked_to = models.PositiveIntegerField(default=0)
    
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.created)


class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField(blank=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return 'Message by {} on {}'.format(self.name, self.created)
    

class Suscriber(models.Model):
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Suscriber: {}'.format(self.email)