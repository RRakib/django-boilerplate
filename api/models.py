from django.db import models


class DemoPurpose(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Demo"

    def __str__(self):
        return self.name
