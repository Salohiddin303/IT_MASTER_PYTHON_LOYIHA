my_dict={'напиток': 'яблочный сок', 'объем': '2 л', 'цена': 250, 'количество': '156'}
print(min(my_dict), max(my_dict))
print(min(my_dict, key=len))