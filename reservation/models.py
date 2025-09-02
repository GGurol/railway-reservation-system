from django.db import models

# Create your models here.
class Train(models.Model):
    train_name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    time = models.TimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=120.00) # Use DecimalField for money
    seats_available = models.IntegerField()

    def __str__(self):
        return self.train_name

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date_and_time_of_booking = models.DateTimeField(auto_now_add=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE) # Also update the ForeignKey

    def __str__(self):
        return self.name