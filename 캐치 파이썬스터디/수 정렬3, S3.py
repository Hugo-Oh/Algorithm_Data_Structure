import sys
sys.stdin = open("input.txt", "rt")
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

"""
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1
    swap(x, pivot_idx, rmark)
    return rmark

def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)
    _qsort(x, 0, len(x)-1)

quickSort(arr)
print(arr)"""

def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]

mergeSort(arr)

for i in arr:
    print(i)