# Generated by Django 3.2.3 on 2021-06-11 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_comment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.post', verbose_name='Пост'),
            preserve_default=False,
        ),
    ]
