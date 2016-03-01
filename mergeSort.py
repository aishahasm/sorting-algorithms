"""
Merge Sort:
Input : A => Array of n elements
Output: a sorted permuatation of A
Work = O(n log(n))
"""
def merge(A1, A2):
    n1 = len(A1)
    n2 = len(A2)
    i = 0
    j = 0
    k = 0
    merged = []
    while k  < n1 + n2:
        if i < n1 and j < n2:
            if A1[i] <= A2[j]:
                merged = merged + [A1[i]]
                i = i + 1
            else:
                merged = merged + [A2[j]]
                j = j + 1
        elif i < n1:
            merged = merged + [A1[i]]
            i = i + 1
        else:
            merged = merged + [A2[j]]
            j = j + 1            
        k = k + 1
    return merged
        

def mergeSort(A):
    n = len(A)
    mid = n//2
    if n == 1:
        return A
    elif n == 2:
        if A[0] > A[1]:
            return [A[1]]+[A[0]]
        else:
            return A
    else:
        return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))

A = [3,5,1,3,4,6,5,8,8,2,6,3,7,143,67]
print(mergeSort(A))
