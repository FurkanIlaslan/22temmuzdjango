# Generated by Django 4.2.3 on 2023-11-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('resim', models.FileField(upload_to='filmler/', verbose_name='Film Adı')),
            ],
        ),
    ]