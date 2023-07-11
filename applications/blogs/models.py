from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel


class Tag(models.Model):
    text = models.CharField(max_length=255)
    visit_count = models.PositiveIntegerField(default=0, editable=False)
    slug = AutoSlugField(populate_from='text')

    def __str__(self):
        return self.text


class Blog(models.Model):
    title = models.CharField(max_length=255)
    banner_title = models.CharField(max_length=255, null=True, blank=True)
    slug = AutoSlugField(populate_from='title')
    body = RichTextUploadingField()
    date = models.DateField(auto_now=True)
    image = models.ImageField()
    gallery_info = models.TextField()
    main_image = models.ImageField()
    banner_image = models.ImageField()
    tags = models.ManyToManyField(Tag)
    publish = models.BooleanField(default=0)
    visit_count = models.PositiveIntegerField(default=0)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['order']


class Gallery(models.Model):
    blog = models.ForeignKey(Blog, null=True, blank=True, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Galley Image"
        verbose_name_plural = "Gallery Images"


class About(SingletonModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    video = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"


class SocialMediaProfiles(models.Model):
    about_content = models.ForeignKey(About, related_name='social_profiles', on_delete=models.CASCADE)
    site = models.CharField(max_length=255)
    profile_link = models.URLField()
    image = models.ImageField()
    description = RichTextUploadingField()

    def __str__(self):
        return self.site

    class Meta:
        verbose_name = "Social Media"
