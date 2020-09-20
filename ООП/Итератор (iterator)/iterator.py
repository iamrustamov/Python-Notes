
class SimpleIterator:
    def __init__(self, limit):
        self.max = limit
        self.count = 0

    def __next__(self):
        if self.count < self.max:
            self.count += 1
            return self.count
        else:
            raise StopIteration

    def __iter__(self):
        return self


for x in SimpleIterator(10):
    print(x)
