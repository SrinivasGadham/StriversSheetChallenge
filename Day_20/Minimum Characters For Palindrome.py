

 



def isPalindrome(str):

 

    l = len(str)

    i = 0

    j = l - 1

 

    while i < j:

        if str[i] != str[j]:

            return False

        i += 1

        j -= 1

 

    return True

 

def minCharsforPalindrome(str):

 

    count = 0

 

    while len(str) > 0:

 

        

        if isPalindrome(str):

            break

 

        

        else:

            count += 1

            str = str[:-1]

 

    return count