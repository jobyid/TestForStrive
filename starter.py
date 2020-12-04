#Starter file for the code
print("Hello code Strive")
print(" Hellow git hub")
for x in range(1,6):
    print("How many commits {}".format(x))
#day 4 exercise 5.3
# Print multiplication table
import pandas as pd
from IPython.display import display
#i imported pands to get a nice data fram then display to make it look nice

def dataForTable(n):
    #worked out the data in this function
    d = dict()
    h = []
    for x in range(1,n+1):
        l = []
        h.append(x)
        for y in range(1,n+1):
            l.append(y*x)
        d[x] = l

    print_multiplication_table(d,h)

def print_multiplication_table(d,h):
    #Displayed the data in this function
    display(pd.DataFrame(d, h, h))

dataForTable(10)
