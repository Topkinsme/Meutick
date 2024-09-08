from django.contrib import admin
from .models import Customer,AdminUser,Ticket,Categories

admin.site.register(Customer)
admin.site.register(AdminUser)
admin.site.register(Ticket)
admin.site.register(Categories)