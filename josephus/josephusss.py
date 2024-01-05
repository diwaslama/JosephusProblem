# Vanilla solution
a = [1, 2, 3, 4, 5, 6, 7]

index = 0

while len(a) > 1:
    index = (index + 1) % len(a)
    a.pop(index)
    
print(a[0])