class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def print_tree(self):
        f = open("print.txt","w")
        if self.left:
            self.left.print_tree()
        print (self.data, file = f)
        if self.right:
            self.right.print_tree()

