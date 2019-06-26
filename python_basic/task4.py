#Define a function isPalindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, isPalindrome("radar") should return True.

def isPalindrome(string):
     val =''
     for i in string[::-1]:
       val = val + i
     if val == string:
         print('True', string)
     else:
         print('False', string)

isPalindrome('radar')
isPalindrome('query')


