from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class TopSkills(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='top_skills_img/')
    table = RichTextUploadingField()