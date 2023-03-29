from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.title} | {self.date}'


class AboutKEU(Page):
    class Meta:
        pass


class Program(Page):
    class Meta:
        pass


class Project(Page):
    class Meta:
        pass


class About(Page):
    class Meta:
        pass


class News(Page):
    class Meta:
        pass


class BlankPage(Page):
    class Meta:
        pass


class Messages(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    tel_number = models.IntegerField()
    question = models.TextField()

    def __abs__(self):
        return f'{self.name} {self.surname} | {self.question}'

    def get_absolute_url(self):
        return reverse('home')
