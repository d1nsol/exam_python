from tree import Tree
from bfs import BFS

def main():
    examTree = Tree(None, None, None)

    n = int(input())

    for i in range(n):
        examList = [int(v) for v in input().split()]

        if examList[1] == -1 :
            examList[1] = None

        if examList[2] == -1 :
            examList[2] = None

        examTree.addNode(examList[0], examList[1], examList[2])

    print(*BFS(examTree))

if __name__ == "__main__":
    main()