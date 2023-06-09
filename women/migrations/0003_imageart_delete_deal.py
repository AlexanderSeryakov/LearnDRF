# Generated by Django 4.1.7 on 2023-03-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_deal'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageArt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название картины')),
                ('author', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Deal',
        ),
    ]
