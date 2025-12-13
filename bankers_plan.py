# validate whether a banker's plan is right or wrong

# variables:
## f: deposit
## p: interest rate
## c: withdrawl
## n: years
## i: interest rate

# build a function "fortune" that returns TRUE if John can make a living until the nth year and FALSE if not

def fortune(f, p, c, n, i):
    for _ in range(n):
        # fortune earns interest, then withdrawl
        f = f + (p/100) * f - c

        if f < 0:
            return False
        
        # withrawl increases for next year
        c = c + (i/100) * c

    return True

    

# function call
print(fortune(10000, 1, 2000, 15, 1))
print(fortune(100000, 1, 10000, 10, 1))
print(fortune(100000, 1, 9185, 12, 1))




