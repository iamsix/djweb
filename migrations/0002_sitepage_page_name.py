# Generated by Django 2.0.7 on 2018-07-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitepage',
            name='page_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
