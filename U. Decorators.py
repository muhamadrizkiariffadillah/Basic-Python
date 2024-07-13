def response(func):
    def sounds():
        print("Response")
        func()

    return sounds()


@response
def kibo():
    print("Get")


q = kibo
q


# chapter 2
def response_to_approucher(name):
    def inner_func(func):
        def wrapper(*args, **kwargs):
            print(f"A {name} is comming")
            f_response = func(*args, **kwargs)
            return f_response

        return wrapper

    return inner_func
@response_to_approucher("python developer")
def sounds(sound):
    return sound * 3

return_value = sounds("Kibo ")
print(return_value)

