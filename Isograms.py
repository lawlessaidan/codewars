#An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
#Implement a function that determines whether a string that contains only letters is an isogram. 
#Assume the empty string is an isogram. Ignore letter case.
#is_isogram("Dermatoglyphics" ) == true
#is_isogram("aba" ) == false
#is_isogram("moOse" ) == false # -- ignore letter case

def is_isogram(string):
    string = string.lower()
    string = list(string)
    i = 0
    duplicates = []
    while i < len(string):
        mycount = string.count(string[i])
        if mycount > 1:
            duplicates.append(mycount)
        i += 1 
    if len(duplicates) > 0:
        return False
    else:
        return True
