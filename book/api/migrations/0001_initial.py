# Generated by Django 4.0.2 on 2022-02-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('named', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('steps', models.TextField()),
                ('img', models.ImageField(height_field=100, upload_to='book of recipes/article', width_field=100)),
            ],
        ),
    ]
