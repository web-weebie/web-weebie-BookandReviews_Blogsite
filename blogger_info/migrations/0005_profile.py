# Generated by Django 4.2 on 2023-04-10 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogger_info', '0004_alter_users_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=200, null=True, verbose_name='the first name of a user')),
                ('lastname', models.CharField(blank=True, max_length=200, null=True, verbose_name='the last name of a user')),
                ('display_pic', models.ImageField(blank=True, default='static/images/avatar.jpg', null=True, upload_to='photo/%Y/%m/%d', verbose_name='profile picture')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio of user')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
