class SelfCount:
    _count = 0
    
    def __init__(self):
        SelfCount._count += 1

    @property
    def count(self) -> int:
        return SelfCount._count
    
    @count.setter
    def count(self, value: int) -> None:
        pass

    @count.deleter
    def count(self):
        pass
    
    def __del__(self):
        SelfCount._count -= 1

a = SelfCount()
print(a.count)
b, c = SelfCount(), SelfCount()
a.count = 100500
print(a.count, b.count, c.count)
del b.count
del b
print(a.count)
