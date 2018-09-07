#Binary Addition
#Implement a function that adds two numbers together and returns their sum in binary. 
#The conversion can be done before, or after the addition.
#The binary number returned should be a string.

def add_binary(a,b):
    #your code here
    quo = a + b
    remlist = []
    
    while quo > 0:
        rem = quo % 2
        remlist.append(str(rem))
        quo = quo / 2
        
    remlist.reverse()
    return ''.join(remlist)
