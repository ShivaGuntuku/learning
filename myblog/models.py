from django.db import models
from django.core.urlresolvers import reverse
from PIL import Image
# Create your models here.

def upload_location(instance,filename):
	return "%s/%s" %(instance.id,filename)

class Posts(models.Model):
	title = models.CharField(max_length = 120)
	slug = models.SlugField(unique = True, max_length = 50)
	image = models.ImageField(upload_to = upload_location, 
			null=True, blank=True,
			width_field = "width_field",
			height_field = "height_field")
	height_field = models.IntegerField(default = 0)
	width_field = models.IntegerField(default = 0)
	content = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __str__(self):
		return  self.title

	def get_absolute_url(self):
		return reverse('posts:detail',kwargs = {'id' : self.id})

	class Meta:
		ordering = ["-timestamp","-updated"]

	# def save(self):
	# 	if not self.image:
	# 		return

	# 	super(Posts, self).save()
	# 	image = Image.open(self.image)
	# 	(width, height) = image.size
	# 	size = ( 100, 100)
	# 	image = image.resize(size, Image.ANTIALIAS)
	# 	image.save(BytesIO(),format="JPEG")