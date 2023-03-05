from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Auto, Make

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}

        return render(request, 'autos/auto_list.html', ctx)

class MainCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MainUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MainDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# ___________________________________________Make______________________________#


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all()
        ctx = {'make_list': mc}
        return render(request, 'autos/make_list.html', ctx)

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')