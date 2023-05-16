def count_characters_in_string(mystring):
    s=0
    
    for string in mystring:
        if string.isalpha():
            s=s+1          
    print("The number of characters in this string is:",s)
    print("The length in this string is:",len(mystring))

count_characters_in_string("Apple123")