class Node:
    def __init__(self,value,next=None):
        self.value = value  # 노드의 값을 나타내는 value
        self.next = next  # 노드의 다음위치를 가리키는 next의 초기값은 None

class linked_list:
    def __init__(self,value):
        self.head = Node(value) # 초기 클래스에 head노드선언

    def add_node(value):
        node = head           # 첫번째 위치에 해당하는 head를 생성하고, node 변수에 저장해둔다.
        while head.next:      # head노드의 다음위치에 노드가 생성될 때까지 반복문 진행한다.
            node = head.next    # head노드의 다음위치에 노드가 있는 경우(두번째 노드라고 가정),
            print(head.next)
                                # 두번째 노드부터 node변수에 저장
        node.next = Node(value)# 데이터를 노드 다음위치에 저장
