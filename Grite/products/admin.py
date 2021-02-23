from django.contrib import admin
from products.models import Division, Reagent, ReagentsFile


admin.site.register(Division)
admin.site.register(Reagent)
admin.site.register(ReagentsFile)


