
class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
          
class MinMax:  
    #Represent the head and tail of the singly linked list  
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
          
    #addNode() will add a new node to the list  
    def addNode(self, data):  
        #Create a new node  
        newNode = Node(data);  
          
        #Checks if the list is empty  
        if(self.head == None):  
            #If list is empty, both head and tail will point to new node  
            self.head = newNode;  
            self.tail = newNode;  
        else:  
            #newNode will be added after tail such that tail's next will point to newNode  
            self.tail.next = newNode;  
            #newNode will become new tail of the list  
            self.tail = newNode;  
              
    #minNode() will find out the minimum value node in the list  
    def minNode(self):  
        current = self.head;  
          
        if(self.head == None):  
            print("List is empty");  
        else:  
            #Initializing min with head node data  
            min = self.head.data;  
              
            while(current != None):  
                #If current node's data is smaller than min  
                #Then, replace value of min with current node's data  
                if(min > current.data):  
                    min = current.data;  
                current = current.next;  
            print("Minimum value node in the list: " + str(min));  
              
    #maxNode() will find out the maximum value node in the List  
    def maxNode(self):  
        current = self.head;  
          
        if(self.head == None):  
            print("List is empty");  
        else:  
            #Initializing max with head node data  
            max = self.head.data;  
              
            while(current != None):  
                #If current node's data is greater than max  
                #Then, replace value of max with current node's data  
                if(max < current.data):  
                    max = current.data;  
                current= current.next;  
            print("Maximum value node in the list: " + str(max));  
   
sList = MinMax();      
          
#Adds data to the list  
sList.addNode(5);  
sList.addNode(8);  
sList.addNode(1);  
sList.addNode(6);  
   
#Display the minimum value node in the list  
sList.minNode();  
   
#Display the maximum value node in the list  
sList.maxNode();  