##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment

def differential():
    year1 = int(input("enter the year!"))
    year2 = int(input("enter second year!"))

    difference = abs(year2 - year1)

    print(f"Year 1: {year1}")
    print(f"Year 2: {year2}")
    print(f"Difference: {difference}")

differential()
#%%
# Second Assignment

def FtoC():
    F = float(input("Enter the current temperature in fahrenheit: "))
    C = (F - 32) * 5/9

    print(f"Fahrenheit: {F}")
    print(f"Celsius: {C:.2f}")
FtoC()

#%%
# Third Assignment

def usdtoeuro():
    EXR = 0.97

    usd = float(input("USD: "))
    euro = usd * EXR

    print(f"USD: {usd}")
    print(f"EURO: {euro:.2f}")

usdtoeuro()



##### ASSIGNMENT ENDS HERE #####
