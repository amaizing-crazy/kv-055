#Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(string):
    rstring = ''
    for i in string[::-1]:
#    for i in string[-1:0:-1]:
        rstring = rstring + i
    print(rstring)

reverse("I am testing")




