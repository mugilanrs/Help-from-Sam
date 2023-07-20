def helpsam(a):
    count, i = 1,1
    while (i<a):
        i *=2
        if (a==i):
            return count
        if (i>a):
            i/=2
            b = a-int(i)
            return (count+b)

print(helpsam(int(input())))


