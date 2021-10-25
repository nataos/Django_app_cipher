from django.forms import ModelForm
from .models import Passwords
class PasswordsForm(ModelForm):
    class Meta:
        model = Passwords
        fields = ['text']