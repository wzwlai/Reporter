from django.db import models

# Create your models here.


class Industry(models.Model):
    """行业表"""
    name = models.CharField(max_length=20,verbose_name='行业名称')

    class Meta:
        db_table = 'tb_industry'
        verbose_name = '行业'
        verbose_name_plural = verbose_name

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class Company(models.Model):
    """公司表"""
    name = models.CharField(max_length=20,verbose_name='公司全称')
    abbreviation = models.CharField(max_length=10,verbose_name='公司简称')
    Synopsis = models.CharField(max_length=500,verbose_name='公司简介')
    address = models.CharField(max_length=30,verbose_name='地址')
    contact = models.CharField(max_length=10,verbose_name='联系人')

    class Meta:
        db_table = 'tb_company'
        verbose_name = '公司'
        verbose_name_plural = verbose_name

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class Manuscript(models.Model):
    """历史稿件"""
    name = models.CharField(max_length=20,verbose_name='稿件名')
    createTime = models.DateField(verbose_name='发布日期')
    issuer = models.CharField(max_length=10,verbose_name='发布人')
    content = models.CharField(max_length=500,verbose_name='稿件文字内容')

    class Meta:
        db_table = 'tb_manuscript'
        verbose_name = '历史稿件'
        verbose_name_plural = verbose_name

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class Reporters(models.Model):
    """记者个人信息表"""
    name = models.CharField(max_length=10, verbose_name='姓名')
    mobile = models.CharField(max_length=11,unique=True,verbose_name="手机号")
    password = models.CharField(max_length=20, verbose_name='密码')
    Industry_Id = models.ForeignKey('Industry', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='行业')
    Company_Id = models.ForeignKey('Company', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='公司')
    Manuscript_Id = models.ForeignKey('Manuscript', null=True, blank=True, on_delete=models.SET_NULL,verbose_name='历史稿件')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_reporters'  # 指明数据库表名
        verbose_name = '记者'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
