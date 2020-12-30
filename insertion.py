# applying insertion to array
def insertion_sort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[1,4,2,6,7,3]
n=len(arr)
insertion_sort(arr,n)
print("the sorted array is")
for i in range(len(arr)):
    print(arr[i])
