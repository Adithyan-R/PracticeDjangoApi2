# Generated by Django 5.0.6 on 2024-06-13 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorialNo', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('StartDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
