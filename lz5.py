# import colorama
#
# print(dir(colorama))

from colorama import init, Fore, Back, Style

init(autoreset=True)  # Щоб кольори автоматично скидалися

print(Fore.RED + "Червоний текст")
print(Back.GREEN + "Текст із зеленим фоном")
print(Style.BRIGHT + "Яскравий текст")
print("Повернення до звичайного стилю")
