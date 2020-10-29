# Generated by Django 3.1.2 on 2020-10-29 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0004_ratings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratings',
            options={'verbose_name_plural': 'Ratings'},
        ),
        migrations.AlterField(
            model_name='ratings',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterUniqueTogether(
            name='ratings',
            unique_together={('product', 'user_profile')},
        ),
        migrations.AlterIndexTogether(
            name='ratings',
            index_together={('product', 'user_profile')},
        ),
    ]
