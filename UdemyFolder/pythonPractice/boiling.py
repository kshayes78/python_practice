unit = input("What unit are you using?")
temp = int(input("What temperature is the water?"))
if unit == 'f':
    if temp >= 212:
        print("WATER IS BOILING!")
    else: 
        print("WATER IS NOT BOILING!")
elif unit == "c":
    if temp >= 100:
        print("WATER IS BOILING!")
    else: 
        print("WATER IS NOT BOILING! MUST HIT 100C")
elif unit == "k":
    if temp >= 373:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING! MUST HIT 373K")
else:
    print("I don't know those units.")