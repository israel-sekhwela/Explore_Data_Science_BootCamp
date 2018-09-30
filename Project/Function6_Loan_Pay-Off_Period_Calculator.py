### START FUNCTION 6

def pay_off_period(PV, PMT, i):

    # YOUR CODE HERE
    n = 0
    interest_rate = 1 + i
    check = PV
    while n < check:

        check = check * (interest_rate) - PMT
        n += 1
    return int(n)

### END FUNCTION 6

print(pay_off_period(1635153, 15000*12, 0.1045) == 30)
print(pay_off_period(1578934, 15000*12, 0.1045) == 25)

