from django.db import models
from datetime import datetime, date


sales_team = (
    ('anna', 'Anna'), ('bob', 'Bob'), ('charlene', 'Charlene'), ('david', 'David'),
)


countries = (
    ('united kingdom', 'United Kingdom'), ('france', 'France'), 
    ('germany', 'Germany'), ('netherlands', 'Netherlands'), ('spain','Spain'),
)

fruits = (
    ('apples','Apples'),  ('pears','Pears'), ('strawberries','Strawberries'), ('bananas', 'Bananas'),
)









class Extract(models.Model):
    date = models.DateTimeField("Today's date(dd/mm/yyyy)", auto_now_add = True)
    Sales_person =  models.CharField(max_length=100, choices=sales_team)
    Customer_name = models.CharField(max_length=100)
    customer_country = models.CharField(max_length=100, choices=countries)
    Desired_fruit = models.CharField(max_length=100, choices=fruits)

    def __str__(self):
        return self.Customer_name


