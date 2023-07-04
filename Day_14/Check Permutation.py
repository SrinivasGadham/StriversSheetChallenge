NO_OF_CHARS = 256

def areAnagram(str1, str2):
    
    hash = [0 for i in range(NO_OF_CHARS)]

    n1 = len(str1)
    n2 = len(str2)
    
    if (n1 != n2):
       return False
    for i in range(n1):
        hash[ord(str1[i])] += 1
        hash[ord(str2[i])] -= 1
        i += 1

    
    for i in range(NO_OF_CHARS):
        if (hash[i] != 0):
            return False
    
    return True