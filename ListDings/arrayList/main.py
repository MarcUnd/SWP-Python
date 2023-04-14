class Array:
    last: int
    array = []

    def __init__(self, *args):
        size_max = max(10, len(args))
        self.size_max = size_max
        self.last = 0
        self.array = [0] * size_max
        self.append(args)

    def append(self, *args):
        self.resize(self.size_max + len(args))
        for a in args:
            if self.last < self.size_max:
                self.array[self.last] = a
                self.last += 1
        else:
            self.resize()
            self.append(a)

    def remove(self, elem):
        index = self.find(elem)
        if index == -1:
            return False

        if index >= self.last or index < 0:
            raise IndexError("List index out of range")

        for i in range(index, self.last - 1):
            self.array[i] = self.array[i + 1]
        self.last -= 1
        return True
    
    def resize(self, size_max = None):
        if size_max is None:
            size_max = self.size_max * 2
        if size_max < 2 * self.size_max:
            size_max = 2 * self.size_max

        self.array = self.array + [0] * (size_max - self.size_max)
        self.size_max = size_max

    def find(self, elem):
        for i in range(self.last):
            if self.array[i] == elem:
                return i
        return -1

    def get(self, index: int):
        if index >= self.last or index < 0:
            raise IndexError("List index out of range")

        return self.array[index]

    def set(self, index: int, elem):
        if index >= self.last or index < 0:
            raise IndexError("List index out of range")

        self.array[index] = elem

    def size(self) -> int:
        return self.last

    def __str__(self) -> str:
        return str(self.array[: self.last])

    def __repr__(self) -> str:
        return f"Array({self.array[: self.last]})"

    def __len__(self) -> int:
        return self.last

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __setitem__(self, index: int, elem):
        self.set(index, elem)



if __name__ == "__main__":
    test = Array(1,2,3,4,9,5)

    print(test)