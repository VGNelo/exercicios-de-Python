import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

x = calendar.month(year, month)

print(x)