import sys, os

my_cwd = os.getcwd()
new_cwd = r'C:\Users \User\Python \MyData'

try:
    os.chdir(new_cwd)
    print(f'Изменяем рабочую директорию на {os.getcwd()}')
except:
    print(f'Произошла ошибка {sys.exc_info()}')
finally:
    print ('Восстанавливаем рабочую директорию на прежнюю')
    os.chdir(my_cwd)
    print(f'Текущая рабочая директория - {os.getcwd()}')