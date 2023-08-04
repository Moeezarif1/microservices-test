# Generated by Django 4.2.2 on 2023-07-20 10:23

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('product_quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('product_description', models.TextField(default='No description available', max_length=500)),
            ],
        ),
    ]
