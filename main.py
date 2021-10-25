
alphabet = {'a': '1', 'b': '2', 'c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10',
            'k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19',
            't':'20','u':'21','v':'22','x':'23','y':'24','z':'25','A': '26', 'B': '27', 'C':'28',
            'D':'29', 'E':'30','F':'31','G':'32','H':'33','I':'34','J':'35','K':'36','L':'37','M':'38',
            'N':'39','O':'40','P':'41','Q':'42','R':'43','S':'44','T':'45','U':'46','V':'47','X':'48',
            'Y':'49','Z':'50','1':'52','2':'53','3':'54','4':'55','5':'56','6':'57','7':'58',
            '8':'59','9':'60',',':'61','\n':'62','.':'63',':':'64',';':'65','/':'66','?':'67',
            '#':'68','!':'69','@':'70'}
def code_text():
    while True:
        try:
            text = input('Podaj tekst do zaszyfrowania, co najmniej 8 znaków')
            if len(text) > 8:
                for i in text:
                    value = (alphabet[i])
                    klucz = 10
                    new_value = int(value) + klucz
                    if new_value > 70:
                        new_value = new_value - 70
                    for key, value in alphabet.items():
                        if value == str(new_value):
                            print (key, end ='')
                return ''
            else:
                print('Szyfr musi zawirać conajmniej 8 znaków')
        except KeyError:
            return ('Nie znaleziono wartości' + i + ' w słowniku!')

def decode_text(text):
    for i in text:
        value = (alphabet[i])
        klucz = 10
        original_value = int(value) - klucz
        if original_value < 0:
            original_value = 70 + original_value
        for key, value in alphabet.items():
            if value == str(original_value):
                print (key, end ='')
    return ''



#p = (decode_text('DDD'))
#print(p)

print(code_text())
