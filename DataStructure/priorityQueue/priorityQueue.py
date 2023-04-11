class PriorityQueue:

    # 0 * n = 0
    def __init__(self) :
        self.data = [0]

    def push(self, value) :
        self.data.append(value)
        index = len(self.data) - 1
        
        # 마지막으로 삽입한 값이 루트노드가 되면 반복문을 종료
        while index != 1:
            if self.data[index//2] > self.data[index]:
                temp = self.data[index]
                self.data[index] = self.data[index//2]
                self.data[index//2] = temp

                index = index // 2
            else:
                break

    def pop(self) :
        if len(self.data) == 1:
            return

        # 마지막 노드를 루트 노드 자리로 이동한다.
        self.data[1] = self.data[-1]
        self.data.pop()

        index = 1
        while True:
            priority = -1
            # 1. 아무 자식도 없는 경우
            if len(self.data)-1 < index*2:
                break
            # 2. 왼쪽 자식만 있는 경우
            elif len(self.data)-1 < index*2 + 1:
                priority = index * 2
            else:
                if self.data[index*2] < self.data[index*2 + 1]:
                    priority = index*2
                else:
                    priority = index*2 + 1

            if self.data[index] > self.data[priority]:
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp

                index = priority
            else:
                break


    def top(self) :
        if len(self.data) == 1:
            return -1
        else:
            return self.data[1]
