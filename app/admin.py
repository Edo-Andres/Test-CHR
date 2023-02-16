from django.contrib import admin
from .models import BikeSantiago, EstacionBicicletas

# Register your models here.

# class EstacionBicicletasInline(admin.StackedInline):
#     model = EstacionBicicletas
#     extra = 0

# class BikeSantiagoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'city', 'country')
#     inlines = [EstacionBicicletasInline]

# admin.site.register([BikeSantiago], BikeSantiagoAdmin)



class EstacionBicicletasInline(admin.TabularInline):
    model = EstacionBicicletas

class BikeSantiagoAdmin(admin.ModelAdmin):
    inlines = [EstacionBicicletasInline]

admin.site.register(BikeSantiago, BikeSantiagoAdmin)


