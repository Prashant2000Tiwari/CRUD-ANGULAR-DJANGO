from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list = ('id','name','email','phone','address')
    admin.site.register(User)