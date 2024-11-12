age = int(input('Сколько тебе лет? '))
if age < 7:
    print('В какой детсад ходишь?')
elif 7 <= age <= 18:
    print('В какой школе учишься?')
elif 18 <= age <= 23:
    print( 'Учишься в ВУЗе?')
elif 60 <= age < 90:
    print( 'Уже не работаешь?')
elif age > 90:
    print ( 'Долгожитель! ')
else:
    print( 'Где работаешь? ')