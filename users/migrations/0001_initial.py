# Generated by Django 4.2.7 on 2023-11-15 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, default='', max_length=30, verbose_name='name')),
                ('birthday', models.DateField(blank=True, max_length=20, null=True, verbose_name='birthday')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=10, verbose_name='gender')),
                ('address', models.CharField(blank=True, default='', max_length=100, verbose_name='address')),
                ('image', models.ImageField(default='images/default.png', upload_to='images/%Y/%m', verbose_name='user_pic')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
