from django.contrib import admin
from components.models import (
    Components,
    ComponentsAbout,
)

admin.site.register(Components)
admin.site.register(ComponentsAbout)
