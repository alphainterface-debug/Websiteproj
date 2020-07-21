# Generated by Django 3.0.8 on 2020-07-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
