from django.contrib import admin
from reptiles.models.utils import Biotop, Distribution


class BiotopAdmin(admin.ModelAdmin):
    pass

admin.site.register(Biotop, BiotopAdmin)


class DistributionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Distribution)
