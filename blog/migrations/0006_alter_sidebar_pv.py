# Generated by Django 4.2.7 on 2023-12-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_sidebar_pv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='pv',
            field=models.PositiveIntegerField(default=0, verbose_name='Views'),
        ),
    ]
