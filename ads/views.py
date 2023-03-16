from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import  View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
from django.db.models import Q


from .owner import OwnerListView,OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerDetailView
from .models import Ad, Comment, Fav

from .forms import CreateForm, CommentForm

class AdListView(LoginRequiredMixin, View):
  template_name = 'ads/ad_list.html'
  model = Ad

  def get(self, request):
    search = request.GET.get('search')
    if search:
      query = Q(title__icontains=search)
      query.add(Q(text__icontains=search), Q.OR)
      query.add(Q(price__icontains=search), Q.OR)
      query.add(Q(tags__name__in=[search]), Q.OR)
      ads = Ad.objects.filter(query).order_by('-updated_at')

    else:
      ads = Ad.objects.all().order_by('-updated_at')

    favorites = list()
    if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            # rows = Fav.objects.filter(user__id=request.user.id).values('id')
            rows = request.user.favorite_ads.values('id')
            print(rows)
            # favorites = [2, 4, ...] using list comprehension
            favorites = [ row['id'] for row in rows ]
            
    ctx = {'ads': ads, 'favorites': favorites}
    return render(request, self.template_name, ctx)

class AdDetailView(LoginRequiredMixin, View):
  template_name = 'ads/ad_detail.html'
  model = Ad
  context_object_name = "Ad"

  def get(self, request, pk):
    ad = Ad.objects.get(id=pk)
    comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
    comment_form = CommentForm()
    ctx = {'Ad': ad, 'form': comment_form, 'comments': comments}
    return render(request, self.template_name, ctx)

class AdCreateView(LoginRequiredMixin, View):  
  template_name = 'ads/ad_form.html'
  success_url = reverse_lazy('ads:all')


  def get(self, request, pk=None):
    form = CreateForm()
    ctx = {'form': form}
    return render(request, self.template_name, ctx)

  def post(self, request):
    form = CreateForm(request.POST, request.FILES or None)
    if not form.is_valid():
      ctx = {'form': form}
      return render(request, self.template_name, ctx)

    ad = form.save(commit=False)
    ad.owner = self.request.user
    ad.save()
    form.save_m2m()

    return redirect(self.success_url)


class AdUpdateView(LoginRequiredMixin, View):  
  template_name = 'ads/ad_form.html'
  success_url = reverse_lazy('ads:all')


  def get(self, request, pk):
    ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
    form = CreateForm(instance=ad)
    ctx = {'form': form}
    return render(request, self.template_name, ctx)

  def post(self, request, pk=None):
    ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
    form = CreateForm(request.POST, request.FILES or None, instance=ad)
    
    if not form.is_valid():
      ctx = {'form': form}
      return render(request, self.template_name, ctx)

    ad = form.save(commit=False)
    ad.owner = self.request.user
    ad.save()

    return redirect(self.success_url)

class AdDeleteView(OwnerDeleteView):
  model = Ad
  success_url = reverse_lazy('ads:all')

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        ad = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=ad)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])



@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        ad = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad=ad)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        ad = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, ad=ad).delete()
        except Fav.DoesNotExist as e:
            pass

        return HttpResponse()


def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response
