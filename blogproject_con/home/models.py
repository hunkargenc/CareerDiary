from django.db import models
from django.core.validators import RegexValidator

class Home(models.Model):

    favicon = models.ImageField(upload_to="img/favicon/",default="img/favicon.png")
    site_title = models.CharField(max_length=100)
    name_surname = models.CharField(max_length=100)
    username = models.SlugField(max_length=100, unique=True, null=True)
    job_title = models.CharField(max_length=100)
    home_background = models.ImageField(upload_to="img/background/",default="img/favicon.png")
    URL_VALIDATOR_MESSAGE = 'Not a valid URL. Please write https://...'
    URL_VALIDATOR = RegexValidator(regex='(https)', message=URL_VALIDATOR_MESSAGE)
    twitter_url = models.URLField(max_length=200, null=True, blank=True,validators=[URL_VALIDATOR])
    facebook_url = models.URLField(max_length=200, null=True, blank=True,validators=[URL_VALIDATOR])
    instagram_url = models.URLField(max_length=200, null=True, blank=True,validators=[URL_VALIDATOR])
    skype_url = models.CharField(max_length=100)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True,validators=[URL_VALIDATOR])
    calender_url = models.URLField(max_length=200, null=True, blank=True,validators=[URL_VALIDATOR])


    def __str__(self):
        return self.name_surname
