war = input()

yellow = war.count("Y")
green = war.count("G")
red = war.count("R")

if  (red >=3) or (red>=2 and yellow>=2) or (green==0):
    print("nakhor lite")
else:
    print("rahat baash")