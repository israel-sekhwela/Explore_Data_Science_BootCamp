### START FUNCTION 3
def retirement_age(PMT, i, FV, start_age):

    # YOUR CODE HERE
    age = 0
    end_age = 0
    interest_rate = 1 + i

    while end_age < FV:
        end_age = PMT + end_age * (interest_rate)
        age = age + 1
        
    age += start_age
    return int(age)

### END FUNCTION 3

print(retirement_age(20000, 0.1, 635339.63, 20) == 35) #true
print (retirement_age(10000, 0.1, 572749.99, 40) == 60) #true