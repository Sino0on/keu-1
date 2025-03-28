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


class ProgramCategory(models.Model):
    title = models.CharField(max_length=123)


class AboutKEU(Page):
    category = models.ForeignKey('AboutCategory', on_delete=models.CASCADE, related_name='about_pages', blank=True, null=True)

    class Meta:
        pass


class HeadCategory(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return f'{self.name}'


class AboutCategory(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=123)
    head_category = models.ForeignKey(HeadCategory, on_delete=models.CASCADE, related_name='categories', blank=True,
                                      null=True)

    def __str__(self):
        return f'{self.name}'


class Program(Page):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='programs', blank=True, null=True)

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


class DocsForum(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Форум категория'
        verbose_name_plural = 'Форум категории'


class Documents(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка', blank=True, null=True)
    file = models.FileField(upload_to='files/', verbose_name='Файл', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(DocsForum, on_delete=models.CASCADE, related_name='docs', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
