# Generated by Django 3.2.3 on 2021-06-11 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='website.category', verbose_name='Категории'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.author', verbose_name='Автор')),
            ],
        ),
    ]
