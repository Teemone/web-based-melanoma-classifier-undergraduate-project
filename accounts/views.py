from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    template_name = 'signup2.html'
    success_url = reverse_lazy('login')
    form_class = MyUserCreationForm