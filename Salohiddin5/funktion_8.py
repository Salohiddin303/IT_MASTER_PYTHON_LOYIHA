def my_function(name, last_name, occupation, age):
    print(f'Ishchi #1 - {name} {last_name} {occupation} {age}')

info1, info2, info3, info4 = 'Alijon', 'Jalilov', 'programmist', 30
my_function(info1, info2, info3, info4)
my_function(info2, info3, info1, info4)
my_function(info4, info1, info2, info3)


