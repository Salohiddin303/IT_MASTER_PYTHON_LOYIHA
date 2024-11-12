def my_function (**countries):
    print(f'Самая густонаселенная страна -'
          f' {max(countries, key=countries.get)}'
          f'{max (countries.values())}'
          f'чел/км2, \п самая малонаселенная -'
          f'{min(countries, key=countries.get)}'
          f'{min(countries.values())} чел/км2')
my_function(Мальта=1432, Дания=128,
            Монако=18679, Индия=357, Монголия=2)



