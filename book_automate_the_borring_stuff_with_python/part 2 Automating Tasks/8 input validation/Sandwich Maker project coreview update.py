import pyinputplus as pyip
money = 0

print('Welcome, build your sandwich!')

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                       numbered=True,
                       prompt='choose bread: \n')
if bread == 'wheat':
    money += 1
if bread == 'white':
    money += 2
if bread == 'sourdough':
    money += 3
print(money)

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                         numbered=True,
                         prompt='choose protein : \n')
if protein == 'chicken':
    money += 1
if protein == 'turkey':
    money += 2
if protein == 'ham':
    money += 3
if protein == 'tofu':
    money += 4

print(money)
cheese = pyip.inputYesNo(prompt='want cheese?: \n')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'],
                                numbered=True,
                                prompt='which cheese?: \n')
    if cheeseType == 'cheddar':
        money += 1
    if cheeseType == 'swiss':
        money += 2
    if cheeseType == 'mozzarella':
        money += 3
    print(money)
mayo = pyip.inputYesNo('want mayo?: \n')
if mayo == 'yes':
    money += 1
print(money)
mustard = pyip.inputYesNo('want mustard?: \n')
if mustard == 'yes':
    money += 2
print(money)
lettuce = pyip.inputYesNo('want lettuce?: \n')
if lettuce == 'yes':
    money += 3
print(money)
tomato = pyip.inputYesNo('want tomato?: \n')
if tomato == 'yes':
    money += 4
print(money)

howMany = pyip.inputInt(prompt='how many sandwiches?: \n', min=1)
money *= howMany
print(money)


print('your total order cost is $%s' % money)
