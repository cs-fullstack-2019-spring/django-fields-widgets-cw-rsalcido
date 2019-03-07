from django.db import models

# Create your models here.


class supeHero(models.Model):
    name= models.CharField(max_length=25)
    city_or_origin= models.CharField(max_length=40)
    dropdown=models.CharField(max_length=35)#,rich or have super powers)
    dropdown2=models.CharField(max_length=35)#,super power(Flight, Speed, Invisibility, Telekenetic, Healing, Other)
    dropdown3=models.CharField(max_length=35)#,following (Good, kinda good, neutral, a little evil, evil)
    text=models.CharField(max_length=200) #,(3 examples of when you used your super hero abilities.)