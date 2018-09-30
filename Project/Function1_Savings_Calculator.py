### START FUNCTION 1

def savings_calculator(PMT, n, i):

    # YOUR CODE HERE
    interest_rate = 1 + i
    FV = 0
    for year in range(n):
        FV += PMT * (interest_rate ** year)
    # Remember to round your answer to 2 decimal places:
    FV = round(FV, 2)

    return FV

### END FUNCTION 1

print(savings_calculator(20000, 15, 0.1) == 635449.63) #True
print(savings_calculator(10000, 20, 0.1) == 572749.99) #True