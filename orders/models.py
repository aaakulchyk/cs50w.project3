from typing import Tuple, List
from django.db import models

_size = models.CharField(max_length=1, blank=False)  # DRY


class Dish(models.Model):
    class Meta:
        db_table = 'Menu'

    article = models.CharField(max_length=50)
    price = models.IntegerField()   # Store prices in terms of cents.


# Above classes are inherited from <Dish>
class Pizza(Dish):
    class Meta:
        db_table = 'Pizzas'

    mod = models.CharField(max_length=15)
    size = _size


class Topping(Dish):
    class Meta:
        db_table = 'Toppings'


class Sub(Dish):
    class Meta:
        db_table = 'Subs'

    size = _size


class Pasta(Dish):
    class Meta:
        db_table = 'Pasta'


class Salad(Dish):
    class Meta:
        db_table = 'Salads'


class DinnerPlatter(Dish):
    class Meta:
        db_table = 'Dinner Platters'

    size = _size


class Order(models.Model):
    class Meta:
        db_table = 'Orders'

    customer = models.CharField(max_length=20)
    order_list = models.ManyToManyField(Dish, blank=True, related_name='Articles')
    status = 'Cooking'