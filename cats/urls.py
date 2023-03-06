from .views import CatsList, CatsCreate, CatsUpdate, CatsDelete, BreedList, BreedCreate, BreedUpdate, BreedDelete
from django.urls import path

app_name = 'cats'

urlpatterns = [
  path('', CatsList.as_view(), name='all'),
  path('cats/create/', CatsCreate.as_view(), name='cat_create'),
  path('cats/<int:pk>/update/', CatsUpdate.as_view(), name='cat_update'),
  path('cats/<int:pk>/delete/', CatsDelete.as_view(), name='cat_delete'),

  path('breed', BreedList.as_view(), name='breeds'),
  path('breed/create/', BreedCreate.as_view(), name='breed_create'),
  path('breed/<int:pk>/update/', BreedUpdate.as_view(), name='breed_update'),
  path('breed/<int:pk>/delete/', BreedDelete.as_view(), name='breed_delete'),
  
]