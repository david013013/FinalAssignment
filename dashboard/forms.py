from django.forms import ModelForm
from .models import *


class PhotoUploadForm(ModelForm):
    class Meta:
        model = PhotoFeed
        fields = '__all__'