def powerset(a,lst):
    if len(a)==0:
        print(lst)

    else:
        powerset(a[1:],lst)
        powerset(a[1:],lst+[a[0]])
a=[1,4,6,9]
powerset(a,[])