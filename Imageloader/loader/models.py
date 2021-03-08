from django.db import models


class UploadImage(models.Model):
    file = models.ImageField(upload_to='uploads')

    class Meta:
        verbose_name = 'загруженное изображение'
        verbose_name_plural = 'загруженные изображения'

    def __str__(self):
        return str(self.pk)






