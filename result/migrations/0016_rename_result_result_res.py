# Generated by Django 5.0.1 on 2024-03-05 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0015_rename_marks_result_total_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='result',
            new_name='res',
        ),
    ]
