# Generated by Django 3.1.1 on 2020-09-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandbox_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucketlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
