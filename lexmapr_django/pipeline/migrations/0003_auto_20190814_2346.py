# Generated by Django 2.1.8 on 2019-08-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0002_auto_20190814_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelinejob',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]