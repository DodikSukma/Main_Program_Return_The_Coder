# includes the pandas library to display the data
import pandas as pd


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
print("================= Return of The Coder =================== \n")


# Create a function to input year data
def input_year():
    year_of_death = int(input("Input Year of Death : "))
    age_of_death = int(input("Input Age of death : "))
    return year_of_death, age_of_death

# Main program
death_data = []

while True:
    year_of_death, age_of_death = input_year()
    n = year_of_death - age_of_death

    sum_suku = sum_fibonacci(n)
    if n < 0:
        print("Death Data is not found ! ")
        print("The data provided is invalid. Please try again.")
        continue
    else:
        # store data in an array
        death_data.append({'Year': n, 'Count Of Death': sum_suku})
        print("Number of Deaths in {} year is: {}".format(n, sum_suku))

    comfirm = str(input("Do you want to input data again? (Y or N):"))
    if comfirm != 'Y':
        break

# Displaying death data using Pandas DataFrame
df = pd.DataFrame(death_data)
print("\nDeath Data in Every Year:")
print(df)

# Calculates the average number of deaths
amount_of_data = len(df)
amount_of_death = df['Count Of Death'].sum()
average_of_death = amount_of_death / amount_of_data
print("\nAverage Number of Deaths : {:.2f}".format(average_of_death))
