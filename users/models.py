from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class BlogUser(AbstractUser):
    nikename = models.CharField(name='昵称', max_length=50, default='')

class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=50, default='')
    email = models.EmailField(verbose_name='邮箱', max_length=50)
    send_type = models.CharField(verbose_name='验证码类型', choices=(("register", u"注册"), ("forget", u"找回密码"), ("update_email", u"更改邮箱")), max_length=50)
    send_time = models.DateTimeField(verbose_name='发送时间', default=datetime.now)
    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{0}{1}'.format(self.code,self.email)


