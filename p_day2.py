#  ## for any percntage we do
# digit%=digit/100=ans
print("welcome to the tip calculater")
total=float(input("enter the total price of the bill?\n"))
tip=int(input("how much tip would you like to give?\n"))
ans=tip/100*total
total+=ans
print(f"total amount with tip is = {total}")
people=int(input("how many person will split bill\n"))
split=total/people
print(f"Each person should pay = {round(split,2)}")
