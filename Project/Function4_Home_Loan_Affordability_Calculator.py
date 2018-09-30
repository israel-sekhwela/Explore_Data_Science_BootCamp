### START FUNCTION 4

def maximum_home_loan(PMT, i, n):

    # YOUR CODE HERE
    interest_rate = (1 + i)
    total_present_value = 0
    for year in range(n):
        year = year + 1
        total_present_value += PMT * (interest_rate ** -year)
    
    PV = round(total_present_value, 2)
    return PV

### END FUNCTION 4
    
print(maximum_home_loan(15000*12, 0.1045, 30) == 1635153.79) #True
print(maximum_home_loan(15000*12, 0.1045, 25) == 1578934.73) #True


