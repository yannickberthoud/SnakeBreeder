from django.contrib import admin
from reptiles.models.snake import Family, Dentition, Venom, Snake


class FamilyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    pass

admin.site.register(Family)

class DentitionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dentition)

class VenomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Venom)

class SnakeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identitifcation', {'fields': ['family', 'scientific_name', 'slug', 'sex', 'dentition', 'birth',
                                        'no_longer_own', 'description']}),
        ('Toxicologie', {'fields': ['is_venomous', 'venom']}),
        ('Reproduction', {'fields': ['reproduction', 'reproduced', 'qt_born', 'is_new_birth']}),
        ('Mode de vie', {'fields': ['life_style', 'distribution', 'biotop']}),
        ('Achats, ventes et échanges', {'fields': ['business', 'price']}),
    )

    prepopulated_fields = {'slug': ('scientific_name',)}
    list_editable = ('reproduced', 'no_longer_own', 'qt_born', 'business', 'price',)

    search_fields = ['family', 'dentition', 'venom']
    list_display = ('family', 'scientific_name', 'birth', 'no_longer_own', 'reproduced', 'qt_born',
                    'business', 'price')
    list_filter = ['family', 'dentition', 'biotop', 'reproduction']

admin.site.register(Snake, SnakeAdmin)