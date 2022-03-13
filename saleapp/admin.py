from django.contrib import admin

from saleapp.models import Extract
from .models import Extract


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'updated_date', 'Sales_person', 'Customer_name','customer_country', 'Desired_fruit')

admin.site.register(Extract)
