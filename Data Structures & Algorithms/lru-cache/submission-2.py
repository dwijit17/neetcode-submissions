class ListNode:
    def __init__(self,key=None,val=None,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.size = 0
        self.capacity = capacity
        self.head = ListNode(key=-1,val=-1)
        self.tail = ListNode(key=-2,val=-2)
        self.head.next = self.tail
        self.tail.prev = self.head

    #function to remove a node from dll
    def remove(self,node):
        n1 = node.prev
        n2 = node.next
        n1.next = n2
        n2.prev = n1
    #function to insert a node at the end of dll
    def insert(self,node):
        oldnode = self.tail.prev
        self.tail.prev = node
        oldnode.next = node
        ###
        node.prev = oldnode
        node.next = self.tail

    def get(self, key: int) -> int:
        #return the value at key and remove and put it at end
        if key in self.hmap:
            node = self.hmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            #update that value and put it at the end of dll
            node = self.hmap[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            new_node = ListNode(key=key,val=value)
            if self.size<self.capacity:
                #means there is capacity to insert the node
                self.hmap[key] = new_node
                self.insert(new_node)
                self.size+=1
            else:
                #size exceeds capacity
                #delete the node at head
                #insert the new node
                del self.hmap[self.head.next.key]
                self.remove(self.head.next)
                self.insert(new_node)
                self.hmap[key] = new_node

        
