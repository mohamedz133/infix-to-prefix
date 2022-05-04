class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items[::-1])

    ############################


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def printStack(self):
        print(self.items)


########################################

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext


#################################33
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        if self.tail == None:
            self.tail = temp

    def append(self, item):
        temp = Node(item)
        if self.tail != None:
            self.tail.set_next(temp)
        self.tail = temp
        if self.head == None:
            self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def printList(self):
        current = self.head
        while current != None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print("")

    def get_head(self):
        return self.head

    def remove_head(self):
        current = self.head.get_next()
        self.head = current


###############################################

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right


class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def insert(self, key):
        if self.root:
            self._put(key, self.root)
        else:
            self.root = TreeNode(key)
        self.size = self.size + 1

    def _put(self, key, currentNode):
        if key < currentNode.value:
            if currentNode.hasLeftChild():
                self._put(key, currentNode.left)
            else:
                currentNode.left = TreeNode(key)
        else:
            if currentNode.hasRightChild():
                self._put(key, currentNode.right)
            else:
                currentNode.right = TreeNode(key)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return True
            else:
                return False
        else:
            return False

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.left)
        else:
            return self._get(key, currentNode.right)
