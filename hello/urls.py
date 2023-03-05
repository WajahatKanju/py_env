from django.urls import path
from  .views import cookie

urlpatterns = [
    path('', cookie)
    ]