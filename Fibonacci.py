def A(n):
    if n<=1:
        return n
    else:
        return A(n-1)+ A(n-2)

a = 6
for i in range(a):
    print(A(i), end=" ")
