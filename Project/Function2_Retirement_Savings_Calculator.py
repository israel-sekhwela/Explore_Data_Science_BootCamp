### START FUNCTION 2

def retirement_savings(PMT, i, start_age, end_age):

    # YOUR CODE HERE
    interest_rate = 1 + i
    age_diff = end_age - start_age
    FV = 0
    for year in range(age_diff):
        FV += PMT * (interest_rate ** year)
        
    # Remember to round your answer to 2 decimal places:
    FV = round(FV, 2)

    return FV

### END FUNCTION 2

print (retirement_savings(20000, 0.1, 20, 35) == 635449.63) #true
print (retirement_savings(10000, 0.1, 40, 60) == 572749.99) #true
