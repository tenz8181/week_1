##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''
# Input for the two years
year1 = int(input('Please enter the first year: '))
year2 = int(input('Please enter the second year: '))

# Calculate the difference between the two years
difference = abs(year2 - year1)

# Display the results
print(f'Year 1: {year1}')
print(f'Year 2: {year2}')
print(f'Difference: {difference}')


#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''
# Input temperature in Fahrenheit
fahrenheit = float(input('Please enter the temperature in Fahrenheit: '))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Display the results
print(f'Fahrenheit: {fahrenheit}')
print(f'Celsius: {celsius:.2f}')


#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''
# Input amount in US Dollars
usd = float(input('Please enter the amount in US Dollars: '))

# Exchange rate from USD to Euro
exchange_rate = 0.97

# Convert USD to Euro
euros = usd * exchange_rate

# Display the results
print(f'USD: {usd}')
print(f'EU: {euros:.2f}')


##### ASSIGNMENT ENDS HERE #####
