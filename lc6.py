mas = ["larasa", "Erik", "Pupik", "Adam", "Ivan"]

while True:
    inp = input("Введіть індекс або exit для виходу з цикла: ")
    if inp == "exit":
        break

    try:
        i = int(inp)

        if 0 <= i <= len(mas):
            print(mas[i])
        else:
            print("ти тупе")
    except IndexError:
        print("Такого індекса не існує")