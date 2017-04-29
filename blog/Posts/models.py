from django.db import models
from django.core.urlresolvers import reverse_lazy
class Post(models.Model):

	title = models.CharField(max_length=50)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)


	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse_lazy('posts:detail', kwargs={'id':self.id})