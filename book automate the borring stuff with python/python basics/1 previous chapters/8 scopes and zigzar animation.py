

"""
zigzag right arrow my version

lines = 0
space = ' '
while lines <= 10:
    print(space * lines +'****' + ' № of lines = ' + str(lines))
    lines = lines + 1

while lines <= 20:
    print(space * lines + '****'+ ' № of lines = '+ str(lines))
    lines = lines - 1
    if lines <= -1:
        break

result
**** № of lines = 0
 **** № of lines = 1
  **** № of lines = 2
   **** № of lines = 3
    **** № of lines = 4
     **** № of lines = 5
      **** № of lines = 6
       **** № of lines = 7
        **** № of lines = 8
         **** № of lines = 9
          **** № of lines = 10
           **** № of lines = 11
          **** № of lines = 10
         **** № of lines = 9
        **** № of lines = 8
       **** № of lines = 7
      **** № of lines = 6
     **** № of lines = 5
    **** № of lines = 4
   **** № of lines = 3
  **** № of lines = 2
 **** № of lines = 1
**** № of lines = 0

zigzag left arrow my version



result
          **** № of lines = 10
         **** № of lines = 9
        **** № of lines = 8
       **** № of lines = 7
      **** № of lines = 6
     **** № of lines = 5
    **** № of lines = 4
   **** № of lines = 3
  **** № of lines = 2
 **** № of lines = 1
**** № of lines = 0
 **** № of lines = 1
  **** № of lines = 2
   **** № of lines = 3
    **** № of lines = 4
     **** № of lines = 5
      **** № of lines = 6
       **** № of lines = 7
        **** № of lines = 8
         **** № of lines = 9
          **** № of lines = 10

long zigzag my version
y = 100
def x():
    lines = 10
    space = ' '
    while lines >= 0:
        print(space * lines + '****' + ' № of lines = ' + str(lines) + ' y right now is ' + str(y))
        lines = lines - 1
        if lines <= 0:
            break

    while lines <= 10:
        print(space * lines + '****' + ' № of lines = ' + str(lines) + ' y right now is ' + str(y))
        lines = lines + 1
        if lines >= 11:
            break

while y >= 0:
    x()
    y = y - 1
"""
import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: #the main program loop
        print(' ' * indent, end='')
        print('****')
        time.sleep(0.1) #pause for 1/10 of a second

        if indentIncreasing:
            # increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False

        else:
            #decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()

