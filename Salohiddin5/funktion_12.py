def my_function(**kwargs):
    print(f'Самый легкий металл -'
          f'{min(kwargs, key=kwargs.get)}'
          f'{min(kwargs.values())}, \n'
          f'самый тяжелый -'
          f'{max(kwargs, key=kwargs.get)}'
          f'{max(kwargs.values())}')
my_function(осмий=22.61, цинк=7.1, золото=19.3,
           ртуть=13.6, олово=7.3)



