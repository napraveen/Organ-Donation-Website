# Generated by Django 4.1.7 on 2023-04-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_person_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
