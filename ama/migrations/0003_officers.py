# Generated by Django 2.0 on 2018-03-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ama', '0002_auto_20180324_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officerFirstName', models.CharField(max_length=50)),
                ('officerLastName', models.CharField(max_length=50)),
                ('officerPosition', models.CharField(max_length=50)),
            ],
        ),
    ]
