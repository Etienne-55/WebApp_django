from django.db import models

class computer_hardware(models.Model):
    
    name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

