# Generated by Django 2.1.8 on 2019-08-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pipelinejob',
            name='input',
        ),
        migrations.RemoveField(
            model_name='pipelinejob',
            name='output',
        ),
        migrations.AddField(
            model_name='pipelinejob',
            name='input_file',
            field=models.FileField(blank=True, upload_to='input_files/'),
        ),
        migrations.AddField(
            model_name='pipelinejob',
            name='output_file',
            field=models.FileField(blank=True, upload_to='output_files/'),
        ),
    ]