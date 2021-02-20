from django.db import models

# Create your models here.

class RTOCode(models.Model):
    state_name = models.CharField(max_length=2)
    #  some sectors have 02A like city_codes
    city_code = models.CharField(max_length=4)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name + ' - ' +str(self.city_code) + ' ==> ' + str(self.city_name)




