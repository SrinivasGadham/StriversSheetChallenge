import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        heapq.heapify(self.maxheap)
        self.minheap=[]
        heapq.heapify(self.minheap)
        # print(self.maxheap)


        

    def addNum(self, num: int) -> None:
        if len(self.maxheap)==0 or num<=self.maxheap[0]*-1:
            heapq.heappush(self.maxheap,num*-1)
        else:
            heapq.heappush(self.minheap,num)
        if len(self.maxheap)>len(self.minheap)+1:
            a=heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,a*-1)
        elif len(self.maxheap)<len(self.minheap):
            a=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,a*-1)

        

    def findMedian(self) -> float:
        # total_length=+len(self.minheap)
        if len(self.maxheap)!=len(self.minheap):
            return round((self.maxheap[0]*-1),2)
        else:
            return round(((self.maxheap[0]*-1)+self.minheap[0])/2,2)


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()