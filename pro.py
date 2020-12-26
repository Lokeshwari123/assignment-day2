# python program of left rotation of an array k number of times
def leftrotate(arr,n,k):
    mod=k%n
    # s=" "
    for i in range(n):
        print(str(arr[(mod+i)%n]))
    print()
    return
arr=[1,3,5,8,9]
n=len(arr)
k=2
leftrotate(arr,n,k)