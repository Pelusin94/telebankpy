from django.db import models

class CharityNames(models.Model):
    display_name    = models.CharField(max_length=100, blank=True, null=True)
    system_name     = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.display_name

    def __str__(self):
        return self.system_name