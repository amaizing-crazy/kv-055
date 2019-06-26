#Write a function charFreq() that takes a string and builds a frequency listing of the characters contained in it.
# Represent the frequency listing as a Python dictionary.
# Try it with something like charFreq("abbabcbdbabdbdbabababcbcbab").

#dictionary

def charFreq(stringtotest):
    freq={}
    occurs = 0
    for index, value in enumerate(stringtotest):
        freq[value] = freq.get(value, 0) + 1
        #freq[value]
        #print(value)
        # print(freq[value])
        #freq[number]=
        #freq[value]= freq[value]++
    # for i in freq:
    #     print(i)
    print(freq)
charFreq("abbabcbdbabdbdbabababcbcbab")
