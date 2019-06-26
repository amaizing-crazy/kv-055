# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the
# numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum(list_of_numbers):
     value = 0
     for number in (list_of_numbers):
       value = value + number
     print(value)

def multiply(list_of_numbers):
     value = 1
     for number in (list_of_numbers):
      value = number * value
     print(value)

def en(list_of_numbers):
    value1 = 0
    value2 = 1
    for number in (list_of_numbers):
       value1 = value1 + number
       value2 = value2 * number
    print(value1, value2)

a=[1,2,3,4]
sum(a)
multiply(a)
en(a)
