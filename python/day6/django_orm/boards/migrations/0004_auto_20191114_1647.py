# Generated by Django 2.2.7 on 2019-11-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_subway'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subway',
            name='bread',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subway',
            name='date',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subway',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='subway',
            name='sandwitch',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subway',
            name='size',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subway',
            name='source',
            field=models.TextField(max_length=10),
        ),
    ]
