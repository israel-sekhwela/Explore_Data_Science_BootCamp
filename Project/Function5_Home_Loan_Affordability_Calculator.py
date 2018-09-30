### START FUNCTION 5

def maximum_home_loan_with_age(PMT, i, start_age):

    # YOUR CODE HERE
    interest_rate = 1 + i
    END_AGE = 65
    age_diff = END_AGE - start_age
    total_present_value = 0

    for year in range(age_diff):
        year = year + 1
        total_present_value += PMT * (interest_rate ** -year)
        
    PV = round(total_present_value, 2)
    return PV

### END FUNCTION 5

print(maximum_home_loan_with_age(15000*12, 0.1045, 35)  == 1635153.79) #true
print(maximum_home_loan_with_age(15000*12, 0.1045, 40) == 1578934.73) #true