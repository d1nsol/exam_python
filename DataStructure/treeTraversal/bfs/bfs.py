# BFS(너비우선탐색)

from queue import Queue

def BFS(tree):

    q = Queue()
    q.put(tree)

    result = []

    # q에 뭔가 들어있으면 계속 반복
    # -> 더 이상 방문할 노드가 없을 때 종료
    while len(q.queue) > 0:
        cur = q.get()
        if cur == None:
            continue

        result.append(cur.index) # 방문
        q.put(cur.left)
        q.put(cur.right)

    return result