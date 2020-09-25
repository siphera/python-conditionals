current_speed = int(input("Enter current speed: "))
average_allowed_speed = int(input("enter average allowed speed: "))

calc = current_speed - average_allowed_speed
demerits = calc // 5
print("Points: ", demerits)

if 0 <= demerits <= 12:
    print("OK")

elif demerits > 12:
    print("Time to go to jail")

