class Node:
    def __init__(self, value, location):
        self.value = value
        self.left = None
        self.right = None
        self.x = location[0]
        self.y = location[1]

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self):
        self.root = None
        self.preorderPath = []
        self.postorderPath = []
        self.ordering_y = dict()

    def pre_order(self, node):
        self.preorderPath.append(node.value)
        if node.left is not None:
            self.pre_order(node.left)
        if node.right is not None:
            self.pre_order(node.right)

    def post_order(self, node):
        if node.left is not None:
            self.post_order(node.left)
        if node.right is not None:
            self.post_order(node.right)
        self.postorderPath.append(node.value)

    def make_tree(self, parent, node):
        if parent.x < node.x:
            if parent.right:
                self.make_tree(parent.right, node)
            else:
                parent.right = node
        else:
            if parent.left:
                self.make_tree(parent.left, node)
            else:
                parent.left = node


def solution(nodeinfo):
    tree = Tree()
    nodes = []
    for value, location in enumerate(nodeinfo):
        nodes.append(Node(value + 1, location))
    for node in nodes:
        if node.y not in tree.ordering_y:
            tree.ordering_y[node.y] = [node]
        else:
            tree.ordering_y[node.y].append(node)
    tree.ordering_y = sorted(tree.ordering_y.items(), reverse=True)
    tree.ordering_y = [i[1] for i in tree.ordering_y]
    for i in range(len(tree.ordering_y)):
        tree.ordering_y[i] = sorted(tree.ordering_y[i], key=lambda x: x.x)
    for nodes in tree.ordering_y:
        for node in nodes:
            if tree.root is None:
                tree.root = node
            else:
                tree.make_tree(tree.root, node)

    tree.pre_order(tree.root)
    tree.post_order(tree.root)
    return [tree.preorderPath, tree.postorderPath]


print(
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
)
