# Generated by Django 3.2.8 on 2021-10-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_descripction_todo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isfrendly', models.BooleanField()),
                ('opinion', models.TextField()),
                ('qualification', models.IntegerField(choices=[[0, 'Muy Malo'], [1, 'Malo'], [2, 'Aceptable'], [3, 'Bueno'], [4, 'Muy Bueno']])),
            ],
        ),
    ]
