class Node:
    def __init__( self, value):
         self.value =value
         self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
    
    def create(self, value):
        newNode = Node(value)
        if self.head==None :
            self.head = newNode

    def append(self, value):
          newNode = Node(value)
          current = self.head
          while current.next:
                current  = current.next
          current.next = newNode

    def print(self):
        nextvalue = self.head
        # print(nextvalue)
        while nextvalue:
            print(nextvalue.value)
            nextvalue = nextvalue.next
        print("None")

    def dele(self,value):
       nextvalue = self.head
       previousValue =None
       while nextvalue.next:
            if nextvalue.value == value:
                previousValue.next = nextvalue.next
                return
            previousValue= nextvalue
            nextvalue = nextvalue.next
            print(previousValue.value, nextvalue.value)

    def deltwithNumber(self, nodeNumber):
        current = self.head
        previous = None
        for r in range(nodeNumber+1):
            if r == nodeNumber:
              previous.next =  current.next
              return
            previous = current
            current= current.next
                 
                
               
          
               
                
 
    


list = LinkedList()


list.create(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

list.dele(3)
# print("hello")
list.print()
list.deltwithNumber(2)

list.print()
