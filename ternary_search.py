# it is divide and conquer algorithm
# it is similar to the binary search where we divide array in two parts but here we divide array into three part.

def ternary_search(l,r,key,arr):
    if (r>=l):
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if (arr[mid1]==key):
            return mid1
        if (arr[mid2]==key):
            return mid2
        if (arr[mid1]>key):
            return (ternary_search(l,mid1-1,key,arr))
        elif (arr[mid2]<key):
            return (ternary_search(mid2+1,r,key,arr))
        else:
            return ternary_search(mid1+1,mid2-1,key,arr)
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
l=0
r=9
key=5
p=ternary_search(l,r,key,arr)
print("index of",key,"is",p)
