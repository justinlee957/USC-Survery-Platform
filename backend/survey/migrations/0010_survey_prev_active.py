# Generated by Django 4.0.1 on 2022-02-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_alter_surveycode_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='prev_active',
            field=models.BooleanField(default=False),
        ),
    ]