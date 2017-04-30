from django.db import models
from django.core.urlresolvers import reverse_lazy

def upload_location(instance, filename):
	return '%s/%s' %(instance.id, filename)
	
class Post(models.Model):

	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True,
		height_field='height_field',
		width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)


	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"
		ordering = ['-timestamp', '-update']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse_lazy('posts:detail', kwargs={'id':self.id})