import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    @property
    def parent(self):
        # weakref is proxy, call the name can return the real object
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

def test():
    root = Node('root')
    c1 = Node('child01')
    root.add_child(c1)
    print(c1.parent)
    print(root.parent)


if __name__ == "__main__":
    test()