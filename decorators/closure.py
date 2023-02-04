def outer_fun(msg):
    message = msg

    def inner_fun():
        print(message)

    return inner_fun

hi_fun = outer_fun('hi')
hello_fun = outer_fun('hello')
hi_fun()
hello_fun()
