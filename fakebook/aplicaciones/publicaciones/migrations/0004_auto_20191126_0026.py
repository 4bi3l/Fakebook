# Generated by Django 2.2.5 on 2019-11-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_auto_20191125_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Post_img', verbose_name='Imagen'),
        ),
    ]
