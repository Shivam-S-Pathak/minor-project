# Generated by Django 5.0.1 on 2024-03-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_rename_user_table_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='examResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subeject1', models.CharField(max_length=30)),
                ('subeject2', models.CharField(max_length=30)),
                ('subeject3', models.CharField(max_length=30)),
            ],
        ),
    ]
