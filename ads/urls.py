from django.urls import path
from .views import AdListView, AdCreateView, AdUpdateView, AdDeleteView

app_name = 'ad'

urlpatterns = [
  path('', AdListView.as_view(), name='all'),
  path('ad/create', AdCreateView.as_view(), name='ad_create'),
  path('ad/<int:pk>/update', AdUpdateView.as_view(), name='ad_update'),
  path('ad/<int:pk>/delete',AdDeleteView.as_view(), name='ad_delete')
]