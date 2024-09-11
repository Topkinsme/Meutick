from django.contrib import admin
from .models import Customer,AdminUser,Ticket,Categories,feedback,lostandfound

admin.site.register(Customer)
admin.site.register(AdminUser)
admin.site.register(Ticket)
admin.site.register(Categories)
admin.site.register(feedback)
admin.site.register(lostandfound)