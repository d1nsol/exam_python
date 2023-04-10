def inorder(tree, depth):
    result = []

    if tree.left != None:
        result += inorder(tree.left, depth + 1)

    tree.setDepth(depth)
    result.append(tree)

    if tree.right != None:
        result += inorder(tree.right, depth + 1)

    return result

def getWidth(myTree):
    
    result = inorder(myTree, 1)
    n = len(result)

    # 정점의 개수는 1000개 이하(조건)
    # 깊이의 최댓값은 1000
    
    # left[i] = 깊이가 i인 모든 노드들 중에서, 가장 왼쪽에 있는 노드의 행
    # right[i] = 깊이가 i인 모든 노드들 중에서, 가장 오른쪽에 있는 노드의 행
    # 어떤 깊이의 너비는 right[i] - left[i]
    left = [1001 for i in range(1001)]
    right = [-1 for i in range(1001)]
    maxDepth = 0

    for i in range(n):
        d = result[i].depth

        left[d] = min(left[d], i)
        right[d] = max(right[d], i)

        maxDepth = max(maxDepth, d)

    asnDepth = 0
    ans = 0

    for i in range(1, maxDepth+1):
        temp = right[i] - left[i] + 1

        if ans < temp:
            ansDepth = i
            ans = temp

    return (ansDepth, ans)
