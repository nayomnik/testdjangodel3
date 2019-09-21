from django.db import models


#   number to count
#   address of office
#   alias
class LineInOffice(models.Model):
    addressOfOffice = models.CharField("Корхоная манзилаш/ориентир",max_length= 200)
    alias = models.CharField("Корхоная калта номаш", max_length=100)
    occuredTime = models.CharField("Ахиранги хизмата вакташ", default='2019-09-20 13:55:47',max_length=100)
    numberToCount = models.IntegerField('Раками навбат')
    class Meta:
        verbose_name= "Очарад корхонаба"
        verbose_name_plural= "Очарадхо корхонаба"