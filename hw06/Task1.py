class ChainIterator:
    def __init__(self, begin, end, *args):
        self.begin = begin
        self.end = end
        self.seq = list(*args)
        self.counter = 0

    def __next__(self):
        if self.counter < len(self.seq):
            self.counter += 1
            return " ".join(map(str, self.seq[self.counter - 1][self.begin:self.end]))
        else:
            raise StopIteration

    def __iter__(self):
        return self

def chainslice(begin, end, *args):
    print(*args)
    return ChainIterator(begin, end, [*args])

chainIterator = chainslice(1, 2, [1, 2, 3, 4], [5, 7, 8])
for i in chainIterator:
    print(i)
chainIterator = chainslice(1, 4, [1, 2, 3, 4], [5, 7, 8], [0, 8, 6, 5])
for i in chainIterator:
    print(i)
chainIterator = chainslice(-2, -1, [1, 2, 3, 4], [5, 7, 8])
for i in chainIterator:
    print(i)
chainIterator = chainslice(-2, 5, [1, 2, 3, 4], [5, 7, 8])
for i in chainIterator:
    print(i)
chainIterator = chainslice(-1, -3, [2, 3])
for i in chainIterator:
    print(i)  
   