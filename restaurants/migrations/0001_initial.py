# Generated by Django 4.1.2 on 2022-10-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('descrition', models.TextField(default='')),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
