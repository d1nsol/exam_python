def getHeight(myTree):

    # 루트노드를 포함해서, 왼쪽 서브트리와 오른쪽 서브트리를 모두 포함
    # 왼쪽 서브트리의 높이를 구해보고,
    # 오른쪽 서브트리의 높이를 구해보고,,
    # 두 높이를 비교
    # 왼쪽 서브트리의 높이 + 1(루트노드)

    if myTree == None:
        return 0
    else:
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))