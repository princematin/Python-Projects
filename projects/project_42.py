class Reverse:
    def __init__(self, ls):
        self.ls = ls
        self.index = len(ls)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        
        self.index -= 1
        return self.ls[self.index]



ls = [10, 20, 30]

print("Reverse iteration")
for it in Reverse(ls):
    print(it)

print("Original list:")
print(ls)
