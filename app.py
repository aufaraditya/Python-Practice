'''
----------------------------------------------- Tutorial 1: Input --------------------------------------------------
name = input("What is your name? ")
color = input("What is your favorite color? ")

print(name + " likes " + color)
------------------------------------------------------------------------------------------------------------------
'''

'''
----------------------------------------------- Tutorial 1: Data Type Conversion ----------------------------------
weight_pounds = float(input("What is your weight(in pounds)? "))
weight_kg = str(weight_pounds * 0.453592)
print("Your weight is " + weight_kg + " kg")
------------------------------------------------------------------------------------------------------------------
'''

'''
----------------------------------------------- Tutorial 1: If/Else & Formatted String ----------------------------
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = int(price * 0.1)
else:
    down_payment = int(price * 0.2)
print(f"The Down Payment is  ${down_payment}" ) #Formatted String
------------------------------------------------------------------------------------------------------------------
'''

'''
----------------------------------------------- Tutorial 1: Project Weight Conversion ----------------------------
weight = float(input("Weight: "))
unit = input('L(bs) or (K)g): ').upper()

if unit == 'L':
    weight_conversion = str(weight * 0.453592)
    print(f'You are {weight_conversion} kg')
else:
    weight_conversion = str(weight * 2.20462)
    print(f'You are {weight_conversion} lbs')
------------------------------------------------------------------------------------------------------------------
'''

'''
----------------------------------------------- Tutorial 1: Comparison Operand  ----------------------------------
name = 'is' #Hardcoded
if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name can be maximum of 50 characters')
else:
    print('name looks good')
------------------------------------------------------------------------------------------------------------------
'''

'''
----------------------------------------------- Tutorial 1: Project w/ While Loop  -------------------------------
command = ""
state = 'STOP' #Default State
while command != 'QUIT':
    command = input('> ').upper()
    if command == 'HELP':
        print('''
#start - to start the car
#stop - to stop the car
#quit - to exit
''' )
    elif command == 'START':
        if state == 'STOP':
            print('Car started...Ready to go!')
            state = 'START'
        elif state == 'START':
            print('Car already started!')
    elif command == 'STOP':
        if state == 'START':
            print('Car stopped')
            state = 'STOP'
        elif state == 'STOP':
            print('Car already stopped')
    elif command == 'QUIT':
        break
    else:
        print("I don't understand that")
------------------------------------------------------------------------------------------------------------------
'''

'''
----------------------------------------------- Tutorial 1: For Loop  --------------------------------------------
prices = [10,20,30]
sum = 0
for price in prices:
    sum += price
print(f"Total: {sum}")
------------------------------------------------------------------------------------------------------------------
'''

'''
--------------------------------------------- Challenge: Print 'x' per line according to numbers array -----------
numbers = [5,2,5,2,2]
iteration = 0
for number in numbers:
    output = ''
    for iteration in range(number):
        output += 'x'
    print(output)

--------------------------------------------- Challenge: Alternative ---------------------------------------------
numbers = [5,2,5,2,2]
iteration = 0
for number in numbers:
    output = ''
    while iteration < number:
        output += 'x'
        iteration += 1
    print(output)
    iteration = 0
------------------------------------------------------------------------------------------------------------------
'''

'''
--------------------------------------------- Challenge: Max in List ---------------------------------------------
numbers =  [3,4,99,8,33]
max = numbers[0] 
for number in numbers:
    if number >= max:
        max = number

print(max)
ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt------------------------------------------------------------------------------------------------------------------
'''


