# 어떤 트리의 루트 노드를 갖고 있음
class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r
        self.depth = -1

    def setDepth(self, d):
        self.depth = d

    # 재귀적으로 동작
    # 새로운 노드가 현재 노드의 자식으로 추가되어야 하는 경우
    # -> 바로 추가
    # 그렇지 않다면, 자기 자식중에 새로운 노드를 받을 수 있는 노드를 탐색
    # -> 재귀 알고리즘
    def addNode(self, i, l, r) :

        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None

            return True
        else:
            flag = False
            
            if self.left != None:
                flag = self.left.addNode(i, l, r)
            
            if flag == False and self.right != None:
                flag = self.right.addNode(i, l, r)

            return flag
