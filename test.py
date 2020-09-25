mark = int(input("Enter mark: "))

if not isinstance(mark, int):
    print("wrong input")

elif 80 <= mark <= 100:
    print("grade A")

elif 70 <= mark <= 79:
    print("Grade B")

elif 50 <= mark <= 69:
    print("Grade C")

elif 40 <= mark <= 49:
    print("Grade D")

elif 0 <= mark <= 39:
    print("Grade E")

else:
    print("please enter any number between 0 and 100")
