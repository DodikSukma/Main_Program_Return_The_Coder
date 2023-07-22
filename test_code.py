# Create a function to determine Fibbonacy numbers
def fibonacci(n):
    if n <= 0:
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        fib_prev_prev = 1
        fib_prev = 1
        fib_current = 0
        for i in range(3, n + 1):
            fib_current = fib_prev + fib_prev_prev
            fib_prev_prev = fib_prev
            fib_prev = fib_current
        return fib_current

# create a function to determine the number of the nth term of a fibbonacy number
def sum_fibonacci(n):
    sum_fib = 0
    for i in range(1, n + 1):
        sum_fib += fibonacci(i)
    return sum_fib

# Creaet a header of Program
print("================= Return of The Coder Testing =================== \n")


# Create a deklar data

year_of_death = 17
age_of_death = 13

n = year_of_death - age_of_death 

sum_suku = sum_fibonacci(n)

print("Number of Deaths in {} year is: {}".format(n, sum_suku))