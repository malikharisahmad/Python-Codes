def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + 1 + j]
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def M_S(A,p,r):
    if p<r:
        q=(p+r)//2
        M_S(A,p,q)
        M_S(A,q+1,r)
        Merge(A,p,q,r)

def main():
    arr = [5,0,3,9,1,7,2,8]
    print("Original array:", arr)
    M_S(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
main()


