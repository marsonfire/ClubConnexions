# Generated by Django 2.0 on 2018-03-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ama', '0003_officers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberFirstName', models.CharField(max_length=50)),
                ('memberLastName', models.CharField(max_length=50)),
                ('officerPosition', models.CharField(max_length=50)),
            ],
        ),
    ]
