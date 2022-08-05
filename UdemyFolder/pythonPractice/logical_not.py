year = input("What year were you born in?")
if not year.isnumeric():
    year = input("That isn't a valid number. Please enter numeric characters only. What year were you born in?")
year = int(year)
print(f"You were born {2022-year} years ago")