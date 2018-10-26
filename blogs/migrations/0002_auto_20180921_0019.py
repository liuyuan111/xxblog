# Generated by Django 2.1.1 on 2018-09-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='标题',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='轮播图',
        ),
        migrations.RemoveField(
            model_name='post',
            name='标题',
        ),
        migrations.AddField(
            model_name='banner',
            name='cover',
            field=models.ImageField(default=None, upload_to='static/images/banner', verbose_name='轮播图'),
        ),
        migrations.AddField(
            model_name='banner',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='是否是active'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(default=None, max_length=50, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='idx',
            field=models.IntegerField(verbose_name='索引'),
        ),
    ]
