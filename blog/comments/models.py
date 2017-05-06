from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from django.db import models

# Create your models here.
class CommentManager(models.Manager):
	def all(self):
		qs = super(CommentManager, self).filter(parent=None)
		return qs

	def filter_by_instance(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id 
		qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)	#filtro para ver si esta el padre
		return qs

class Comment(models.Model):
	# post = models.ForeignKey(Post)
	#Relación a cualquier modelo con ContentType
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	content = models.TextField()	
	timestamp = models.DateTimeField(auto_now_add=True)

	parent = models.ForeignKey('self', blank=True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	class Meta:
		ordering = ['-timestamp']

	objects = CommentManager()

	def __str__(self):
		return str(self.user.username)

	def get_absolute_url(self):
		return reverse_lazy('comment:thread', kwargs={'id': self.id})

	def children(self):
		return Comment.objects.filter(parent=self)

	@property
	def is_parent(self):
		if self.parent is not None:
			return False
		return True