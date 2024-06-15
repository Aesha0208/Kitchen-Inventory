from django.db import models

class Add_Inventory(models.Model):
    # feilds of model
    Product = models.CharField(max_length=200)
    Unit = models.CharField(max_length=200)
    Quantity = models.CharField(max_length=200)

    def __str__(self):
        return self.Product

class Create_Inventory(models.Model):
    # feilds of model
    ProductName = models.ForeignKey(Add_Inventory,on_delete=models.CASCADE)
    Year = models.CharField(max_length=200)
    Month = models.CharField(max_length=200)



   


   
   
