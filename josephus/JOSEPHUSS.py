# Since we know the answer if the number is
# a return of power of two this checks it
# straight out the bat
def is_power_of_two(n):
    return (n & (n - 1)) == 0

# and if the number is not a power of two
# Every round makes the circle half. Getting 2^m
# after 2^m makes the circle as small as it can
# calculate the leftover people n
# We double the leftover poeple and add one
# to account that every second person is eliminated 
# we start our count from 1
def last_remaining(n):
    if is_power_of_two(n):
        return 1
    else:
        m = 1
        while 2 ** m < n:
            m += 1
        m -= 1
        
        return 2 * (n - 2 ** m) + 1

n = 410000000000000000000000
print(last_remaining(n))
