class DynamicArray:

    def __init__(self, capacity: int):
        self.arr = [];
        self.capacity = capacity;

    def get(self, i: int) -> int:
        return self.arr[i];

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n;

    def pushback(self, n: int) -> None:
        if (len(self.arr) + 1 > self.capacity):
            self.capacity *= 2;
        self.arr += [n];

    def popback(self) -> int:
        last_item_index = len(self.arr) - 1;
        return self.arr.pop(last_item_index);
        
    def resize(self) -> None:
        self.capacity *= 2;

    def getSize(self) -> int:
        return len(self.arr);
    
    def getCapacity(self) -> int:
        return self.capacity;