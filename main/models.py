from django.db import models
from django.contrib.auth.models import User

class ImageBase(models.Model):
    image = models.ImageField(upload_to = 'media')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    mel_class = models.CharField(max_length=255)
    upload_date = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.uploaded_by.username

