from django import forms
from .models import Ad
from django.core.files.uploadedfile import InMemoryUploadedFile
from .humanize import naturalsize

class CreateForm(forms.ModelForm):
  max_upload_limit = 2 * 1024 * 1024
  max_upload_limit_text = naturalsize(max_upload_limit)

  picture = forms.FileField(required=False, label="file to upload, size <= " + max_upload_limit_text)
  upload_field_name = 'picture'

  class Meta:
    model = Ad
    fields = ['title', 'price', 'text', 'picture']

  def clean(self):
    cleaned_data = super().clean()
    pic = cleaned_data.get('picture')
    if pic is None:
      return 
    if len(pic) > self.max_upload_limit:
      self.add_error('picture', f'File size is greater then f{self.max_upload_limit}')
    
  def save(self, commit=True):
    instance = super(CreateForm, self).save(commit=False)
    file = instance.picture
    if isinstance(file, InMemoryUploadedFile):
      bytearray = file.read()
      instance.content_type = file.content_type
      instance.picture = bytearray
    if commit:
      instance.save()
    return instance

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True, label='Add A New Comment', widget=forms.TextInput(attrs={'class': 'my-2'}))
