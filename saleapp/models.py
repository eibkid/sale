from django.db import models
from datetime import datetime, date
from django.utils import timezone

# items to populate the sales_team choice field
sales_team = (
    ('anna', 'Anna'), ('bob', 'Bob'), ('charlene', 'Charlene'), ('david', 'David'),
)

# items to populate the contries choice field
countries = (
    ('united kingdom', 'United Kingdom'), ('france', 'France'), 
    ('germany', 'Germany'), ('netherlands', 'Netherlands'), ('spain','Spain'),
)
# items to populate the fruits choice field
fruits = (
    ('apples','Apples'),  ('pears','Pears'), ('strawberries','Strawberries'), ('bananas', 'Bananas'),
)






class Extract(models.Model):
    created_date = models.DateTimeField(default=timezone.now, null=True)
    Sales_person =  models.CharField(max_length=100, choices=sales_team)
    Customer_name = models.CharField(max_length=100)
    customer_country = models.CharField(max_length=100, choices=countries)
    Desired_fruit = models.CharField(max_length=100, choices=fruits)

    def __str__(self):
        return self.Customer_name


