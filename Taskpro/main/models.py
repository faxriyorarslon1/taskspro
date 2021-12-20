from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(verbose_name="Sarlavha", max_length=250)
    text = models.TextField(verbose_name="Matn qismi", max_length=500)
    image = models.ImageField(verbose_name="surat", upload_to='tasks/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Qayd"
        verbose_name_plural = "Qaydlar"



class Opinion(models.Model):
    ism = models.CharField(max_length=20)
    fikr = models.TextField(max_length=200)
    kasb = models.CharField(max_length=20)
    image = models.ImageField(verbose_name="surat", upload_to='fikrlar/')

    def __str__(self):
        return f"{self.ism} {self.kasb}"

    class Meta:
        verbose_name = "Fikr"
        verbose_name_plural = "Fikrlar"


class Gallery(models.Model):
    image = models.ImageField(verbose_name="rasm", upload_to="gallery")
    name = models.CharField(verbose_name="surat nomi", max_length=20)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Surat"
        verbose_name_plural = "Suratlar"






