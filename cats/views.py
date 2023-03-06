from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cat, Breed

class CatsList(LoginRequiredMixin, ListView):
  model = Cat

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['cats'] = Cat.objects.all()
    context['breeds'] = Breed.objects.all().count()
    return context

class CatsCreate(LoginRequiredMixin, CreateView):
  model = Cat
  fields = '__all__'
  success_url = reverse_lazy('cats:all')

class CatsUpdate(LoginRequiredMixin, UpdateView):
  model = Cat
  fields = '__all__'
  success_url = reverse_lazy('cats:all')
  
class CatsDelete(LoginRequiredMixin, DeleteView):
  model = Cat
  fields = '__all__'
  success_url = reverse_lazy('cats:all')

# TODO:Create Seprator Line ####################################

class BreedList(LoginRequiredMixin, ListView):
  model = Breed

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['breeds'] = Breed.objects.all()
    return context

class BreedCreate(LoginRequiredMixin, CreateView):
  model = Breed
  fields = '__all__'
  success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
  model = Breed
  fields = '__all__'
  success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
  model = Breed
  fields = '__all__'
  success_url = reverse_lazy('cats:all')

