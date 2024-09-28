class MyCircularDeque:
    def __init__(self, k: int):
        self.circular_que = []
        self.capacity = k
        self.items = 0


    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            temp= self.circular_que
            self.circular_que= []
            self.circular_que.append(value)
            self.circular_que += temp
            self.items+=1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.circular_que.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.circular_que.pop(0)
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.circular_que.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.circular_que[0]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.circular_que[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if not self.circular_que:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.circular_que) == self.capacity:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()