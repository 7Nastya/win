class MyClass:

    @staticmethod
    def ex_static_method():
        print("static method")

    @classmethod
    def ex_class_method(cls):
        print("class method")

    def ex_method(self):
        print("method")

#Статический и классовый метод можно вызвать, не создавая экземпляр класса
MyClass.ex_class_method()
MyClass.ex_static_method()
#для вызова ex_method() нужен объект
#MyClass.ex_method()
m = MyClass()
m.ex_method()