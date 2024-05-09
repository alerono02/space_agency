from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    image = FilerImageField(on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'
        ordering = ('order',)
