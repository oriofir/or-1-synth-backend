from django.db import models

# Create your models here.


class Synth(models.Model):
    name: models.CharField(max_length=200)
    synth_type: models.CharField(max_length=200)
    filter_amount: models.IntegerField(blank=True, null=True)
    delay_amount: models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
