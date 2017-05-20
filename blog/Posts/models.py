from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from comments.models import Comment
from .utils import get_read_time
	#override al manager
class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
	return '%s/%s' %(instance.id, filename)
	
class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True,
		height_field='height_field',
		width_field='width_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)
	draft = models.BooleanField(default=False)
	publish = models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
	read_time = models.IntegerField(default=0)
	

	objects = PostManager()


	class Meta:
		ordering = ['-timestamp', '-update']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse_lazy('posts:detail', kwargs={'slug':self.slug})

	def get_list_url(self):
		return reverse_lazy('posts:list', kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse_lazy('posts:delete', kwargs={'slug':self.slug})

	def get_absolute_url_update(self):
		return reverse_lazy('posts:update', kwargs={'slug':self.slug})

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)

	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(instance)
		return qs
	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

#crea slug para identificar con esto en lugar de id
def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:	#si no tiene crea un nuevo slug
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by('-id')		#la consulta los filtra por slug
	exists = qs.exists()
	if exists:					#si existe le agrega +1, esto sólo  si es el mismo titulo
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

#guarda el slug que recive con la señal
def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
	#se le asigna a instance el tiempo de lectura
	if instance.content:
		html_string = instance.get_markdown()
		read_time_var = get_read_time(html_string)
		instance.read_time = read_time_var

pre_save.connect(pre_save_post_receiver, sender=Post)	#Remitente
