# Generated by Django 5.0.3 on 2024-04-02 11:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('quantity_in_stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('quantity_sold', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
