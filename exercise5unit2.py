#Kenrick Tendi
#Exercise 5 unit 2 

x = int(input('pick a number?'))
# from F to C 
def c(x):
    total1 = x - 32 / 1.8 
    print(str(total1))
# from C to F
def f(x):
    total2 = 1.8 * x + 32
    print(str(total2))
opt = input("what do you want to convert to? (Fahrenheit, Celsius)")

if (opt=="Fahrenheit"):
    f(x)

elif (opt=="Celsius"):
    c(x)

