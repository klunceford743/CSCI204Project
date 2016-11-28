class HeapSort:

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def maxSort(self, nums, n):
        i = len(nums)//2
        self.size = len(nums)
        self.heap = [0] + nums
        while i > 0:
            self.maxMoveUp(i)
            i = i - 1

        y = []
        x = 0
        while self.heap != [0] and x < n:
            y.append(maxHeapRemove(self.heap))
            x += 1

        return y

    def maxMoveUp(self, i):
        while i * 2 <= self.size:
            m = self.maxChild(i)
            if self.heap[i][1] < self.heap[m][1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[m]
                self.heap[m] = temp
            i = m

    def maxChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i*2][1] > self.heap[i*2+1][1]:
            return i * 2
        return i* 2 + 1

    
    def minSort(self, nums, n):
        i = len(nums)//2
        self.size = len(nums)
        self.heap = [0] + nums
        while i > 0:
            self.minMoveUp(i)
            i = i - 1

        y = []
        x = 0
        while self.heap != [0] and x < n:
            y.append(minHeapRemove(self.heap))
            x += 1

        return y

    def minMoveUp(self, i):
        while i * 2 <= self.size:
            m = self.minChild(i)
            if self.heap[i][1] > self.heap[m][1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[m]
                self.heap[m] = temp
            i = m

    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i*2][1] < self.heap[i*2+1][1]:
            return i * 2
        return i* 2 + 1

def maxHeapRemove(heap):
    top = heap[len(heap)-1]
    m = heap[1]
    heap[1] = top
    heap.pop()
    maxFixdown(heap, 1)
    return m


def maxFixdown(heap, ind):
    l = leftChildOne(heap, ind)
    r = rightChildOne(heap,ind)
    if l == None:
        return
    if r == None:
        if heap[ind][1] < heap[l][1]:
            temp = heap[l]
            heap[l] = heap[ind]
            heap[ind] = temp
        return
    if heap[ind][1] < max(heap[l][1], heap[r][1]):
        if heap[l][1] >= heap[r][1]:
            temp = heap[l]
            heap[l] = heap[ind]
            heap[ind] = temp
            maxFixdown(heap, l)
        else:
            temp = heap[r]
            heap[r] = heap[ind]
            heap[ind] = temp
            maxFixdown(heap,r)

def minHeapRemove(heap):
    top = heap[len(heap)-1]
    m = heap[1]
    heap[1] = top
    heap.pop()
    minFixdown(heap, 1)
    return m


def minFixdown(heap, ind):
    l = leftChildOne(heap, ind)
    r = rightChildOne(heap,ind)
    if l == None:
        return
    if r == None:
        if heap[ind][1] > heap[l][1]:
            temp = heap[l]
            heap[l] = heap[ind]
            heap[ind] = temp
        return
    if heap[ind][1] > min(heap[l][1], heap[r][1]):
        if heap[l][1] <= heap[r][1]:
            temp = heap[l]
            heap[l] = heap[ind]
            heap[ind] = temp
            minFixdown(heap, l)
        else:
            temp = heap[r]
            heap[r] = heap[ind]
            heap[ind] = temp
            minFixdown(heap,r)

def leftChildOne(tree, index):
    child = index*2
    if child >= len(tree):
        return None
    return child

def rightChildOne(tree, index):
    child = index*2 + 1
    if child >= len(tree):
        return None
    return child
