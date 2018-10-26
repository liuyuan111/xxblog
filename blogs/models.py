from django.db import models
from datetime import datetime
from users.models import *
# Create your models here.
#轮播图
class Banner(models.Model):
    title = models.CharField('标题', max_length=50, default=None)
    cover = models.ImageField('轮播图', upload_to='static/images/banner', default=None)
    link_url = models.URLField('图片链接', max_length=100)
    idx = models.IntegerField('索引')
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'
#博客分类
class BlogCategory(models.Model):
    name = models.CharField('分类名称', max_length=20, default='')
    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
#标签
class Tags(models.Model):
    name = models.CharField('标签名称', max_length=20, default='')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name
#博客
class Post(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='作者', on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, verbose_name='博客分类', default=None, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField('标题', max_length=50, default=None)
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发布日期', default=datetime.now)
    cover = models.ImageField('博客封面', upload_to='static/images/post', default=None)
    views = models.IntegerField('浏览数', default=0)
    recommend = models.BooleanField('推荐博客', default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='博客', on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, verbose_name='作者', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('发布时间')
    content = models.TextField('内容')

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


class FriendlyLink(models.Model):
    title = models.CharField('标题', max_length=50)
    link = models.URLField('链接', max_length=50, default='')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'