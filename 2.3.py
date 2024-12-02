a, b = map(str, input().split())
violet = ['красный', 'синий']
orange = ['красный', 'желтый']
green = ['синий', 'желтый']
if a in violet and b in violet:
    print('фиолетовый')
elif a in orange and b in orange:
    print('оранжевый')
elif a in green and b in green:
    print('зеленый')
else:
    print('Ошибка')
