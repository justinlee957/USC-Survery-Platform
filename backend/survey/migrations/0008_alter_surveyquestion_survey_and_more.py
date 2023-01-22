# Generated by Django 4.0.1 on 2022-02-04 22:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_remove_surveyquestion_hidden_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyquestion',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.survey'),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='type',
            field=models.CharField(choices=[('MC', 'Multiple Choice'), ('CB', 'Checkboxes'), ('DP', 'Dropdown'), ('SC', 'Scale'), ('SA', 'Short Answer'), ('PA', 'Long Answer')], max_length=2),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.surveyquestionchoice'),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='survey.surveyquestion'),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='survey.surveysubmission'),
        ),
        migrations.CreateModel(
            name='SurveyCode',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
        ),
    ]
