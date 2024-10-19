from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

def user_profile_pic_path(instance, filename):
    return f'profile_pics/{instance.email}/profile.jpg'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, username=username, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(upload_to=user_profile_pic_path, default='default_profile_pic.jpg')
    otp = models.CharField(max_length=6,blank=True,null=True)
    otp_verified = models.BooleanField(default=False) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tshirt', 'T-shirt'),
        ('pants', 'Pants'),
        ('jackets', 'Jackets'),
        ('men', 'Men'),
        ('women', 'Women'),
    ]    
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    material_composition = models.CharField(max_length=255, blank=True)
    pattern = models.CharField(max_length=255, blank=True)
    fit_type = models.CharField(max_length=255, blank=True)
    sleeve_type = models.CharField(max_length=255, blank=True)
    collar_style = models.CharField(max_length=255, blank=True)
    length = models.CharField(max_length=255, blank=True)
    country_of_origin = models.CharField(max_length=255, blank=True)
    details = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tshirt')

    def __str__(self):
        return self.name