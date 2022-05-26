def squares(start, stop):
    for i in range(start, stop):
        yield i * i

generator = squares(1, 10)