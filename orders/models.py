from typing import Tuple, List
from django.db import models

_size = models.CharField(max_length=1, blank=False)  # DRY


class Dish(models.Model):
    class Meta:
        db_table = 'Menu'

    article = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)   # Store prices in terms of cents.


# Above classes are inherited from <Dish>
class Pizza(Dish):
    class Meta:
        db_table = 'Pizzas'

    mode = models.CharField(max_length=15)
    size = _size

    def __str__(self):
        return f"Pizza: {self.article}, {self.size}, with {self.mode.lower()}"


class Topping(Dish):
    class Meta:
        db_table = 'Toppings'

    def __str__(self):
        return f"Topping: {self.article}"


class Sub(Dish):
    class Meta:
        db_table = 'Subs'

    size = _size

    def __str__(self):
        return f"Sub: {self.article}, {self.size}"


class Pasta(Dish):
    class Meta:
        db_table = 'Pasta'

    def __str__(self):
        return f"Pasta: {self.article}"


class Salad(Dish):
    class Meta:
        db_table = 'Salads'

    def __str__(self):
        return f"Salad: {self.article}"


class DinnerPlatter(Dish):
    class Meta:
        db_table = 'Dinner Platters'

    size = _size

    def __str__(self):
        return f"Dinner Platter: {self.article}, {self.size}"


class Order(models.Model):
    class Meta:
        db_table = 'Orders'

    customer = models.CharField(max_length=20)
    order_list = models.ManyToManyField(Dish, blank=True, related_name='Articles')
    status = 'Cooking'