# Generated by Django 5.0.1 on 2024-03-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0010_rename_exam_type_exam_exam_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='subject',
        ),
        migrations.AddField(
            model_name='result',
            name='subject1',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject2',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject3',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject4',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject5',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject6',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='result',
            name='subject7',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
