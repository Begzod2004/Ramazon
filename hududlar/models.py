from django.db import models

class Hududlar(models.Model):
    hudud_id = models.IntegerField()
    nomi = models.CharField(max_length=30)
    vaqt_farqi = models.IntegerField(default=0)

    def __str__(self):
        return self.nomi

class Vaqt(models.Model):
    sana = models.DateField()
    ochish = models.TimeField()
    yopish = models.TimeField()
    hudud = models.ForeignKey(Hududlar, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sana)
    

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.text)

class Answer(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)
    

class VideoCategory(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.title)
    
class Video(models.Model):
    text = models.CharField(max_length=255)
    link = models.TextField()
    vide_category = models.ForeignKey(VideoCategory, related_name='videocategory', on_delete=models.CASCADE)


class Viloyat(models.Model):
    nomi = models.CharField(max_length=30)
    vaqt_farqi = models.IntegerField(default=0)

    def __str__(self):
        return str(self.nomi)

class NamozVaqti(models.Model):
    sana = models.DateField()
    bomdod = models.TimeField()
    peshin = models.TimeField()
    asr = models.TimeField()
    shom = models.TimeField()
    xufton = models.TimeField()
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sana)
    