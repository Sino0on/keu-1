from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
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
