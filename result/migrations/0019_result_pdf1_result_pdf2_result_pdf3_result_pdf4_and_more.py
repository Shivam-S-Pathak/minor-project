# Generated by Django 5.0.1 on 2024-03-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0018_result_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='pdf1',
            field=models.FileField(blank=True, null=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='result',
            name='pdf2',
            field=models.FileField(blank=True, null=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='result',
            name='pdf3',
            field=models.FileField(blank=True, null=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='result',
            name='pdf4',
            field=models.FileField(blank=True, null=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='result',
            name='pdf5',
            field=models.FileField(blank=True, null=True, upload_to='.'),
        ),
    ]