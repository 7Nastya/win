# def even_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 2
#
# ran = even_range(0, 4)
# x = next(ran)
# print(x)
# y = next(ran)
# print(y)
# z = next(ran)
# print(z)

#Можем проверить, что функция прерывается каждый раз после выполнения yield:
# def list_generator(list_obj):
#     for item in list_obj:
#         yield item
#         print('After yieloding {}'.format(item))
#
# generator = list_generator([1, 2])
# next(generator)
# next(generator)
# next(generator)

#генератор accumulator, который
# хранит общее количество данных и в бесконечном цикле получает с помощью оператора
# yield значение
def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

generator = accumulator()

next(generator)
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))