# Generated by Django 3.2.13 on 2022-04-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='xxx', max_length=254),
            preserve_default=False,
        ),
    ]
