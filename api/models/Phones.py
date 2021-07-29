from django.db import models


class Phones(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    number = models.CharField(max_length=12, null=False, verbose_name="Phone Number")
    area_code = models.IntegerField(max_length=12, null=False, verbose_name="Phone Area")
    country_code = models.CharField(max_length=5, null=False, verbose_name="Phone Country")

    def __str__(self):
        return str(self.area_code) + " - " + self.number