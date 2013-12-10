# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.
from twisted.python.zipstream import countFileChunks
from Foundation import MAX

def freq_analysis(message):
    freq_list = countFreq()
    freq_list = calcFreq(freq_list, message)
    freq_list = normalize(freq_list, message)
    return freq_list


def countFreq():
    letters = []
    i = 0 # index to be incremented 
    maxLetters = 26 # 26 letters from a to z
    while i < maxLetters: 
        letters += [0]
        i += 1
        
    return letters


def calcFreq(list, msg):
    # switch to test letter & add 1 if letter is present
    for char in msg: 
        if char == 'a': 
            list[0] += 1 
            break
        if char == 'b':
            list[1] += 1
            break
        if char == 'c':
            list[2] += 1
            break
        if char == 'd':
            list[3] += 1
            break
        if char == 'e':
            list[4] += 1
            break
        if char == 'f':
            list[5] += 1
            break
        if char == 'g':
            list[6] += 1
            break
        if char == 'h':
            list[7] += 1
            break
        if char == 'i':
            list[8] += 1
            break
        if char == 'j':
            list[9] += 1
            break
        if char == 'k':
            list[10] += 1
            break
        if char == 'l':
            list[11] += 1
            break
        if char == 'm':
            list[12] += 1
            break
        if char == 'n':
            list[13] += 1
            break
        if char == 'o':
            list[14] += 1
            break
        if char == 'p':
            list[15] += 1
            break
        if char == 'q':
            list[16] += 1
            break
        if char == 'r':
            list[17] += 1
            break
        if char == 's':
            list[18] += 1
            break
        if char == 't':
            list[19] += 1
            break
        if char == 'u':
            list[20] += 1
            break
        if char == 'v':
            list[21] += 1
            break
        if char == 'w':
            list[22] += 1
            break
        if char == 'x':
            list[23] += 1
            break
        if char == 'y':
            list[24] += 1
            break
        if char == 'z':
            list[25] += 1
        
    return list

def normalize(list, msg):
    numChar = len(msg)
    for letter in list: 
        letter = letter / numChar
    return list


#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]