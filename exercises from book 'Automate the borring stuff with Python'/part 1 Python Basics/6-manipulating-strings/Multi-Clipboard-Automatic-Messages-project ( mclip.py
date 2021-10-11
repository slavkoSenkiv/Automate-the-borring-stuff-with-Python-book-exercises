# Step 1: Program Design and Data Structures

#! python3
# mclip.py - A multi-clipboard program

TEXT = {'agree': """Yes, I agree. That sounds fine to me""",
        'busy': """Sorry, can we do this later this week or next week""",
        'upsell': """Would ypu consider making this a monthly donation?"""}

# Step 2: Handle Command Line Arguments

import sys, pyperclip
if len(sys.argv) < 2:
        print('Usage: python mclip.py [keyphrase] - copy phrase text')
        sys.exit()

keyphrase = sys.argv[1]         # first command line arg is the keyphrase

if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Text for ' + keyphrase + ' copied to clip board')
else:
        print('there is no text for ' + keyphrase)

#TODO: make the program to input the desider recepient name inside the desired messege from winR bar for exmp the command will be "mclip Slavko busy" and the output will be "Dear slavko im busy"