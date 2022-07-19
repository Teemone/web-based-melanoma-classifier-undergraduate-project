from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class":"form-control"
        })
        self.fields["email"].widget.attrs.update({
            "class":"form-control"
        })
        self.fields["password1"].widget.attrs.update({
            "class":"form-control"
        })
        self.fields["password2"].widget.attrs.update({
            "class":"form-control"
        })

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)