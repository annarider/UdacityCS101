# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If the first number in the string is greater than or equal 
# to the proceeding number, the proceeding number should be inserted 
# into a sublist. Continue adding to the sublist until the proceeding number 
# is greater than the first number before the sublist. 
# Then add this bigger number to the normal list.

#Hint - "int()" turns a string's element into a number

'''
Pseudo code - brainstorm algorithm
create empty list
add first number to list
check proceeding number
    if it's smaller than or equal to the first num:
    then insert into it's own list
    else if it's bigger than the first number:
    just add it to the list as usual
next number: 
    if smaller than or equal to the first num: 
    insert into same list as sublist
    else if it's bigger than first num: 
    just add to list as usual, not into sublist
continue until no more numbers
'''

def numbers_in_lists(string):
    firstNum = int(string[0])
    nLarge = True
    list = [firstNum]
    sub = []
    i = 1 
    while i < len(string):
        n = int(string[i])
        
        # Proceeding num is greater, therefore add to list
        if firstNum < n :
            list += [n]
            list.append(sub)
        elif nLarge: 
            sub.append(n)
            
        i += 1
    print list
    return list
    
    
#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
