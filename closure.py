def outer():
    a= 25
    name = "python"
    def inner(prefix):
        print(prefix, name)
    return inner
k = 45
# my_func = outer()
myfunc = outer()
print(myfunc)