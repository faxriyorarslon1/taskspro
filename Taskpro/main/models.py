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


