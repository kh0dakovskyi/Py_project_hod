age = int(input("Введіть вік: "))
def check_age():
    try:
        assert age >= 18, "Вам має бути 18 років або більше"
        print("Ви можете використовувати цей сервіс")
    except AssertionError as e:
        print(e)

check_age()
