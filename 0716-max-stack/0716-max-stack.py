class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.root = None
    
    def insert(self, node):
        if self.root:
            self.root.prev = node
        node.next = self.root
        self.root = node
        return node
    
    def delete(self):
        node = self.root
        self.root = self.root.next
        if self.root:
            self.root.prev = None
        return node
    
    def delete_node(self, node):
        if node.prev is None:
            self.root = self.root.next
            if self.root:
                self.root.prev = None
        else:
            prev = node.prev
            prev.next = node.next
            if node.next:
                node.next.prev = prev
    
    def top(self):
        return self.root


class Heap:
    def __init__(self):
        self.heap = []
    
    def insert(self, node):
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)
        return node
    
    def peak(self):
        return self.heap[0]
    
    def delete(self):
        self._swap(0, -1)
        max_node = self.heap.pop()
        self._heapify_down(0)
        
        return max_node
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _find_parent(self, idx):
        return (idx - 1) // 2
    
    def _find_left_child(self, idx):
        return 2*idx + 1
    
    def _find_right_child(self, idx):
        return 2*idx + 2
    
    def _heapify_up(self, idx):
        par_idx = self._find_parent(idx)

        if idx > 0 and self.heap[par_idx].val <= self.heap[idx].val:
            self._swap(par_idx, idx)
            self._heapify_up(par_idx)
    
    def _heapify_down(self, idx):
        left_idx = self._find_left_child(idx)
        right_idx = self._find_right_child(idx)
        max_child_idx = idx

        if left_idx < len(self.heap) and self.heap[left_idx].val > self.heap[max_child_idx].val:
            max_child_idx = left_idx
        
        if right_idx < len(self.heap) and self.heap[right_idx].val > self.heap[max_child_idx].val:
            max_child_idx = right_idx
            
        if max_child_idx != idx:
            self._swap(max_child_idx, idx)
            self._heapify_down(max_child_idx)
        
            


class MaxStack:

    def __init__(self):
        self.linkedlist = LinkedList()
        self.heap = Heap()
        self.removed = set()

    def push(self, x: int) -> None:
        node = Node(x)
        self.heap.insert(node)
        self.linkedlist.insert(node)

    def pop(self) -> int:
        node = self.linkedlist.delete()
        while node in self.removed:
            node = self.linkedlist.delete()
        self.removed.add(node)
        return node.val

    def top(self) -> int:
        node = self.linkedlist.top()
        while node in self.removed:
            self.linkedlist.delete()
            node = self.linkedlist.top()
        return node.val

    def peekMax(self) -> int:
        node = self.heap.peak()
        while node in self.removed:
            self.heap.delete()
            node = self.heap.peak()
        return node.val

    def popMax(self) -> int:
        node = self.heap.delete()
        while node in self.removed:
            node = self.heap.delete()
        self.removed.add(node)
        return node.val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()