# day2 assignment
#delete an element from begining
def delete_array_begining(arr):
    if len(arr)<1:
        print("array is empty cant delete")
    else:
        # for i in range(len(arr)):
        # del_element=arr1.array('i',arr)
        # del del_element[0]
        my_list=arr
        my_list.remove(arr[0])
        print("array after deleting first element:",my_list)
    print()

arr=[1,4,5,6,7,3]
print("the elements in array are:",arr)
delete_array_begining(arr)

# delete an element at end
def delete_element_at_end(arr):
    if len(arr)>1:
        l=arr
        l.remove(arr1[-1])
        print("after deleting last element:",l)
    print()
arr1=[1,3,4,5,6]
print("the element in the array:",arr1)
delete_element_at_end(arr1)


# delete an element at particular position
# import array as arr1
def del_at_position(arr,k):
    new_list=[]
    if len(arr)>1:
        # print("elements are greater than 1")
        for i in range(len(arr)):
            if i!=k:
                new_list.append(arr[i])
        print("array after delete at particular position",new_list)
                
                
arr=[1,4,2,6,3,8]
print("the elements in the array are:",arr)
k=3
del_at_position(arr,k)           