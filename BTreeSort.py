class treeNode:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
        self.count = 1 if value != None else 0

    def insert(self, value):
        if self.value == None:
            self.value = value
        elif value > self.value:
            if self.right == None:
                self.right = treeNode(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left == None:
                self.left = treeNode(value)
            else:
                self.left.insert(value)
        else:
            self.count += 1

    def toList(self):
        retList = []
        if self.left != None:
            retList.extend(self.left.toList())
        for i in range(self.count):
            retList.extend([self.value])
        if self.right != None:
            retList.extend(self.right.toList())
        return retList

def main(listy):
    tree = treeNode()
    for val in listy:
        tree.insert(val)
    return tree.toList()

print(main([1231,12312, 3245234, 44, 0, -1, 5465, 4]))
