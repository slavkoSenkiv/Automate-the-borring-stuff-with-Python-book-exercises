# Step 1: Program Design and Data Structures

#! python3
# mclip.py - A multi-clipboard program

TEXT = {'agree': """Yes, I agree. That sounds fine to me""",
        'busy': """Sorry, can we do this later this week or next week""",
        'upsell': """Would ypu consider making this a monthly donation?"""}

# Step 2: Handle Command Line Arguments

import sys, pyperclip
if len(sys.argv) < 2:   
        print('You need to enter " mclip.py [keyphrase] "  ')
        sys.exit()

keyphrase = sys.argv[1]         # first command line arg is the keyphrase
name = sys.argv[2]

if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase] + ' dear ' + name)
        print('Text for keyphrase " ' + keyphrase + ' " copied to clip board')
else:
        print('there is no text for keyphrase " ' + keyphrase + '"')
