def Check_Vow(string, vowels):

    # casefold has been used to ignore cases
    string = string.casefold()

    # Forms a dictionary with key as a vowel
    # and the value as 0
    count = {}.fromkeys(vowels, 0)

    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1
    return count

# Driver Code
vowels = 'aeiou'
string=input("enter string to count number of vowels in it:")
print (Check_Vow(string, vowels))
