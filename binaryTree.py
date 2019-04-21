class Node():
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class tree():
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        print(self.root)
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return # return 后的语句不会被执
            else:
                queue.append(cur_node.lchild)
                
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def zhongxu(self):
        if self.root == None:
            return
        queue = [self.root]
        while queue:
            q = queue.pop(0)
            print(q.elem)
            if q.lchild is not None:
                queue.append(q.lchild)
            if q.rchild is not None:
                queue.append(q.rchild)

    def preorder(self,node):
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem)
        self.inorder(node.rchild)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem)
            
    

    
        
            

if __name__=='__main__':
    t=tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    
    
    
