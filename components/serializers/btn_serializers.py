from rest_framework import serializers
from components.models import (
    Components,
    ComponentsAbout
)


class ComponentsSerializers(serializers.ModelSerializer):
    """Components Serializers"""

    class Meta:
        """Components Fileds"""

        model = Components
        fields = '__all__'


class ComponentsAboutSerializers(serializers.ModelSerializer):
    """Components Serializers"""
    component_id = ComponentsSerializers(read_only=True)

    class Meta:
        """Components Fileds"""

        model = ComponentsAbout
        fields = '__all__'
