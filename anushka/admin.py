from django.contrib import admin
from .models import drawing2d3d, printing3d, ProductRendering, Lasercutting, CNCcutting, Sheetmetal, Metalstrture, Furnitureandtoys
# Register your models here.


admin.site.register(drawing2d3d)

admin.site.register(printing3d)

admin.site.register(ProductRendering)

admin.site.register(Lasercutting)

admin.site.register(CNCcutting)

admin.site.register(Sheetmetal)

admin.site.register(Metalstrture)

admin.site.register(Furnitureandtoys)

# admin.site.register(Laserandplasma)