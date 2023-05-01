# Generated by Django 4.2 on 2023-04-19 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogger_info', '0006_remove_users_is_authenticated'),
        ('blogs', '0007_alter_blogpost_id_alter_comments_id_alter_tags_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='votes_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogger_info.profile'),
        ),
    ]
