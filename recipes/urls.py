from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_home, name='recipes_home'),
    path('breakfast', views.recipes_breakfast, name='recipes-breakfast'),
    path('lunch', views.recipes_lunch, name='recipes-lunch'),
    path('dinner', views.recipes_dinner, name='recipes-dinner'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.RecipesDetailView.as_view(), name='recipes-detail'),
    path('<int:pk>/update', views.RecipesUpdateView.as_view(), name='recipes-update'),
    path('<int:pk>/delete', views.RecipesDeleteView.as_view(), name='recipes-delete'),
    path('search/', views.Search.as_view(), name='search'),
]