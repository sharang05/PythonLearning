# Python args and kwargs
def my_function(x, *args, **kwargs):
    print(x, args, kwargs)
    # print(x)

my_function(1, 2, 45, 50, name='John', age=25)
