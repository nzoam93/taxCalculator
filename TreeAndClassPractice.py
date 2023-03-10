class binaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

node1 = binaryTreeNode(50)
node2 = binaryTreeNode(20)
node3 = binaryTreeNode(45)
node4 = binaryTreeNode(11)
node5 = binaryTreeNode(15)
node6 = binaryTreeNode(30)
node7 = binaryTreeNode(78)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

print("Root node is:", node1.data)
print("left child of node 1 is: ", node1.leftChild.data)
print("left child of node 7 is: ", node7.leftChild)
