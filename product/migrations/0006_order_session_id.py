# Generated by Django 3.2 on 2021-04-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_order_order_confirmation_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_id',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
