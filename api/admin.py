from django.contrib import admin

# Register your models here.
from api.models.User import User
from api.models.Phones import Phones

admin.site.register(User)
admin.site.register(Phones)
