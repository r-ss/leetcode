# Sorting algorthythm
# from book by Thomas H. Cormen - Algorithms

a = [8,4,29,56,1,7,9,100]

for index, item in enumerate(a):
    key = a[index]
    z = index - 1
    while z >= 0 and a[z] > key:
        a[z + 1] = a[z]
        z = z - 1
    a[z + 1] = key

print(a)