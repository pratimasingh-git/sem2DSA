class Node:
    def __init__(self,mydata):
        self.data= mydata
        self.address=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtFirstPosition(self, mydata):
        newNode= Node(mydata)
        newNode.address=self.head
        self.head=newNode

    def traversal(self):
        currentNode= self.head
        while currentNode != None:
            print(currentNode.data, end=" -> ")
            currentNode=currentNode.address


myLinkedList= LinkedList()
myLinkedList.insertAtFirstPosition(10)
myLinkedList.insertAtFirstPosition(20)
myLinkedList.insertAtFirstPosition(30)

myLinkedList.traversal()