class SlotsClass:
    __slots__ = ('foo', 'bar')

class ChildrenClass(SlotsClass):
    __slots__ = ('zip')
obj = SlotsClass()
obj.foo = 5
child = ChildrenClass()
child.bar = 6
child.zip = 8
# Нельзя добавлять в экземпляры случайные атрибуты
#obj.another = 'Some'
print(obj.__slots__)
print(child.__slots__)
print(child.bar)
#print(obj.__dict__)