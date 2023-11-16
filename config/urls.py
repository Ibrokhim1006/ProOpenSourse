from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView

urlpatterns = [
    path("api/components/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/components/admin/", admin.site.urls),
    path(
        "api/components/docs/",
        TemplateView.as_view(
            template_name="doc.html", extra_context={"schema_url": "api_schema"}
        ),
        name="swagger-ui",
    ),
    path("api/components/", include("components.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
