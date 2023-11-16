from django.urls import path
from components.views.btn_views import (
    ComponentsListViews,
    ComponentsButtonViews
)

urlpatterns = [
    path('', ComponentsListViews.as_view()),
    path('<str:name>/', ComponentsButtonViews.as_view())
]
