# Generated by Django 5.0 on 2023-12-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
