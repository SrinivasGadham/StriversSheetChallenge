

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root)->list:
    if root==None:
        return []
    from queue import Queue
    def bfs(root):
        res=[]
        q=Queue()
        q.put(root)

        
        while q.qsize():
            l=[]
            n=q.qsize()
            while n:
                node=q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                l.append(node.data)
                n-=1
            res.append(l)
        return res
    res=bfs(root)
    final=[]
    for i in res:
        final.append(i[0])
    return final                