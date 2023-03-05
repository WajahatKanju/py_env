from django.urls import path
from .views import MainView, MainCreate, MainUpdate, MainDelete, MakeView, MakeCreate, MakeUpdate, MakeDelete

app_name = 'autos'

urlpatterns = [
    path('', MainView.as_view(), name='all'),
    path('main/create', MainCreate.as_view(), name='auto_create'),
    path('main/<int:pk>/update/', MainUpdate.as_view(), name='auto_update'),
    path('main/<int:pk>/delete/', MainDelete.as_view(), name='auto_delete'),
    path('lookup/', MakeView.as_view(), name='make_list'),
    path('lookup/create', MakeCreate.as_view(), name='make_create'),
    path('lookup/<int:pk>/update/', MakeUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete/', MakeDelete.as_view(), name='make_delete'),
    ]