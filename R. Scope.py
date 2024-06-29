# local scope

def my_func():
    x = 300
    print(x)


my_func()


# nested function

def my_func2():
    x = 300

    def my_func3():
        print(x)

    my_func3()


my_func2()

# global scope
x = 200


def func():
    print(x)


func()


# Global keyword

def user():
    global name
    name = "Kibo"


user()
print(name)

# nonlocal keyword is used to work variables inside nested func

def func1():
    x = "Rizki"
    def func2():
        nonlocal x
        x = "Kibo"
    func2()
    return x
print(func1())