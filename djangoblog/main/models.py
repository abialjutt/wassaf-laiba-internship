from datetime import datetime
import imp
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser 
from .manager import UserManager

# Create your models here.

class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length= 200)
    category_summary = models.CharField(max_length= 200)
    category_slug = models.SlugField(null=True)

    def save(self, *args, **kwargs):
            self.category_slug = slugify(self.tutorial_category)
            super(TutorialCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

        def __str__(self) -> str:
            return self.tutorial_category
        
        


class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, verbose_name="Category", on_delete=models.CASCADE)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published', default= datetime.now())
    tutorial_series = models.ForeignKey(TutorialSeries, verbose_name="Series", on_delete=models.CASCADE)
    tutorial_slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.tutorial_title
    
    def save(self, *args, **kwargs):
                self.tutorial_slug = slugify(self.tutorial_title)
                super(Tutorial, self).save(*args, **kwargs)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100,null=True, blank=True)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []