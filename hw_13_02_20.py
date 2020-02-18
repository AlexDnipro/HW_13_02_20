#https://www.codewars.com/kata/58b309e4bffc6b0a09000036
#Simple: Find The Distance Between Two Points

import math
def distance(x1, y1, x2, y2):
    return round( math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

# https://www.codewars.com/kata/587a75dbcaf9670c32000292
# No yelling!

def filter_words(st):
    st = st.lower()
    spisok = st.split()
    character_list = list(spisok[0])
    character_list[0] = character_list[0].upper()
    word = ''.join(character_list)
    spisok[0] = word
    st = ' '.join(spisok)
    return st


#https://www.codewars.com/kata/unfinished-loop-bug-fixing-number-1
#Unfinished Loop - Bug Fixing #1
def create_array(n):
    res=[]
    for i in range(1, n + 1):
        res+=[i]
    return res