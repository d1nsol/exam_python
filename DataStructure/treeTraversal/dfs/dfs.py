'''
class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
'''

# DFS(깊이우선탐색)

# 전위순회
def preorder(tree):
    result = []

    result.append(tree.index)
    
    # [루트노드] + [왼쪽 전위순회] + [오른쪽 전위순회]
    if tree.left != None:
        result = result + preorder(tree.left)

    if tree.right != None:
        result = result + preorder(tree.right)

    return result

# 중위순회
def inorder(tree):
    result = []

    if tree.left != None:
        result = result + inorder(tree.left)

    result.append(tree.index)

    if tree.right != None:
        result = result + inorder(tree.right)

    return result

# 후위순회
def postorder(tree):
    result = []

    if tree.left != None:
        result = result + postorder(tree.left)

    if tree.right != None:
        result = result + postorder(tree.right)

    result.append(tree.index)
    
    return result
