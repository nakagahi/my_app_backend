from django.db import models

class User(models.Model):

    GENDERS = (
        ('M', '男性'),
        ('F', '女性'),
    )
    
    last_name = models.CharField(max_length=150, verbose_name='従業員名/苗字', blank=True, default=None, null=True)
    first_name = models.CharField(max_length=150, verbose_name='従業員名/名前', blank=True, default=None, null=True)
    last_name_kana = models.CharField(max_length=150, verbose_name='従業員名/苗字/ひらがな', blank=True, default=None, null=True)
    first_name_kana = models.CharField(max_length=150, verbose_name='従業員名/名前/ひらがな', blank=True, default=None, null=True)
    birthday = models.DateField(verbose_name='生年月日', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS,
                              verbose_name='性別', blank=True, null=True)