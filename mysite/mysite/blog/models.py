from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = "published")


class Post(models.Model):
    objects = models.Manager()  #defalut
    published = PublishedManager() #Our custome model maanger
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )

    title  = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User,related_name='blog_posts', on_delete=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name= 'likes', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("blog:post_details", args=[self.id, self.slug])

@receiver(pre_save, sender= Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "Profile of User{}".format(self.user.username)

