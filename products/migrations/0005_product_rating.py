# Generated by Django 3.2 on 2022-05-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
