# Generated by Django 2.1.1 on 2018-09-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='cast_set',
            field=models.ManyToManyField(to='petter.Cast', verbose_name='참여인원'),
        ),
    ]