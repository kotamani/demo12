# Generated by Django 3.1.3 on 2020-11-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
            ],
        ),
    ]
