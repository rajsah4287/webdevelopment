# Generated by Django 4.0.6 on 2022-07-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='static/images/product'),
        ),
    ]