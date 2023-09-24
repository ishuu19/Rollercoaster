# RollerCoaster

print("Welcome to the Rollercoaster Ride!")
height =int (input('What is your height?'))

need_to_grow = 120-height

if height >=120:
    print('You are eligible to ride the Rollercoaster!')

    age = int(input("what is your age?"))

    if age < 12:
        bill=5
        print("You need to pay $5 to ride.")
    elif age <=18:
        bill=7
        print("You need to pay $7 to ride.")
    else:
        bill=12
        print("You need to pay $12 to ride.")

    want_photo = input('Do you want to take photos? Y or N')
    if want_photo =='Y':
        bill +=3
    print(f'Your total bill is {bill}')
        
else:
    print(f"You need to grow taller by {need_to_grow} cm!")