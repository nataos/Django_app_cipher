from django.test import TestCase
from .forms import PasswordsForm, Passwords
from .views import start

# Create your tests here.
def start_test(request):
    password = Passwords()
    password.text = 'Natalia'
    password.cipher = start(password.text)
    assert password.cipher == 'UhĄhsph'