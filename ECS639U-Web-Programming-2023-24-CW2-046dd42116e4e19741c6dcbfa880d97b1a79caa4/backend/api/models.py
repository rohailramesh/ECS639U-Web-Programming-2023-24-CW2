from django.db import models


# Create your models here.
class Demonstrator_Claim(models.Model):
    module_name = models.CharField(max_length=100)
    hours_worked = models.FloatField()
    claim_form_submitted = models.BooleanField()
    demonstrated_date = models.DateField()

    def __str__(self):
        return self.module_name
