import sys
import argparse
import collections

class Stacks:
    num_list=[]
    slist=[]
    
    def __init__(self,num_list):
        self.num_list=num_list
        
    def stack_op(self):
        for i in range(len(self.num_list)-1,-1,-1):
            self.slist.append(self.num_list[i])
        
        print("arguments                stack")
        for i in range(len(self.num_list)):
            print(f"   |{self.num_list[i]}|                    |{self.slist[i]}|")
        print("    |_stack operation LIFO_|")
    
    def pop(self):
        self.slist.pop()
        return self.num_list.pop()
        
    def top_of_stack(self):
        print(self.num_list[len(self.num_list)-1])
    
    def peek(self):
        if self.num_list:
            print("stack is not empty as bottom is: ",self.num_list[0])
        else:
            print("Stack is empty")
    
    def push(self,ele):
        self.num_list.append(ele)
        print(f"top-->|{self.num_list[len(self.num_list)-1]}|")
        for i in range(len(self.num_list)-2,-1,-1):
            print(f"      |{self.num_list[i]}|")
    
    
class Queue:
    num_list=[]
    de = []
    
    def __init__(self,num_list):
        self.num_list=num_list
        self.de = collections.deque(self.num_list)
        
    def queue_op(self):
        print("arguments themselves form the queue: ",end='')
        for i in self.num_list:
            print(i,"|",end=' ')
    
    def enque(self,num):
        self.de.append(num)
        print("The new queue is:                    ",end='')
        for i in self.de:
            print(i,"|",end=' ')
        
    def deq(self):
        print("removed from front:",self.de.popleft(),end='')
        print(", remaining q: ",end=' ')
        for i in self.de:
            print(i,"|",end=' ')
        
    
    def front(self):
        print(self.de[0])
        
    
if __name__=='__main__':
    parser = argparse.ArgumentParser()
        
    if sys.argv[1]=="--Stacks":
        parser.add_argument('--Stacks',type=str)
        args = parser.parse_args()
        li_list1 = args.Stacks.split(',')
        stacklist=[]
        for i in li_list1:
            stacklist.append(int(i))
        s=Stacks(stacklist)
        print("\n*******Performing stack operations********\n ***************************************")
        s.stack_op()
        
        print("\npeeking: ")
        s.peek()
        
        pop=s.pop()
        print(f"\npopping an element from top: {pop}")
        
        print("\nnow top of the stack is: ",end='')
        s.top_of_stack()
        
        x=int(input("\nfor push operation, enter the new element: "))
        s.push(x)
    
    else:
        parser.add_argument('--Queues',type=str)
        args = parser.parse_args()
        li_list2 = args.Queues.split(',')
        queuelist=[]
        for i in li_list2:
            queuelist.append(i)
        
        q=Queue(queuelist)
        
        print("\n*******Performing queue operations********\n ****************************************")
        q.queue_op()
        
        print("\n\nfront of the queue has: ",end='')
        q.front()
        
        q.deq()
               
        x=int(input("\n\nfor enqueue opperation, enter the new element: "))
        q.enque(x)
    
        
    

    
    