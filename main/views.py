import imp
from pyexpat import model
from django.shortcuts import render
from main.models import ImageBase
from .forms import ImageForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView

from django.conf import settings

from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
import numpy as np


class HomePageView(TemplateView):
    template_name = 'home.html'

class ProfileView(TemplateView):
    template_name = 'profile2.html'


def image_base_delete_item(request, pk):
    ImageBase.objects.filter(id=pk).delete()

    return render(request, 'profile2.html')




def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def predict(request, pk):
    if request.method == 'POST':
        img = ImageBase.objects.get(pk=pk)

        model = load_model("dl_classifier.h5")
        imagePath = settings.MEDIA_ROOT +"\\media\\"+ img.image.url.split('/')[-1]
        test_image = image.load_img(imagePath, target_size = (64, 64)) 
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)

        #predict the result
        result = model.predict(test_image)
        if request.user.is_authenticated: # Check if the user is logged in
            img.uploaded_by = request.user # Set the uploaded_by field (in models.py) to the current user
        if result[0][0] == 0:
            pred = "This image contains melanoma lesion"
            img.mel_class = 'melanoma'
            img.save()
        else:
            pred = "This image does not contain a melanoma lesion"
            img.mel_class = 'non melanoma'
            img.save()
        return render(request, 'upload.html', {'pred':pred, 'img_obj':img,})

    return render(request, 'upload.html')

# class HistoryView(ListView):
#     template_name = 'history.html'
#     context_object_name = 'img_obj'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in the publisher
#         context['user'] = self.request.user
#         return context
        

    