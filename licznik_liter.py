import string
# cyfry = "1234567890"
plznaki = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"

def odmiana_liter(n):
    if n == 0:
        return f'{n} liter'
    if n == 1:
        return f'{n} literę'
    if 1 < n < 5:
        return f'{n} litery'
    if n > 4:
        return f'{n} liter'

def odmiana_cyfr(n):
    jedności = n % 10
    if n == 0:
        return f'{n} cyfr'
    if n == 1:
        return f'{n} cyfrę'
    if 11 < n < 15:
        return f'{n} cyfr'
    if 1 < jedności < 5:
        return f'{n} cyfry'
    if n > 4:
        return f'{n} cyfr'

def odmiana_znaków(n):
    if n == 0:
        return f'{n} znaków specjalnych'
    if n == 1:
        return f'{n} znak specjalny'
    if 1 < n < 5:
        return f'{n} znaki specjalne'
    if n > 4:
        return f'{n} znaków specjalnych'

def odmiana_plznaków(n):
    if n == 0:
        return f'{n} polskich znaków'
    if n == 1:
        return f'{n} polski znak'
    if 1 < n < 5:
        return f'{n} polskie znaki'
    if n > 4:
        return f'{n} polskich znaków'

def print_hi(name):
    lista_liter = [znak for znak in name if znak in string.ascii_letters]
    lista_cyfr = [znak for znak in name if znak in string.digits]
    lista_znaków = [znak for znak in name if znak in string.punctuation]
    lista_plznaków = [znak for znak in name if znak in plznaki]
    liczba_liter = odmiana_liter(len(lista_liter))
    liczba_cyfr = odmiana_cyfr(len(lista_cyfr))
    liczba_znaków = odmiana_znaków(len(lista_znaków))
    liczba_plznaków = odmiana_plznaków(len(lista_plznaków))
    print(f'Hej, {name}',
          f'Twoje imie ma {liczba_liter}, {liczba_cyfr}, {liczba_znaków}, {liczba_plznaków}',
          sep="\n")

if __name__ == '__main__':
    print_hi(
        # "Ałeks123!."
        input("Podaj swoje imie\n")
    )
