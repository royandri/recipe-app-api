# Generated by Django 2.1.15 on 2020-03-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
