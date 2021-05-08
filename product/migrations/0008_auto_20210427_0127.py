# Generated by Django 3.2 on 2021-04-27 01:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_cartitem_fridge_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-date_created',), 'verbose_name_plural': 'الطلبات'},
        ),
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
