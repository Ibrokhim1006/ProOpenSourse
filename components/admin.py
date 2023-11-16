from django.contrib import admin
from components.models import (
    Components,
    ComponentsAbout,
    ScretKey,
)

admin.site.register(Components)
admin.site.register(ComponentsAbout)
admin.site.register(ScretKey)
