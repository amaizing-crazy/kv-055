#Define a function, which takes a string with N opening brackets ("[") and N closing brackets ("]"),
# in some arbitrary order. Determine whether the generated string is balanced; that is, whether it
# consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.

def brackets(string):
    open=0
    closing=0
    f=0
    if (ord(string[0]) == 93):
        closing = closing + 1
        f = f +1
    else:
        for i in string:
            if closing > open:
                closing = closing + 1
            elif i == '[':
                open = open + 1
                f= f + 1
            else:
                closing = closing +1
                f= f - 1
    if f == 0:
        print('OK')
    else:
        print('NOT OK')

A = '[]'
brackets(A)
A = ']['
brackets(A)
A = '[][]'
brackets(A)
A = '][]['
brackets(A)
A = '[[][]]'
brackets(A)
A = '[]][[]'
brackets(A)



