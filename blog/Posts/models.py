from django.db import models

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
        