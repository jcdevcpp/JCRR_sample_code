#!/bin/python3
import ittertools
'''linked list implementation'''
class LinkedList:
    def __init__(self, nodes=None):        
        self.head=None
        if nodes is not None:#if a list of str data points is passed at initial instantiation
            nodes.reverse()
            node=LLNode(nodes.pop())
            node.next=LLNode(nodes[-1])
            self.head=node
            while len(nodes)>1:
                node.next.next=LLNode(nodes[-2])
                nodes.pop()
                node=node.next
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def add_to_first_pos(self, data):
        inode=LLNode(data)
        inode.next=self.head
        self.head=inode

    def add_to_end_pos(self, data):
        if self.head:
            for enode in self:
                pass
            enode.next=LLNode(data)
            return
        self.head=LLNode(data)

    def insert_after(self, data, new_data):
        node=LLNode(new_data)
        if self.head:  
            for nodei in self:
                if nodei.data == data:
                    node.next=nodei.next
                    nodei.next=node
                    return
            raise Exception(f"Target node {data} not found")
        raise Exception("empty list")

    def insert_before(self, data, new_data):
        
        if self.head is None:
            raise Exception("empty list")
        elif self.head.data==data:
            self.add_to_first_pos(new_data)
            return
            
        node=LLNode(new_data)
        prev_node=self.head

        for nodei in self:
            if nodei.data == data:
                prev_node.next=node
                node.next=nodei
                return
            prev_node=nodei
        raise Exception(f"Target node {data} not found")

    def remove(self, data):

        if self.head is None:
            raise Exception("empty list")
        prev_node=self.head
        
        if prev_node.data == data:
            self.head=prev_node.next
            return

        for nodei in self:
            if nodei.data == data:
                prev_node.next=nodei.next
                return
            prev_node=nodei
        raise Exception(f"Target node {data} not found")

    def get(self, idx):

        for j, node in enumerate(self):
            if idx==j:
                return node
        raise Exception("index out of list bound")

    def reverse(self):
        if self.head is None:
            raise Exception("empty list")

        reversed_list=LinkedList()
        #create tail
        past_node=LLNode(self.head.data)
        past_node.next=None
        for idx, node in enumerate(self):
            if idx==0: 
                continue
            link_node=LLNode(node.data)
            link_node.next=past_node
            past_node=link_node
        reversed_list.head=past_node
        return reversed_list    

    def __repr__(self):
        node=self.head
        nodes=[]
        while node is not None:
            nodes.append(node.data)
            node=node.next
        nodes.append("None")
        return " -> ".join(nodes)

class QueueFromList(LinkedList):
    def enqueue(self, data):
        LinkedList.add_to_end_pos(self, data)
    def dequeue(self, data=None):
        if self.head is None:
            raise Exception("empty list")
        prev_node=self.head

        # if just one element and it matches for deletion or if dequeueing a one element list
        if (prev_node.data == data and (data is not None)) or (data is None):
            if prev_node.next is None:#check if it is the tail value
                self.head=prev_node.next            
                return
            if data:
                raise Exception("not tail element, forbidden to delete")

        for nodei in self:
            if (nodei.data == data and (data is not None)) or (data is None):
                if nodei.next is None:
                    prev_node.next=nodei.next
                    return
                if data:
                    raise Exception("not tail element, forbidden to delete")    
            prev_node=nodei
        raise Exception(f"Target node {data} not found")


class LLNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return self.data

if __name__=="__main__":

    linked_list=LinkedList(["one", "two", "three","four","five"])
    print(f'{linked_list = }')
    print([node for node in linked_list])
    linked_list.add_to_first_pos("zero")
    print(f'{linked_list = }')
    linked_list.add_to_end_pos("six")
    print(f'{linked_list = }')
    linked_list.insert_after("two","two&half")
    print(f'{linked_list = }')
    linked_list.insert_before("zero","minus_one")
    print(f'{linked_list = }')
    linked_list.insert_before("four","three&half")
    print(f'{linked_list = }')
    linked_list.remove("four")
    print(f'{linked_list = }')
    queue_obj=QueueFromList([str(dat) for dat in linked_list.reverse()])
    print(f'{queue_obj = }')
    queue_obj.dequeue("minus_one")
    print(f'{queue_obj = }')
    try:
        while True:
            queue_obj.dequeue()
            print(f'{queue_obj = }')
    except Exception as e:
        print(e)
        print(count(5))
