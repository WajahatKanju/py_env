from django.urls import path
from .views import AdListView, AdCreateView, AdUpdateView, AdDeleteView, AdDetailView, stream_file, CommentCreateView, CommentDeleteView

app_name = 'ads'

urlpatterns = [
  path('', AdListView.as_view(), name='all'),
  path('ad/create', AdCreateView.as_view(), name='ad_create'),
  path('ad/<int:pk>', AdDetailView.as_view(), name='ad_detail'),
  path('ad/<int:pk>/update', AdUpdateView.as_view(), name='ad_update'),
  path('ad/<int:pk>/delete',AdDeleteView.as_view(), name='ad_delete'),
  path('ad_picture/<int:pk>', stream_file, name='ad_picture'),
  path('ad/<int:pk>/comment', CommentCreateView.as_view(), name='ad_comment_create'),
  path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='ad_comment_delete'),
]