# Generated by Django 4.0.1 on 2022-02-19 21:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0014_merge_20220218_2035'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='surveysession',
            unique_together={('survey', 'owner')},
        ),
    ]
