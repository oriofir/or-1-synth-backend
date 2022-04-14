from django.db import models

# Create your models here.


class Synth(models.Model):
    name = models.CharField(max_length=200)
    synth_type = models.CharField(max_length=200)
    filter_amount = models.DecimalField(max_digits=3, decimal_places=2)
    delay_amount = models.DecimalField(max_digits=3, decimal_places=2)
    distortion_amount = models.DecimalField(max_digits=3, decimal_places=2)
    autowah_amount = models.DecimalField(max_digits=3, decimal_places=2)
    freeverb_amount = models.DecimalField(max_digits=3, decimal_places=2)
    tremolo_amount = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
