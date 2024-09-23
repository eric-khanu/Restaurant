from django.db import models
 
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Options(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = ("Extra")

    def __str__(self):
        return self.name
    

class Dishes(models.Model):
    name = models.CharField(max_length=50)
    incredients = models.CharField(max_length=150)
    price = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Extra = models.ForeignKey(Options, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restaurants\zee_kitchen\static\images', default='')


    class Meta:
        verbose_name_plural = ("Dishes")

    def __str__(self):
        return f"{self.name}  ---- {self.category}    ------ {self.price}  ---- {self.Extra}"