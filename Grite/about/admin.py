from django.contrib import admin
from .models import Contacts, Laboratory, Production, Advantages, Company, MainPagePhoto, MainPageDescription


admin.site.register(Contacts)
admin.site.register(Production)
admin.site.register(Laboratory)
admin.site.register(Company)
admin.site.register(Advantages)
admin.site.register(MainPagePhoto)
admin.site.register(MainPageDescription)


