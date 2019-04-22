class PriorityQueueBase:
    class Item:
        __slots__ = '_key','_value'

        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __lt__(self,other):
            return self._key < other._key #如果self_.key比other._key小，则返回True,否则，返回False。

        def is_empty(self):
            return len(self) == 0

        def __str__(self):
            return str(self._key)

class HeapPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self,key,value):
        self._data.append(self.Item(key,value))
        self._upheap(len(self._data)-1)

    def min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data[0]
        return (item._key,item._value)
    def remove_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        self._swap(0,len(self._data)-1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key,item._value)

    def _upheap(self,j):
        parent = (j-1)//2
        if j > 0 and self._data[j] < self._data[parent]:
            self._data[j],self._data[parent] = self._data[parent],self._data[j]
            self._upheap(parent)

    def _downheap(self,j):
        if 2*j+1< len(self._data):
            left = 2*j+1
            samll_child = left
            if 2*j+2 < len(self._data): #len(j+1)< len(self._data)
                right = 2*j + 2
                if self._data[right] < self._data[left]:
                    small_child = right
                if self._data[small_child] < self._data[j]:
                    self._data[j],self._data[small_child]=self._data[samll_child],self._data[j]
                    self._downheap(samll_child)
                        
