from django.db import models

class Coffee(models.Model):
    
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    roast = models.CharField(max_length=50)

    def __str__(self):
        return self.name