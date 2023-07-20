from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

LANGUAGE = (
        (0, "Korean"),
        (1, "English")
        )

class Category(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Categories'
    
class Series(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Series'

class Tag(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    series = models.ForeignKey("Series", on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tag = models.ManyToManyField("Tag", blank=True, related_name='posts')
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    published_date = models.DateField(blank=True, null=True)
    language = models.PositiveSmallIntegerField(choices=LANGUAGE, default=0)

    def publish(self):
        self.published_date= timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)