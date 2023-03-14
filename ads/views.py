from django.urls import reverse_lazy

from .owner import OwnerListView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Ad


class AdListView(OwnerListView):
  model = Ad


class AdCreateView(OwnerCreateView):
  model = Ad
  fields = ['title', 'price', 'text']
  success_url = reverse_lazy('ad:all')

class AdUpdateView(OwnerUpdateView):
  model = Ad
  fields = ['title', 'price', 'text']

class AdDeleteView(OwnerDeleteView):
  model = Ad
  success_url = reverse_lazy('ad:all')