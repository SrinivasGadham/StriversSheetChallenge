def left(k):

    return 2 * k + 1

 



def right(k) -> int:

    return 2 * k + 2

 



def parent(k) -> int:

    return (k - 1) // 2

 



def heapify(heap, k, size):

 

    

    l = left(k)

 

    

    r = right(k)

 

    

    

    smallest = k

    if l < size[0] and heap[l] < heap[k]:

        smallest = l

 

    

    if r < size[0] and heap[r] < heap[smallest]:

        smallest = r

 

    

    

    if smallest != k:

 

        

        heap[k], heap[smallest] = heap[smallest], heap[k]

 

        

        heapify(heap, smallest, size)

 





def insert(heap: [], val: int, size: []):

 

    

    heap[size[0]] = val

 

    

    

    

    i = size[0]

    size[0] += 1

    while i != 0 and heap[parent(i)] > heap[i]:

 

        

        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]

 

        

        i = parent(i)

 

def extractMin(heap: [], size: []) -> int:

    

    if size[0] == 1:

        size[0] -= 1

        return heap[0]

 

    

    val = heap[0]

 

    

    heap[0] = heap[size[0] - 1]

 

    

    size[0] -= 1

 

    

    heapify(heap, 0, size)

    return val

 





def minHeap(n: int, q: [[]]) -> []:

 

    

    size = [0]

    

    heap = [None] * n

 

    

    ans = []

 

    

    for i in range(n):

 

        

        

        if q[i][0] == 0:

            insert(heap, q[i][1], size)

        else:

            ans.append(extractMin(heap, size))

 

    

    return ans