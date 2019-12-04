class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def addChild(self, node):
        self._children.append(node)


def test():
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    root.addChild(node1)
    root.addChild(node2)

    for n in root:
        print(n)

if __name__ == "__main__":
    test()