import licznik_liter


def test():
    assert licznik_liter.odmiana_cyfr(3) == "3 cyfry"

#def test_nieprzechodzący():
    #assert 2+2==5

def test2():
    assert licznik_liter.odmiana_cyfr(23) == "23 cyfry"

def test_12_do_14():
    assert licznik_liter.odmiana_cyfr(12) == "12 cyfr"
    assert licznik_liter.odmiana_cyfr(13) == "13 cyfr"
    assert licznik_liter.odmiana_cyfr(14) == "14 cyfr"