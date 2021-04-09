from django.contrib import admin
from .models import Dictionary, SuperUser, User

# Register your models here.
admin.site.register(Dictionary)
admin.site.register(SuperUser)
admin.site.register(User)
