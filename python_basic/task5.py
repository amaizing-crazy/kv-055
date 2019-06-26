#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:

def histogram(list_of_ints):
    for i in list_of_ints:
        j=''
        a='*'
        while i > 0:
            j=j+a
            i=i-1
        print(j)
a=[4, 9, 7]
histogram(a)
