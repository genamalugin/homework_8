from main import calculate

def test(a,b):
    c = calculate(a,b)

    test_calculate = a+b

    assert c == test_calculate


test(10,20)
test(1,15)
test(40,150)
test('dfdf',150)