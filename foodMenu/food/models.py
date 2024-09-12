from django.db import models

# Create your models here.
class Food(models.Model):
    def __str__(self) :
        return self.food_name
    
    food_name=models.CharField(max_length=128)
    food_desc=models.CharField(max_length=1000)
    food_price=models.IntegerField()
    
    
    
    
    
    
