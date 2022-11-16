import heapq


class node:
    def __init__(self, freq, char, left='', right=''):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


def printNodes(root, code):
    newCode = code+root.huff

    if root.left:
        printNodes(root.left, newCode)

    if root.right:
        printNodes(root.right, newCode)

    if not root.left and not root.right:
        print(root.char, newCode)


if __name__ == "__main__":
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [5, 9, 12, 13, 16, 45]
    nodes = []

    for i in range(len(chars)):
        heapq.heappush(nodes, node(freq[i], chars[i]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = '0'
        right.huff = '1'

        heapq.heappush(nodes, node(left.freq+right.freq,
                                   left.char+right.char, left, right))
    printNodes(nodes[0], "")
