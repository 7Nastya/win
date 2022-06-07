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

#Внутренние функции
def parent():
    print("Привет из функции parent().")

    def first_child():
        print("Привет из функции first_child().")

    def second_child():
        print("Привет из функции second_child().")

    second_child()
    first_child()
parent()
#Возврат функций из функций
#TyT
def son(num):
    def work():
        return  "Get money"
    if num == 1:
        return  work()