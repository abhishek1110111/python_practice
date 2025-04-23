def find_Prime(number): # Function to find prime numbers and their factors
    if number <= 1:
        return False, [1, number]
    factors = [1, number]  
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    if len(factors) == 2: 
        return f'It is Prime Number'
    else:
        return f'IT is Not Prime Number and Factor of this number is: {sorted(factors)}'
