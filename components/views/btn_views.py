from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from components.models import (
    Components,
    ComponentsAbout,
)
from components.serializers.btn_serializers import (
    ComponentsSerializers,
    ComponentsAboutSerializers
)


class ComponentsListViews(APIView):
    def get(self, request):
        objects_list = Components.objects.all()
        serializers = ComponentsSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ComponentsButtonViews(APIView):
    def get(self, request, name):
        objects_list = ComponentsAbout.objects.filter(component_id__name=name)
        serializers = ComponentsAboutSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
