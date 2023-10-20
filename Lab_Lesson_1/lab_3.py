hours = float(input("Hours of work: "))
pay = float(input("Pay per hour: "))
money = hours * pay
if hours > 40:
    money = 40*pay
    money += (hours-40)*pay*1.5


print(f'You are getting paid: {money:.2f}lv')