# Generated by Django 3.2.13 on 2022-12-10 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
