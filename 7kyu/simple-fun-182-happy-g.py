'''Task:
Let's say that "g" is happy in the given string, if there is another "g" immediately to the right or to the left of it.
Find out if all "g"s in the given string are happy.

Example:
For str = "gg0gg3gg0gg", the output should be true.
For str = "gog", the output should be false.

Input/Output:
[input] string str
A random string of lower case letters, numbers and spaces.
[output] a boolean value
true if all "g"s are happy, false otherwise.'''

#My solution:
def happy_g(st):
    if 'g' not in st:
        return True  # if no 'g', return True

    last_g_index = -2  # initialize to a value that ensures the first 'g' is not considered adjacent
    for i, char in enumerate(st):
        if char == 'g':
            if i - last_g_index > 1:  # If this 'g' is not adjacent to the previous 'g'
                if i == len(st) - 1 or st[i + 1] != 'g':  # if it's the last char or next char is not 'g'
                    return False  # This 'g' is alone
            last_g_index = i  # update the index of the last seen 'g'

    return True