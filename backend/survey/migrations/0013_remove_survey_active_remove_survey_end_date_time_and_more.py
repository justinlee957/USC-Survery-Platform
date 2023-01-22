# Generated by Django 4.0.1 on 2022-02-18 02:38

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0012_surveysession_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='active',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='end_date_time',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='prev_active',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='start_date_time',
        ),
        migrations.AddField(
            model_name='surveysession',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='type',
            field=models.CharField(choices=[('MC', 'Multiple Choice'), ('CB', 'Checkboxes'), ('DP', 'Dropdown'), (
                'SC', 'Scale'), ('SA', 'Short Answer'), ('PA', 'Long Answer'), ('RK', 'Ranking')], max_length=2),
        ),
    ]