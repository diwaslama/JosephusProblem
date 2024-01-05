# Creating n lists
def createList(a,b):
    return [item for item in range(a, b+1)]
r1, r2 = 1, 1267650600228229401496703205376

# Checking for multiples of two
ass= 0
while ass != 100:
   ass += 1
   two = 2 ** ass
   print(two)

# here i found out is the no.people is a power of 2
# the answer is always 1
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

print(is_power_of_two(1267650600228229401496703205376))
a = createList(r1, r2)
i = 0

while len(a) > 1:
    count = len(a)
    if is_power_of_two(count):
        print(1)
        break
    i = (i + 1) % count
    a.pop(i)

if not is_power_of_two(len(a)):
    print(a[0])
# Checking for powers of two
# i found out that if a number is a power of two the 
# surving slot is always 1 and wanted to test it out
ass= 0
while ass != 100:
   ass += 1
   two = 2 ** ass
   print(two)
a= createList(1,41)
i = 0

# main loop
while len(a) > 1:
    i = (i + 1) % len(a)
    a.pop(i)

# The last slot
print(a[0])