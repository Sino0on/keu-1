# Generated by Django 4.2.6 on 2024-05-31 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocsForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123, verbose_name='Название')),
                ('url', models.URLField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Форум категория',
                'verbose_name_plural': 'Форум категории',
            },
        ),
        migrations.AddField(
            model_name='documents',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='app.docsforum'),
        ),
    ]
