class BSTiterator:
    def __init__(self, root):
        self.st=[]
        while root:
            self.st.append(root)
            root=root.left

    def next(self):
        res=self.st.pop()
        curr=res.right
        while curr:
            self.st.append(curr)    
            curr=curr.left
        return res.data

    def hasNext(self):
        return self.st!=[]