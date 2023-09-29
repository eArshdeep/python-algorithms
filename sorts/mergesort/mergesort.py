def mergesort(A):
    if len(A) <= 1:
        return A

    midpoint = len(A) // 2
    L = mergesort(A[:midpoint])
    R = mergesort(A[midpoint:])

    a = 0
    l = 0
    r = 0
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            A[a] = L[l]
            l += 1
        else:
            A[a] = R[r]
            r += 1
        a += 1
    
    while l < len(L):
        A[a] = L[l]
        l += 1
        a += 1
    while r < len(R):
        A[a] = R[r]
        r += 1
        a += 1
    
    return A
