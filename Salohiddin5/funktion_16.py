def my_function(x, y, *args,
                kx=15, ky=15, **kwargs):
    print(x, y, args, kx, ky, kwargs)
my_function(7, 8, 8, 3, 4, 1, 8, 9,
                север=15, запад=25, восток=45, юг=10)


