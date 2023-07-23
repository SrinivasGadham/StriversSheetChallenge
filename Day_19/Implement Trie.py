from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie :

    def __init__(self) :
        self.root = TrieNode()
    
    def insert(self, string) :
        curr = self.root
        for ch in string:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    
    def search(self, word) :
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isEnd

        
    def startWith(self, prefix) :
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True



# main
t = int(input().strip())
root = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        root.insert(str1)
    
    elif (q == 2) :
        if(root.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(root.startWith(str1)) :
            print("true")

        else :
            print("false")
