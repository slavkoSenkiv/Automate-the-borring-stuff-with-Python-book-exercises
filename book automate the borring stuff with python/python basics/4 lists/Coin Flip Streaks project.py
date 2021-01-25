"""
For this exercise, we’ll try doing an experiment. If you flip a coin 100 times
and write down an “H” for each heads and “T” for each tails, you’ll create
a list that looks like “T T T T H H H H T T.” If you ask a human to make
up 100 random coin flips, you’ll probably end up with alternating headtail
results like “H T H T H H T H T T,” which looks random (to humans),
but isn’t mathematically random. A human will almost never write down
a streak of six heads or six tails in a row, even though it is highly likely
to happen in truly random coin flips. Humans are predictably bad at
being random.

Write a program to find out how often a streak of six heads or a streak
of six tails comes up in a randomly generated list of heads and tails. Your
program breaks up the experiment into two parts: the first part generates
a list of randomly selected 'heads' and 'tails' values, and the second part
checks if there is a streak in it. Put all of this code in a loop that repeats the
experiment 10,000 times so we can find out what percentage of the coin
flips contains a streak of six heads or tails in a row.

Of course, this is only an estimate, but 10,000 is a decent sample size.
Some knowledge of mathematics could give you the exact answer and save
you the trouble of writing a program, but programmers are notoriously
bad at math.

"""
import random
lineOfFlips = []
times = 10000

for i in range(times):
    defineSide = random.randint(0, 1)
    if defineSide == 0:
        coinSide = 'T'
    else:
        coinSide = 'H'
    lineOfFlips.append(coinSide)

print(lineOfFlips)


caseH = 0
caseT = 0
for i in range(times - 5):

    if lineOfFlips[i] == 'H' and lineOfFlips[i + 1] == 'H' and lineOfFlips[i + 2] == 'H' \
            and lineOfFlips[i + 3] == 'H' and lineOfFlips[i + 4] == 'H' and lineOfFlips[i + 5] == 'H':
        caseH += 1
    elif lineOfFlips[i] == 'T' and lineOfFlips[i + 1] == 'T' and lineOfFlips[i + 2] == 'T' \
            and lineOfFlips[i + 3] == 'T' and lineOfFlips[i + 4] == 'T' and lineOfFlips[i + 5] == 'T':
        caseT += 1

print('there are ' + str(caseH) + ' H cases. and ' + str(caseT) + ' T cases')







