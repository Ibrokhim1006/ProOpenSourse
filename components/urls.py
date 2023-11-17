from django.urls import path
from components.views import (
    AboutComponentsViews,
    ComponentsListViews,
    ComponentsAboutViews,
    ComponentsCrudViews,
    ComponentsAbudCrudViews,
)

urlpatterns = [
    path('about_components/', AboutComponentsViews.as_view()),
    path('', ComponentsListViews.as_view()),
    path('<int:pk>/', ComponentsCrudViews.as_view()),
    path('<str:name>/', ComponentsAboutViews.as_view()),
    path('about/<int:pk>/', ComponentsAbudCrudViews.as_view()),
]
