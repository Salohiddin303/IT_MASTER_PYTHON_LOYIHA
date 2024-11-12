import os
my_cwd = os.getcwd()
new_dir = 'Solutions'
path = os.path.join(my_cwd, new_dir)
os.mkdir(path)
print(os.listdir())


