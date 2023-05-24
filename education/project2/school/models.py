from django.db import models
from django.contrib.auth.models import AbstractUser



class Newuser(AbstractUser):
    USER_TYPE_CHOICES = (
        
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('student', 'Student'),
    )
    
    # email=models.EmailField(_('email_address'),unique=True)
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, default='student')
    experience = models.CharField(max_length=300)

# Create your models here.
