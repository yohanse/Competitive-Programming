class Node:
    def __init__(self, value, go=None):
        self.val = value
        self.go = go


class FreqStack:

    def __init__(self):
        self.freq = {}
        self.num = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        val_freq =  self.num.get(val, 0) + 1
        self.max_freq = max(self.max_freq, val_freq)
        
        self.freq[val_freq] = Node(val, self.freq.get(val_freq, None))
        self.num[val] = val_freq

    def pop(self) -> int:
        val = self.freq[self.max_freq].val
        self.num[val] -= 1
        self.freq[self.max_freq] = self.freq[self.max_freq].go
        if not self.freq[self.max_freq]:
            self.max_freq -= 1
        return val


# based on the ocnstraint the push and pop has to work in o(1) time complexity or nlogn

# Let me start with the bruteforce can have stack only and whenever we push we will append to the stack and for the pop we can find oout the frequent element using dictionary and delete it from the stack by finding it is index using stack.remove(i) this would give a time O(n) for pop method and O(1) for push method so finally for m queries the time will n*m in worscase scenraion based on the constraint it won't pass

# Le define some moments 
# we have asked to track the most frequent one we can track it using dictionary the key will be the freq and the value will be someddatastrcture
# also we have asked to delete that element otimally so for delete if it is not on the top using linkedlist is very good approach if we have the node we want to delete

# could you give a minute to thinke more about it?
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()