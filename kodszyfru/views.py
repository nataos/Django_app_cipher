from django.shortcuts import render, get_object_or_404
from .forms import PasswordsForm
from .models import Passwords
from django.http import HttpResponse
alphabet = {'a': '1','ą':'2', 'b': '3', 'c':'4','ć':'5','d':'6','e':'7','ę':'8','f':'9','g':'10',
            'h':'11','i':'12','j':'13','k':'14','l':'15','ł':'16','m':'17','n':'18','ń':'19','o':'20','ó':'21','p':'22',
            'q':'23','r':'24','s':'25','ś':'26','t':'27','u':'28','v':'29','w':'30','x':'31','y':'32','z':'33','ź':'34','ż':'35',
            'A': '36','Ą':'37', 'B':'38','C':'39','Ć':'40','D':'41', 'E':'42','Ę':'43','F':'44','G':'45',
            'H':'46','I':'47','J':'48','K':'49','L':'50','Ł':'51','M':'52','N':'53','Ń':'54','O':'55',
            'Ó':'56','P':'57','Q':'58','R':'59','S':'60','Ś':'61','T':'62','U':'63','V':'64','W':'65',
            'X':'67','Y':'68','Z':'69','Ź':'70','Ż':'71','1':'72','2':'73','3':'74','4':'75','5':'76',
            '6':'77','7':'78','8':'79','9':'80',',':'81','\n':'82','.':'83',':':'84',';':'85','/':'86','?':'87',
            '#':'88','!':'89',' ':'90','(':'91',')':'92','*':'93','&':'94','^':'95','%':'96','$':'97',
            '<':'98','>':'99','     ':'100'}



def decode_text(request, id):
    password = get_object_or_404(Passwords, pk=id)
    return render(request, 'szyfr.html', {'password': password})


def start(request):
    password_form = PasswordsForm(request.POST or None)
    if password_form.is_valid():
        password = password_form.save()
        result = []
        try:
            for i in password.text:
                value = alphabet[i]
                klucz = 10
                new_value = int(value) + klucz
                if new_value > 100:
                    new_value = new_value - 100
                for key, value in alphabet.items():
                    if value == str(new_value):
                        result.append(key)
            password.cipher = ''.join(result)
            return render(request, 'kod.html', {'result':result, 'password':password})
        except KeyError:
            p = 'Nie znaleziono wartości:    ' + i
            return render(request,'start.html',{'p':p, 'password_form': password_form})


    return render(request, 'start.html', {'password_form': password_form})


