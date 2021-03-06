# Generated by Django 2.2.7 on 2019-11-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('name', models.TextField()),
                ('date', models.TextField()),
                ('sandwitch', models.TextField()),
                ('size', models.TextField()),
                ('bread', models.TextField()),
                ('source', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
