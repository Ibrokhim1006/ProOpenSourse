from django.urls import path
from components.views import (
    ComponentsListViews,
    ComponentsAboutViews,
    ComponentsCrudViews,
    ComponentsAbudCrudViews,
)

urlpatterns = [
    path('', ComponentsListViews.as_view()),
    path('<int:pk>/', ComponentsCrudViews.as_view()),
    path('<str:name>/', ComponentsAboutViews.as_view()),
    path('about/<int:pk>/', ComponentsAbudCrudViews.as_view()),
]
