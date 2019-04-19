class MinStack:
    def __inti__(self):
        """initialize your data structure here.
        """
        self.a = []

    def push(self,x:int) -> None:
        self.a.append(x)

    def pop(self)->None:
        self.a = self.a[:-1]
        
    def top(self) ->int:
        return self.a[-1]

    def getMin(self) -> int:
        return min(self.a)
        
