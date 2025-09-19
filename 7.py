class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
# Step 2, 3, 4, 5: Function to insert a new node into the tree
def insert(root, value):
    # If tree is empty, create a new node
    if root is None:
        return Node(value)

    # If value is smaller than root → insert into left subtree
    if value < root.data:
        root.left = insert(root.left, value)

    # Else value is greater or equal → insert into right subtree
    else:
        root.right = insert(root.right, value)

    return root


# Step 6: Functions for tree traversals

# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Preorder Traversal (Root → Left → Right)
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder Traversal (Left → Right → Root)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# ---------------- MAIN PROGRAM ----------------
print("BINARY TREE IMPLEMENTATION")
print("--------------------------")

# Create an empty tree
root = None

# Insert elements one by one
values = [50, 30, 20, 40, 70, 60, 80]
for val in values:
    root = insert(root, val)

# Display all traversals
print("\nInorder Traversal   (Left → Root → Right):")
inorder(root)

print("\n\nPreorder Traversal  (Root → Left → Right):")
preorder(root)

print("\n\nPostorder Traversal (Left → Right → Root):")
postorder(root)
print()   
