# Generated by Django 4.0.3 on 2022-03-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmesInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('link_filme', models.TextField()),
                ('link_poster', models.TextField()),
                ('nota', models.CharField(max_length=255)),
            ],
        ),
    ]