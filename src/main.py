from usReader import Country
from stateReader import State
from countyReader import County

print("Which dataset are you interested in?")
print("For country level COVID-19 data, enter 1")
print("For state level COVID-19 data, enter 2")
print("For county level COVID-19 data, enter 3")

val = input("Enter your value: ") 

if val == "1":
    C = Country("/data/us.csv")
    C.read()
elif val == "2":
    S = State("/data/us-states.csv")
    S.read()
elif val == "3":
    C2 = County("/data/us-counties.csv")
    C2.read()
else:
    print("Your input is not valid. Program end.")
    








