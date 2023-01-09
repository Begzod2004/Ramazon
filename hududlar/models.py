from django.db import models

class Hududlar(models.Model):
    nomi = models.CharField(max_length=30)
    vaqt_farqi = models.IntegerField(default=0)

    def __str__(self):
        return self.nomi

class Vaqt(models.Model):
    sana = models.DateField()
    ochish = models.TimeField()
    yopish = models.TimeField()
    hudud = models.ForeignKey(Hududlar, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.sana)

