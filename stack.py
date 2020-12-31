# implementation of stack and find min and max value in stack
class Node: 
    
    def __init__(self, value): 
        self.value = value 
        self.next = None
    
    
    def __str__(self): 
        return "Node({})".format(self.value) 
      
   
    __repr__ = __str__ 
    
  
class Stack: 
    
    def __init__(self): 
        self.top = None
        self.count = 0
        self.maximum = None
        self.minimum=None

    def __str__(self): 
        temp=self.top 
        out=[] 
        while temp: 
            out.append(str(temp.value)) 
            temp=temp.next
        out='\n'.join(out) 
        return ('Top {} \n\nStack :\n{}'.format(self.top,out)) 
     
    __repr__=__str__ 
      
    
    def getMax(self): 
        if self.top is None: 
            return "Stack is empty"
        else: 
            print("Maximum Element in the stack is: {}" .format(self.maximum)) 
    
    def getmin(self):
        if self.top is None:
            return "stack is empty"
        else:
            print("minimum element in the stack is:{}".format(self.minimum))
  
   
  
    # Method to check if Stack is Empty or not 
    def isEmpty(self): 
        # If top equals to None then stack is empty  
        if self.top == None: 
            return True
        else: 
        # If top not equal to None then stack is empty  
            return False
  
    # This method returns length of stack        
    def __len__(self): 
        self.count = 0
        tempNode = self.top 
        while tempNode: 
            tempNode = tempNode.next
            self.count+=1
        return self.count 
  
  
    def push(self,value): 
        if self.top is None: 
            self.top = Node(value) 
            self.maximum = value 
            self.minimum=value
              
        elif value > self.maximum : 
            temp = (2 * value) - self.maximum 
            new_node = Node(temp) 
            new_node.next = self.top 
            self.top = new_node 
            self.maximum = value 
        elif value<self.minimum:
            temp = (2 * value) - self.minimum 
            new_node = Node(temp) 
            new_node.next = self.top 
            self.top = new_node 
            self.minimum = value 

        else: 
            new_node = Node(value) 
            new_node.next = self.top 
            self.top = new_node 
        print("Number Inserted: {}" .format(value)) 
    
    
 # Driver program to test above class   
stack = Stack()  
  
stack.push(3) 
stack.push(5)  
stack.push(7) 
stack.push(19) 
stack.getMax()
stack.getmin()


  