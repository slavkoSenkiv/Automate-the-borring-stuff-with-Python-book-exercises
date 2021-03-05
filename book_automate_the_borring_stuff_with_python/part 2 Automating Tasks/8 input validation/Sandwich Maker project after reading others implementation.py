import pyinputplus as pyip

print('please build your sandwich!')

prices = {  'white' : 2.00,
            'wheat' : 2.50,
            'sour dough' : 3.00,
            'chicken' : 2.50,
            'turkey' : 2.25,
            'ham' : 1.75,
            'tofu' : 4.00,
            'cheddar' : 1.00,
            'swiss' : 1.25,
            'mozzarella' : 2.00,
            'mayo' : 0.25,
            'mustard' : 0.25,
            'lettuce' : 0.30,
            'tomato' : 0.50
            }

additions = ['mayo', 'mustard', 'lettuce', 'tomato']
sandwich = []

sandwich.append(pyip.inputMenu(['white', 'wheat', 'sour dough'], 'chose bread:\n', numbered=True))
sandwich.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 'chose protein:\n', numbered=True))
if pyip.inputYesNo('need cheese? \n') == 'yes':
    sandwich.append(pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], 'chose cheese :\n', numbered=True))
for item in additions:
    if pyip.inputYesNo(f'want {item}?\n') == 'yes':
        sandwich.append(item)
print(sandwich)

howMany = pyip.inputInt('how many sandwiches?\n', min=1)
totalSum = 0

print('your sandwich consists of: ')

for item in sandwich:
    if item in prices.keys():
        print(f'\t{item} = {prices.get(item)}')
        totalSum += prices.get(item)

print(f'the total cost of 1 sandwich is {totalSum} '
      f' and total order cost is {totalSum} * {howMany} = {totalSum*howMany} ')




