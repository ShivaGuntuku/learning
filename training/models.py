from django.db import models
from django.conf import settings 
# Create your models here.
class Tutorial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique = True, max_length = 50)
    image = models.ImageField(upload_to = upload_location, 
            null=True, blank=True,
            width_field = "width_field",
            height_field = "height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    content = models.TextField()
    draft = models.BooleanField(default = False)
    publish = models.DateField(auto_now = False, auto_now_add = False,)
    read_time = models.TimeField(null = True, blank = True)
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
