from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from components.models import (
    Components,
    ComponentsAbout,
    ScretKey,
)
from components.serializers.serializers import (
    ComponentsSerializers,
    ComponentsAboutSerializers,
)


class ComponentsListViews(APIView):
    @extend_schema(
        description="GET components list",
        responses={200: "OK"},
    )
    def get(self, request):
        objects_list = Components.objects.all()
        serializers = ComponentsSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    @extend_schema(
        description="""POST components key \r\n
            https://prounity.uz/api/components/
            {
            name: <str>,
            secret_key: <str>
            }
        """,
        responses={200: "OK"},
    )
    def post(self, request):
        name = request.data["name"]
        secret_key = request.data["secret_key"]
        if name == "" or secret_key == "":
            context = {"No information entered"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        conmponents_ken = Components.objects.filter(name=name)
        if len(conmponents_ken) != 0:
            return JsonResponse(
                {"msg": "There is such a component"}, status=status.HTTP_200_OK
            )
        secret_keys = ScretKey.objects.filter(name=secret_key)
        if len(secret_keys) != 0:
            components = Components(name=name, secret_key=secret_key)
            components.save()
            return JsonResponse({"msg": "susccess"}, status=status.HTTP_200_OK)
        else:
            context = {"Secret Key error"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"msg": "susccess"}, status=status.HTTP_200_OK)


class ComponentsCrudViews(APIView):
    @extend_schema(
        description="""POST component deteile \r\n

            pk: Component id

            https://prounity.uz/api/components/<int: pk>/
        """,
        responses={200: "OK"},
    )
    def get(self, request, pk):
        objects_list = Components.objects.filter(id=pk)
        serializers = ComponentsSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    @extend_schema(
        description="""POST components update  \r\n
            pk: Component id

            https://prounity.uz/api/components/<int: pk>/

            {
            name: <str>,
            secret_key: <str>
            }
        """,
        responses={200: "OK"},
    )
    def put(self, request, pk):
        component_update = Components.objects.filter(id=pk)[0]
        name = request.data["name"]
        secret_key = request.data["secret_key"]
        if name == "" or secret_key == "":
            context = {"No information entered"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        conmponents_ken = Components.objects.filter(name=name)
        if len(conmponents_ken) != 0:
            return JsonResponse(
                {"msg": "There is such a component"}, status=status.HTTP_200_OK
            )
        secret_keys = ScretKey.objects.filter(name=secret_key)
        if len(secret_keys) != 0:
            component_update.name = name
            component_update.secret_key = secret_key
            component_update.save()
            return JsonResponse({"msg": "susccess"}, status=status.HTTP_200_OK)
        else:
            context = {"Secret Key error"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"msg": "susccess"}, status=status.HTTP_200_OK)

    @extend_schema(
        description="""POST components delete  \r\n
            pk: Component id

            https://prounity.uz/api/components/<int: pk>/

            {
            secret_key: <str>
            }
        """,
        responses={200: "OK"},
    )
    def delete(self, request, pk):
        component_delete = Components.objects.filter(id=pk)[0]
        secret_key = request.data["secret_key"]
        if secret_key == "":
            context = {"No information entered"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        secret_keys = ScretKey.objects.filter(name=secret_key)
        if len(secret_keys) != 0:
            component_delete.delete()
            return JsonResponse({"msg": "Delete susccess"}, status=status.HTTP_200_OK)
        else:
            context = {"Secret Key error"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"msg": "Delete susccess"}, status=status.HTTP_200_OK)


# Component About
class ComponentsAboutViews(APIView):
    @extend_schema(
        description="""GET the component by name \r\n
        component name: button,  card
        https://prounity.uz/api/components/<str: component name>/
        https://prounity.uz/api/components/button/
        """,
        responses={200: "OK"},
    )
    def get(self, request, name):
        n = name.capitalize()
        objects_list = ComponentsAbout.objects.filter(component_id__name=n)
        serializers = ComponentsAboutSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ComponentsAbudCrudViews(APIView):
    @extend_schema(
        description="""POST component about deteile \r\n

            pk: Component about id

            https://prounity.uz/api/components/about/<int: pk>/
        """,
        responses={200: "OK"},
    )
    def get(self, request, pk):
        objects_list = ComponentsAbout.objects.filter(id=pk)
        serializers = ComponentsAboutSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    @extend_schema(
        description="""POST components about update  \r\n
            pk: Component about id

            https://prounity.uz/api/components/about/<int: pk>/

            {
            name: <str>,
            secret_key: <str>
            }
        """,
        responses={200: "OK"},
    )
    def put(self, request, pk):
        component_update = ComponentsAbout.objects.filter(id=pk)[0]
        title = request.data["title"]
        content = request.data["content"]
        img = request.data["img"]
        component_id = request.data["component_id"]
        files = request.data["files"]
        secret_key = request.data["secret_key"]
        if title == "" or content == "" or component_id == "" or secret_key == "":
            context = {"No information entered"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        secret_keys = ScretKey.objects.filter(name=secret_key)
        if len(secret_keys) != 0:
            component_update.title = title
            component_update.content = content
            component_update.img = img
            component_update.files = files
            component_update.secret_key = secret_key
            component_update.save()
            return JsonResponse({"msg": "Update susccess"}, status=status.HTTP_200_OK)
        else:
            context = {"Secret Key error"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"msg": "susccess"}, status=status.HTTP_200_OK)

    @extend_schema(
        description="""POST components about Delete  \r\n
            pk: Component about id

            https://prounity.uz/api/components/about/<int: pk>/

            {
            secret_key: <str>
            }
        """,
        responses={200: "OK"},
    )
    def delete(self, request, pk):
        component_delete = ComponentsAbout.objects.filter(id=pk)[0]
        secret_key = request.data["secret_key"]
        if secret_key == "":
            context = {"No information entered"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        secret_keys = ScretKey.objects.filter(name=secret_key)
        if len(secret_keys) != 0:
            component_delete.delete()
            return JsonResponse({"msg": "Delete susccess"}, status=status.HTTP_200_OK)
        else:
            context = {"Secret Key error"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"msg": "Delete susccess"}, status=status.HTTP_200_OK)


# class AboutComonent(APIView):
#     @extend_schema(
#         description="""GET the component by name \r\n
#         component name: button,  card
#         https://prounity.uz/api/components/<str: component name>/
#         https://prounity.uz/api/components/button/
#         """,
#         responses={200: "OK"},
#     )
#     def get(self, request):
#         objects_list = ComponentsAbout.objects.all()
#         serializers = ComponentsAboutSerializers(objects_list, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     @extend_schema(
#         description="""POST components about key \r\n
#             https://prounity.uz/api/components/component_about/
#             {
#             "title": <str>,
#             "content": <str>,
#             "img": Image File (JPG, PNG),
#             "files": Files (DOC, PDF, EXCEL, TXT)
#             "component_id": <int: id>, Component ID,
#             "secret_key": <str>
#             }
#         """,
#         responses={200: "OK"},
#     )
#     def post(self, request, format=None):
#         title = request.data.get("title")
#         content = request.data.get("content")
#         img = request.data.get("img")
#         component_id = request.data.get("component_id")
#         files = request.data.get("files")
#         secret_key = request.data.get("secret_key")

#         if title == "" or content == "" or component_id is None or secret_key == "":
#             context = {"No information entered"}
#             return Response(context, status=status.HTTP_400_BAD_REQUEST)
#         secret_keys = ScretKey.objects.filter(name=secret_key)
#         if secret_keys.exists():
#             components = ComponentsAbout(
#                 title=title,
#                 content=content,
#                 img=img,
#                 files=files,
#                 component_id=component_id,
#                 secret_key=secret_key,
#             )
#             components.save()

#             return JsonResponse({"msg": "success"}, status=status.HTTP_200_OK)
#         else:
#             context = {"Secret Key error"}
#             return Response(context, status=status.HTTP_400_BAD_REQUEST)


class AboutComponentsViews(APIView):
    def get(self, request):
        print(1)
        print(1)
        return Response(status=status.HTTP_200_OK)
