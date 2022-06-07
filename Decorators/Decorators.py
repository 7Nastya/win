#Передача функции в качестве аргумента
#В Python функции можно передавать и использовать в качестве аргументов, как и любой другой объект.
def say_hello(name):
    return 'Hello, {}!'.format(name)

def be_awesome(name):
    return "Класс, {}, быть вместе так круто!".format(name)

def greet_vanya(greeter_func):
    return greeter_func("Ваня")

#greet_vanya() в качестве аргумента получает другую функцию,
greet_vanya(say_hello)